import uuid
import requests
from gtts import gTTS

def save_tts(text):
   form_data = {
         "msg": text,
         "lang": "Matthew",
         "source": "ttsmp3"
   }
   json = requests.post("https://ttsmp3.com/makemp3_new.php", form_data).json()
   url = json["URL"]
   filename = json["MP3"]
   mp3_file = requests.get(url)
   path = f"audio_data/{filename}"
   open(path, "wb").write(mp3_file.content)
   return path

def save_gtts(text):
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

if __name__ == "__main__":
   save_tts("i am a potato")
