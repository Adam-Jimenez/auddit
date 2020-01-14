# Auddit

Tired of those Reddit text-to-speech videos on Youtube? Now you can make your own!

## How it works

Using the [Reddit API](https://www.reddit.com/dev/api), more specifically the [Python Wrapper for the api](https://github.com/praw-dev/praw), we can query for hot posts from any subreddit. We then list a configurable amount of comments and replies and put all this data in a Post object. 

Then we pipe the text to the text-to-speech task, that generates an audio file using the Google Text-To-Speech API, more specifically the [Python Wrapper](https://gtts.readthedocs.io/en/latest/index.html).


