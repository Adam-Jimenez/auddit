# Python code to demonstrate working of unittest 
import unittest 
from src.tasks.generate_thumbnail.task import generate_thumbnail

class Post:
    pass
  
class TestThumbnail(unittest.TestCase): 
      
    def setUp(self): 
        pass
  
    def test_normal(self): 
        post = Post()
        post.title = "a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a "
        post.score = 42069
        post.num_comments = 42069
        ctx = {
            "subreddit": "askreddit",
            "post": post,
            "video_id": "test"
        }
        generate_thumbnail(ctx)
  
if __name__ == '__main__': 
    unittest.main() 
