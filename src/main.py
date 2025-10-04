from config_loader import load_config
from pmc_parse import scrape_texturepack
from summarize import get_response
from pathlib import Path
from video_generation import make_video
from utils import ASSETS_PATH, remove_whitespaces, remove_all_mp4

CONFIG_FILE_PATH = Path("config.toml")

if __name__ == "__main__":
    config = load_config(CONFIG_FILE_PATH)

    # NOT USED FOR NOW:
    #ai_model = config["Ollama"]["model"]

    video_time = config["Output"]["video_time"]
    injected_text = config["Ollama"]["injected_text"]
    output_path = Path(config["Output"]["directory"])

    url = input("Enter PMC Texturepack url: ")

    pack_name = input("Enter pack name: ")

    Pmc_data = scrape_texturepack(url)

    with open(output_path / "comment.txt", "w") as file:
        file.write(config["Output"]["comment_start"]+url)

    file_name = f"{remove_whitespaces(pack_name)}.mp4"

    # Will remove previously generated videos
    remove_all_mp4(output_path)

    make_video(pack_name,Pmc_data["username"] ,Pmc_data["pictures"],video_time,Path(ASSETS_PATH) / "music" / "music.mp3", output_path / f"{file_name}")
    
    
