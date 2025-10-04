from pathlib import Path

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
ASSETS_PATH = "Assets"

def remove_whitespaces(text: str) -> str:
    """
    Replaces whitespaces with '_'
    :param text: Text to replace whitespaces
    :returns: new text
    """

    INSTEAD_OF_SPACE = '_'
    return INSTEAD_OF_SPACE.join(text.split())

def remove_all_mp4(directory: Path) -> None:
    """
    Remove every .mp4 in the given directory
    :param directory: path of dir
    """

    for mp4 in directory.iterdir():
        if mp4.suffix.lower() == ".mp4" and mp4.is_file():
            mp4.unlink()
