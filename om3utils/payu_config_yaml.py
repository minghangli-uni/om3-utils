"""NUOPC configuration"""

from pathlib import Path
from ruamel.yaml import YAML, CommentedMap


def read_payu_config_yaml(file_name: str) -> CommentedMap:
    """Read a payu config file.

    :param file_name: File name.
    """
    fname = Path(file_name)
    if not fname.is_file():
        raise FileNotFoundError(f"File not found: {fname.as_posix()}")

    config = YAML().load(fname)

    return config


def write_payu_config_yaml(config: [dict | CommentedMap], file: Path):
    """Write a NUOPC config dictionary as a Resource File.

    :param config: Dictionary holding the payu config file to write
    :param file: File to write to.
    """

    YAML().dump(config, file)
