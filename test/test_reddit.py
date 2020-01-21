# Python code to demonstrate working of unittest 
import unittest 
from src.tasks.scrape_reddit.task import get_hottest_post
  
class TestReddit(unittest.TestCase): 
      
    def setUp(self): 
        pass
  
    def test_normal(self): 
        ctx = {
            "subreddit": "askreddit",
            "nsfw": True,
            "comment_limit": 3
        }
        get_hottest_post(ctx)
        print(ctx["post"].title)
  
if __name__ == '__main__': 
    unittest.main() 
