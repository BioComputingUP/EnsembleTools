import os
import sys
from typing import List, Sequence, Tuple, Union
import mdtraj
import numpy as np

from idpet.featurization.angles import featurize_a_angle, featurize_phi_psi, featurize_tr_angle
from idpet.featurization.distances import featurize_ca_dist
from idpet.featurization.glob import compute_asphericity, compute_end_to_end_distances, compute_ensemble_sasa, compute_prolateness
from idpet.featurization.ensemble_level import calc_flory_scaling_exponent
from idpet.data.io_utils import setup_data_dir
from idpet.utils import logger


class Ensemble():
    """
    Represents a molecular dynamics ensemble.

    Parameters
    ----------
    code : str
        The code identifier of the ensemble.

    data_path : str, optional
        The path to the data file associated with the ensemble. It could be a path to one multi-model pdb file 
        , a path to a folder contain pdb files for each model, or .xtc , .dcd trajectory files. Default is None.

    top_path : str, optional
        The path to the topology file associated with the ensemble. In case of having trajectory file. Default is None.

    database : str, optional
        The database from which to download the ensemble. Options are 'ped' and 'atlas'. Default is None.
        
    chain_id : str, optional
        Chain identifier used to select a single chain to analyze in case multiple chains are loaded. Default is None.

    residue_range : Tuple, optional
        A tuple indicating the start and end of the residue range (inclusive), using 1-based indexing. Default is None.

    Notes
    -----
    - If the database is 'atlas', the ensemble code should be provided as a PDB ID with a chain identifier separated by an underscore. Example: '3a1g_B'.
    - If the database is 'ped', the ensemble code should be in the PED ID format, which consists of a string starting with 'PED' followed by a numeric identifier, and 'e' followed by another numeric identifier. Example: 'PED00423e001'.
    - The `residue_range` parameter uses 1-based indexing, meaning the first residue is indexed as 1.
    """
    def __init__(self, code: str, data_path: str = None, top_path: str = None, database: str = None, chain_id: str = None, residue_range: Tuple = None) -> None:
        self.code = code
        self.data_path = data_path
        self.top_path = top_path
        self.database = database
        self.chain_id = chain_id
        self.residue_range = residue_range
        self.trajectory = None
    
    def _save_clean_topology(self, frame, output_path):
        # Get actual residue numbers from topology (includes negatives)
        """Save a clean topology to a PDB file with corrected residue numbering.
        if the residue numbering in the PDB file is not starting from 1, this function will shift the residue numbers to start from 1.
        This is useful for ensuring compatibility with other tools that expect residue numbering to start from 1"""
        pdb_res_nums = [res.resSeq for res in frame.topology.residues]
        min_residue_number = min(pdb_res_nums)
        shift = 1 - min_residue_number if min_residue_number <= 0 else 0

        atom_res_map = {atom.index: atom.residue.index for atom in frame.topology.atoms}

        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".pdb", delete=False) as temp_pdb:
            frame.save(temp_pdb.name)
            with open(temp_pdb.name, 'r') as f:
                lines = f.readlines()

        with open(output_path, 'w') as f:
            for line in lines:
                if line.startswith(("ATOM", "HETATM")):
                    atom_idx = int(line[6:11]) - 1  # PDB atom serials are 1-based
                    res_idx = atom_res_map[atom_idx]
                    original_resnum = pdb_res_nums[res_idx]
                    corrected_resnum = original_resnum + shift
                    line = line[:22] + f"{corrected_resnum:4d}" + line[26:]
                f.write(line)




    def load_trajectory(self, data_dir: str = None):
        """
        Load a trajectory for the ensemble.

        Parameters
        ----------
        data_dir : str, optional
            The directory where the trajectory data is located or where generated trajectory files will be saved.

        Notes
        -----
        This method loads a trajectory for the ensemble based on the specified data path. 
        It supports loading from various file formats such as PDB, DCD, and XTC.
        If the data path points to a directory, it searches for PDB files within the directory 
        and generates a trajectory from them.
        If the data path points to a single PDB file, it loads that file and generates a trajectory.
        If the data path points to a DCD or XTC file along with a corresponding topology file (TOP), 
        it loads both files to construct the trajectory.
        Additional processing steps include checking for coarse-grained models, selecting a single chain 
        (if applicable), and selecting residues of interest based on certain criteria.
        """
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(
                f"Data file or directory for ensemble {self.code} doesn't exist: {self.data_path}"
            )
        elif self.data_path.endswith('.pdb'):
            chain_ids = self.get_chains_from_pdb()
            logger.info(f"{self.code} chain ids: {chain_ids}")
            
            logger.info(f"Generating trajectory for {self.code}...")
            self.trajectory = mdtraj.load(self.data_path)

            chain_selected = self._select_chain(chain_ids)

            if chain_selected:
                traj_suffix = f'_{self.chain_id.upper()}'
            else:
                traj_suffix = ''

            # Saves files for faster access next time the data is loaded.
            setup_data_dir(data_dir)
            traj_dcd = os.path.join(data_dir, f'{self.code}{traj_suffix}.dcd')
            traj_top = os.path.join(data_dir, f'{self.code}{traj_suffix}.top.pdb')
            
            self.trajectory.save(traj_dcd)
            self._save_clean_topology(self.trajectory[0], traj_top)
            
            logger.info(f"Generated trajectory saved to {data_dir}.")
        elif self.data_path.endswith(('.dcd', '.xtc')):
            logger.info(f"Loading trajectory for {self.code}...")
            self.trajectory = mdtraj.load(self.data_path, top=self.top_path)
        elif os.path.isdir(self.data_path):
            files_in_dir = [f for f in os.listdir(self.data_path) if f.endswith('.pdb')]
            if files_in_dir:
                chain_ids = self.get_chains_from_pdb()
                logger.info(f"{self.code} chain ids: {chain_ids}")

                logger.info(f"Generating trajectory for {self.code}...")
                full_paths = [os.path.join(self.data_path, file) for file in files_in_dir]
                self.trajectory = mdtraj.load(full_paths)
                
                chain_selected = self._select_chain(chain_ids)

                if chain_selected:
                    traj_suffix = f'_{self.chain_id.upper()}'
                else:
                    traj_suffix = ''

                setup_data_dir(data_dir)
                traj_dcd = os.path.join(data_dir, f'{self.code}{traj_suffix}.dcd')
                traj_top = os.path.join(data_dir, f'{self.code}{traj_suffix}.top.pdb')
                self.trajectory.save(traj_dcd)
                self._save_clean_topology(self.trajectory[0], traj_top)
                logger.info(f"Generated trajectory saved to {data_dir}.")
            else:
                raise FileNotFoundError(f"No PDB files found in directory: {self.data_path}")
        else:
            raise ValueError(f"Unsupported file format for data file: {self.data_path}")

        if self.trajectory.topology.n_chains > 1:
            raise ValueError(f"Multiple chains found for ensemble {self.code}. "
                             "Chain selection is only supported for PDB files.")
        
        # Save the trajectory for sampling
        self.original_trajectory = self.trajectory
        # Check if a coarse-grained model was loaded
        self._check_coarse_grained()
        # Select residues
        self._select_residues()
        
    def _check_coarse_grained(self):
        residues = self.trajectory.topology.residues
        self.coarse_grained = all(len(list(res.atoms)) == 1 for res in residues)
        self.atom_selector = "all" if self.coarse_grained else "name == CA"

    def random_sample_trajectory(self, sample_size: int):
        """
        Randomly sample frames from the original trajectory.

        Parameters
        ----------
        sample_size : int
            The number of frames to sample from the original trajectory.

        Notes
        -----
        This method samples frames randomly from the original trajectory and updates the ensemble's trajectory attribute.
        """
        
        total_frames = len(self.original_trajectory)
        if sample_size > total_frames:
            raise ValueError("Sample size cannot be larger than the total number of frames in the trajectory.")
        random_indices = np.random.choice(total_frames, size=sample_size, replace=False)
        self.trajectory = mdtraj.Trajectory(
            xyz=self.original_trajectory.xyz[random_indices],
            topology=self.original_trajectory.topology)
        self._select_residues()
        logger.info(f"{sample_size} conformations sampled from {self.code} trajectory.")
        
    def extract_features(self, featurization: str, *args, **kwargs):
        """
        Extract features from the trajectory using the specified featurization method.

        Parameters
        ----------
        featurization : str
            The method to use for feature extraction. Supported options: 'ca_dist', 'phi_psi', 'a_angle', 'tr_omega', 'tr_phi', and 'ca_phi_psi'.
        min_sep : int, optional
            The minimum sequence separation for angle calculations. Required for certain featurization methods.
        max_sep : int, optional
            The maximum sequence separation for angle calculations. Required for certain featurization methods.

        Notes
        -----
        This method extracts features from the trajectory using the specified featurization method and updates the ensemble's features attribute.
        """
        logger.info(f"Performing feature extraction for Ensemble: {self.code}.")

        if featurization == "ca_dist":
            features, names = featurize_ca_dist(
                traj=self.trajectory, 
                get_names=True,
                atom_selector=self.atom_selector,
                *args, **kwargs)
        elif featurization == "phi_psi":
            features, names = featurize_phi_psi(
                traj=self.trajectory, 
                get_names=True,
                *args, **kwargs)
        elif featurization == "a_angle":
            features, names = featurize_a_angle(
                traj=self.trajectory, 
                get_names=True, 
                atom_selector=self.atom_selector,
                *args, **kwargs)
        elif featurization == "tr_omega":
            features, names = featurize_tr_angle(
                traj=self.trajectory,
                type="omega",
                get_names=True,
                *args, **kwargs)
        elif featurization == "tr_phi":
            features, names = featurize_tr_angle(
                traj=self.trajectory,
                type="phi",
                get_names=True,
                *args, **kwargs)
        elif featurization == "ca_phi_psi":
            features_ca, names_ca = featurize_ca_dist(
                traj=self.trajectory, 
                get_names=True,
                atom_selector=self.atom_selector,
                *args, **kwargs)
            features_phi_psi, names_phi_psi = featurize_phi_psi(
                traj=self.trajectory, 
                get_names=True,
                *args, **kwargs)
            features = np.concatenate((features_ca, features_phi_psi), axis=1)
            names = names_ca + names_phi_psi
        else:
            raise NotImplementedError("Unsupported feature extraction method.")

        self.features = features
        self.names = names
        logger.info(f"Transformed ensemble shape: {self.features.shape}")

    def get_features(self, featurization: str, normalize: bool = False, *args, **kwargs) -> Sequence:
        """
        Get features from the trajectory using the specified featurization method.

        Parameters
        ----------
        featurization : str
            The method to use for feature extraction. Supported options: 'ca_dist', 'phi_psi', 'a_angle', 'tr_omega', 'tr_phi', 'rg', 'prolateness', 'asphericity', 'sasa', 'end_to_end'.
        min_sep : int
            The minimum sequence separation for angle calculations.
        max_sep : int
            The maximum sequence separation for angle calculations.
        
        Returns
        -------
        features : Sequence
            The extracted features.

        Notes
        -----
        This method extracts features from the trajectory using the specified featurization method.
        """
        if featurization == "ca_dist":
            return featurize_ca_dist(
                traj=self.trajectory, 
                get_names=False,
                atom_selector=self.atom_selector,
                *args, **kwargs)
        elif featurization == "phi_psi":
            return featurize_phi_psi(
                traj=self.trajectory, 
                get_names=False,
                *args, **kwargs)
        elif featurization == "a_angle":
            return featurize_a_angle(
                traj=self.trajectory, 
                get_names=False, 
                atom_selector=self.atom_selector,
                *args, **kwargs)
        elif featurization == "tr_omega":
            return featurize_tr_angle(
                traj=self.trajectory,
                type="omega",
                get_names=False,
                *args, **kwargs)
        elif featurization == "tr_phi":
            return featurize_tr_angle(
                traj=self.trajectory,
                type="phi",
                get_names=False,
                *args, **kwargs)
        elif featurization == "rg":
            return mdtraj.compute_rg(self.trajectory)
        elif featurization == "prolateness":
            return compute_prolateness(self.trajectory)
        elif featurization == "asphericity":
            return compute_asphericity(self.trajectory)
        elif featurization == "sasa":
            return compute_ensemble_sasa(self.trajectory)
        elif featurization == "end_to_end":
            return compute_end_to_end_distances(self.trajectory, self.atom_selector, normalize)
        elif featurization == "ee_on_rg":
            ee = compute_end_to_end_distances(self.trajectory, self.atom_selector)
            rg = mdtraj.compute_rg(self.trajectory).mean()
            return ee/rg
        elif featurization == "flory_exponent":
            return calc_flory_scaling_exponent(self.trajectory)
        else:
            raise NotImplementedError("Unsupported feature extraction method.")
        
    def normalize_features(self, mean: float, std: float):
        """
        Normalize the extracted features using the provided mean and standard deviation.

        Parameters
        ----------
        mean : float
            The mean value used for normalization.
        std : float
            The standard deviation used for normalization.

        Notes
        -----
        This method normalizes the ensemble's features using the provided mean and standard deviation.
        """
        self.features = (self.features - mean) / std
    
    def _select_chain(self, chain_ids: List[str]) -> bool:
        """
        Select a specific chain from the trajectory based on the chain_id.

        Parameters
        ----------
        chain_ids: List[str]
            A list of chain IDs available in the trajectory.

        Returns
        -------
        bool
            True if a chain was selected, False otherwise.
        """
        if self.trajectory.topology.n_chains == 1:
            return False

        chain_id_to_index = {chain_id.upper(): index for index, chain_id in enumerate(chain_ids)}

        if self.chain_id is None:
            raise ValueError(f"Multiple chains found in the ensemble {self.code}. Please specify a chain_id from {chain_ids}.")

        chain_id_upper = self.chain_id.upper()

        if chain_id_upper not in chain_id_to_index:
            raise ValueError(f"Chain ID '{self.chain_id}' is not present in the ensemble.")

        chain_index = chain_id_to_index[chain_id_upper]

        chain_indices = self.trajectory.topology.select(f"chainid {chain_index}")
        self.trajectory = self.trajectory.atom_slice(chain_indices)
        logger.info(f"Chain {chain_id_upper} selected from ensemble {self.code}.")

        return True

    def _validate_residue_range(self):
        """
        Validate the residue range to ensure it's within the valid range of residues in the trajectory.
        """
        if self.residue_range is None:
            return
        start_residue, end_residue = self.residue_range

        total_residues = self.trajectory.topology.n_residues

        if not (1 <= start_residue <= total_residues):
            raise ValueError(f"Start residue {start_residue} is out of range. Must be between 1 and {total_residues}.")
        if not (1 <= end_residue <= total_residues):
            raise ValueError(f"End residue {end_residue} is out of range. Must be between 1 and {total_residues}.")
        if start_residue > end_residue:
            raise ValueError(f"Start residue {start_residue} must be less than or equal to end residue {end_residue}.")

    def _select_residues(self):
        """
        Modify self.trajectory to only include residues within self.residue_range.
        """
        if self.residue_range is None:
            return
        self._validate_residue_range()
        start_residue, end_residue = self.residue_range
        atom_indices = self.trajectory.topology.select(f'residue >= {start_residue} and residue <= {end_residue}')
        self.trajectory = self.trajectory.atom_slice(atom_indices)
        logger.info(f"Selected residues from ensemble {self.code}")
    
    def get_num_residues(self):
        return self.trajectory.topology.n_residues

    def get_chains_from_pdb(self):
        """
        Extracts unique chain IDs from a PDB file.
        
        Raises
        ------
        FileNotFoundError
            If the specified PDB file or directory does not exist, or if no PDB file is found in the directory.
        ValueError
            If the specified file is not a PDB file and the path is not a directory.
        """
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"The path {self.data_path} does not exist.")
        
        if os.path.isdir(self.data_path):
            # Use the only one .pdb file
            files = os.listdir(self.data_path)
            pdb_files = [file for file in files if file.endswith('.pdb')]
            if not pdb_files:
                raise FileNotFoundError(f"No PDB file found in the directory {self.data_path}.")
            pdb_file = os.path.join(self.data_path, pdb_files[0])
        else:
            if not self.data_path.endswith('.pdb'):
                raise ValueError(f"The file {self.data_path} is not a PDB file.")
            pdb_file = self.data_path

        with open(pdb_file, 'r') as f:
            lines = f.readlines()

        chain_ids = []  # Use a list to preserve the order

        for line in lines:
            if line.startswith('ATOM'):
                chain_id = line[21]
                if chain_id not in chain_ids:
                    chain_ids.append(chain_id)

        return chain_ids
    
    def get_size(self) -> int:
        """Return the number of conformations in an ensemble, if data has been
        loaded."""
        if self.trajectory is None:
            raise ValueError("No ensemble data")
        else:
            return len(self.trajectory)
        
