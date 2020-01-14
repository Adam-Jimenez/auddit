import textwrap
import uuid
from moviepy.editor import *

TITLE_FONT_SIZE = 30
FONT_SIZE = 30
TITLE_FONT_COLOR = 'white'
BGM_PATH = 'assets/bgm.mp3'
SIZE = (1280, 720)
BG_COLOR = (16,16,16)

def generate_clip(text, audio_path, title=False):
    color_clip = ColorClip(SIZE, BG_COLOR)
    audio_clip = AudioFileClip(audio_path)
    font_size = TITLE_FONT_SIZE if title else FONT_SIZE
    wrapped_text = textwrap.fill(text, width=90)
    txt_clip = TextClip(wrapped_text,fontsize=font_size, font='Amiri-regular', color=TITLE_FONT_COLOR, align="west")
    if title:
        txt_clip = txt_clip.set_pos("center")
    else:
        txt_clip = txt_clip.set_pos((20, "center"))
    clip = CompositeVideoClip([color_clip, txt_clip])
    clip.audio = audio_clip
    clip.duration = audio_clip.duration
    return clip

def generate_video(context):
    post = context["post"]
    clips = []
    clips.append(generate_clip(post.title, post.title_audio, title=True))
    for comment in post.comments:
        comment_clip = generate_clip(comment.body, comment.body_audio)
        # overlay reply
        if comment.reply:
            # TODO this
            pass
        clips.append(comment_clip)
    video = concatenate_videoclips(clips)
    background_audio_clip = AudioFileClip(BGM_PATH)
    background_audio_clip = background_audio_clip.set_end(video.duration)
    background_audio_clip = background_audio_clip.fx(afx.volumex, 0.15)
    video.audio = CompositeAudioClip([video.audio, background_audio_clip])
    path = f"video_data/{uuid.uuid4()}.mp4"
    video.write_videofile(path, fps=24, codec='libx264', threads=4)

