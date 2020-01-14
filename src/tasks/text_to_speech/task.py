import uuid
from gtts import gTTS

def save_tts(text):
   tts = gTTS(text=text, lang='en')
   path = f"audio_data/{uuid.uuid4()}.mp3"
   tts.save(path)
   return path

def tts(context):
   post = context["post"]
   post.title_audio = save_tts(post.title)
   for comment in post.comments:
      comment.body_audio = save_tts(comment.body)
      if comment.reply:
         comment.reply_audio = save_tts(comment.reply)
   return
