import requests
from PIL import Image
from io import BytesIO
from pathlib import Path
from utils import VIDEO_WIDTH, VIDEO_HEIGHT, ASSETS_PATH
from text_generation import generate_outlined_text

FILE_TYPE = ".png"
TEMP_FOLDER = "temp_imgs"

WHITE = (255,255,255)
RED = (255, 0, 0)
BLACK = (0,0,0)

def get_resized_image(url: str) -> Image:
    """
    Resize image to Youtube Shorts size
    :param url: URL of the image
    :returns: Pillow image
    """
    image_data = requests.get(url).content
    img = Image.open(BytesIO(image_data))
    
    ratio = VIDEO_HEIGHT / img.height
    
    return img.resize((int(img.width * ratio), VIDEO_HEIGHT))

def get_overlay(tp_name: str, name_size: int, tp_creator: str, creator_size: int) -> Image:
    """
    Creates an overlay image, the image will be overlayed on top of the video
    :param tp_name: texturepack name
    :param name_size: font size of texturepack name
    :param tp_creator: texturepack's creator
    :param creator_size: font size of texturepack's creator    
    :returns: Pillow image
    """

    tp_name_text = generate_outlined_text(-1,150, tp_name,(VIDEO_WIDTH, VIDEO_HEIGHT),name_size, RED, BLACK, 11)
    tp_creator_text = generate_outlined_text(-1,150, f"<BR><BR>Texture Pack by &(#ff0000){tp_creator}",(VIDEO_WIDTH, VIDEO_HEIGHT),creator_size,WHITE,BLACK,8)
    watermark = Image.open(Path(ASSETS_PATH) / "watermark" / "watermark.png")

    tp_name_text.paste(tp_creator_text, (0,0), tp_creator_text)
    tp_name_text.paste(watermark, (0,0), watermark)

    return tp_name_text


