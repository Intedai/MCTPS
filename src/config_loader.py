import tomllib
from pathlib import Path

def load_config(path: Path) -> dict:
    """
    Replaces whitespaces with '_'
    :param path: path of config.toml's dir
    :returns: config as a dict
    """    
    if not path.is_file():
        raise FileNotFoundError(f"Config file not found in '{path}'")
    with open(path, "rb") as file:
        return tomllib.load(file) # Will raise tomllib.TOMLDecodeError if bad TOML