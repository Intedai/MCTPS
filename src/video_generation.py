from moviepy import ImageClip, AudioFileClip, CompositeVideoClip, concatenate_videoclips
from moviepy.audio.fx import AudioLoop
from pathlib import Path
from utils import VIDEO_WIDTH, VIDEO_HEIGHT
from images import get_resized_image, get_overlay

def image_to_animated_video_clip(path: Path, duration: float) -> CompositeVideoClip:
    """
    Turns an image to a "Sliding" video
    :param path: path of the image
    :param duration: lenght of the clip 
    :returns: Animated video clip
    """

    clip = ImageClip(str(path)).with_duration(duration)
    
    image_width = clip.size[0]

    def position(t):
        max_shift = image_width - VIDEO_WIDTH
        x = -max_shift * (t / duration)
        return (x, 0)

    clip = clip.with_position(position)

    final_clip = CompositeVideoClip([clip], size=(VIDEO_WIDTH, VIDEO_HEIGHT), bg_color=(0, 0, 0))

    return final_clip

def make_video(tp_name, tp_creator, pics: list, video_time:float, mp3_path: Path, output: Path) -> None:
    """
    Turns a list of pics into the final video
    :param tp_name: creator name
    :param pics: list of pics
    :param video_time: duration of vid
    :param mp3_path: path of the music
    :param output: path of the final vid
    """

    video_clips = []
    audio = AudioFileClip(mp3_path)

    if audio.duration > video_time:
        audio = audio.with_duration(video_time)
    elif audio.duration < video_time:
        audio = audio.with_effects([AudioLoop(duration=video_time)])

    duration = video_time / len(pics)

    temp = Path("temp.png")

    for pic in pics:
        get_resized_image(pic).save(temp)
        #print(get_response(ai_model, injected_text, Pmc_data["description"]))

        video_clips.append(image_to_animated_video_clip(temp, duration=duration))
    
    # Remove temp file


    vid = concatenate_videoclips(video_clips).with_audio(audio)
    
    get_overlay(tp_name, 80, tp_creator, 60).save(temp)

    overlay = ImageClip(temp, duration=video_time)

    final_vid = CompositeVideoClip([vid, overlay])

    if temp.is_file():
        temp.unlink()

    final_vid.write_videofile(output, fps=30)

