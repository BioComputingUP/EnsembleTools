import os
import tarfile
from pathlib import Path

def get_output_dir(output_dir: str):
    if output_dir is None:
        return os.getenv(
            "IDPET_OUTPUT_DIR",  # If defined, gets an environmental variable.
            str(Path.home() / ".idpet" / "data")  # Else, uses a default path.
        )
    else:
        return output_dir

def setup_data_dir(data_dir: str):
    data_dir = get_output_dir(data_dir)
    os.makedirs(data_dir, exist_ok=True)
    return data_dir

def extract_tar_gz(tar_gz_file:str, output_dir:str, new_name:str):
    # Extract the .pdb file with renaming
    with tarfile.open(tar_gz_file, 'r:gz') as tar:
        for member in tar.getmembers():
            if os.path.splitext(member.name)[1] == '.pdb':
                member.name = new_name
                tar.extract(member, path=output_dir)
                break  # Only rename and extract the first .pdb file

trajectory_extensions = ('.dcd', '.xtc')