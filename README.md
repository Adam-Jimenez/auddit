# Auddit

Tired of those Reddit text-to-speech videos on Youtube? Now you can make your own, automatically!

## Dependencies

- Python 3
- Everything in the requirements.txt file
- https://github.com/porjo/youtubeuploader

## Setup

`sudo pip install -r requirements.txt`

Then add the following environnement variables:

- REDDIT_CLIENT_ID
- REDDIT_CLIENT_SECRET

(Read about how to create a Reddit application to get those).

You also need to register an application on the Google OAuthv2 API. [Here's](https://developers.google.com/youtube/v3/guides/uploading_a_video) a guide.

## Running

`python src/main.py`

## How it works

Using the [Reddit API](https://www.reddit.com/dev/api), more specifically the [Python Wrapper for the api](https://github.com/praw-dev/praw), we can query for hot posts from any subreddit. We then list a configurable amount of comments and replies and put all this data in a Post object. 

Then we pipe the text to the text-to-speech task, that generates an audio file using the Google Text-To-Speech API, more specifically the [gTTS Python Wrapper](https://gtts.readthedocs.io/en/latest/index.html). 

Then, we send the text and the audio to the video generation tasks, which uses [PyMovie](https://zulko.github.io/moviepy/) to make a video with background music, the text-to-speech clips and the text.

All that is left is to [upload to Youtube using the Google API](https://github.com/porjo/youtubeuploader).

## TODO

- Try to use https://ttsmp3.com/ for the text-to-speech, the voice sounds nice.
- Setup a cron job to upload every day

## Why

idk
