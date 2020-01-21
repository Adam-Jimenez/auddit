import praw
import os
from praw.models import MoreComments
from .post import Post, Comment

client_id = os.environ["REDDIT_CLIENT_ID"]
client_secret = os.environ["REDDIT_CLIENT_SECRET"]

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent='auddit-dev v1.0.0 by /u/adamj0')


def get_hottest_post(context):
   subreddit_name=context["subreddit"]
   comment_limit=context["comment_limit"]
   nsfw=context["nsfw"]
   subreddit = reddit.subreddit(subreddit_name)
   hot_posts = subreddit.hot()
   for post in hot_posts:
      if not post.stickied and post.over_18 == nsfw:
         title = post.title
         if len(title) >= 100:
            continue # respect youtube limit of 100
         comments = []
         for comment in post.comments:
            if isinstance(comment, MoreComments):
               continue
            if comment.stickied:
               continue
            comment_body = comment.body
            if comment_body == "[removed]":
               continue
            comment_reply = ""
            comment.replies.replace_more(limit=1)
            if len(comment.replies) > 0:
               reply = comment.replies[0]
               if isinstance(reply, MoreComments):
                  continue
               comment_reply = reply.body
            comment_output = Comment(comment_body, comment_reply)
            comments.append(comment_output)
            if len(comments) >= comment_limit:
               break
         
         post_data = Post(title, comments)
         post_data.score = post.score
         post_data.num_comments = post.num_comments
         context["post"] = post_data
         return

if __name__ == '__main__':
   get_hottest_post()
