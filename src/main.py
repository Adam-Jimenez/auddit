from tasks.scrape_reddit.task import get_hottest_post
from tasks.text_to_speech.task import tts
from tasks.generate_video.task import generate_video
from tasks.upload_video.task import upload_video

class Pipeline:
    def __init__(self):
        self.tasks = [
            get_hottest_post,
            tts,
            generate_video,
            upload_video
        ]
        self.context = dict()

    def execute(self, **kwargs):
        self.context = kwargs
        for task in self.tasks:
            print(f"Current Task: {task.__name__}")
            task(self.context)

if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.execute(subreddit='askreddit', nsfw=True, comment_limit=20)
