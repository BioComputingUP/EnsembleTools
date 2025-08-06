import sys
import logging

# Create a logger.
logger = logging.getLogger("dpet")

def set_verbosity(level: str, stream: str = None):
    """Allows to change the verbosity of IDPET."""
    if stream is not None and stream not in ("err", "out"):
        raise ValueError(stream)
    logger.setLevel(getattr(logging, level))
    # Add a console handler.
    if logger.hasHandlers():
        logger.handlers.clear()
    if stream is None or stream == "err":
        ch = logging.StreamHandler()
    elif stream == "out":
        ch = logging.StreamHandler(sys.stdout)
    else:
        raise ValueError(stream)
    ch.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(ch)

# Default verbosity.
set_verbosity("WARN")