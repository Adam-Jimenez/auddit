from PIL import Image, ImageDraw, ImageFont
from textwrap import fill

THUMBNAIL_DIR = "data/thumbnails/"
THUMBNAIL_DIMENSION = (640, 360)
CLICKBAIT_GIRL = Image.open('./assets/clickbait.png')
CLICKBAIT_GIRL.thumbnail((THUMBNAIL_DIMENSION[0]/2, THUMBNAIL_DIMENSION[1]/2), Image.ANTIALIAS) # aspect ratio resize to fit thumbnail
GOLD = Image.open("./assets/gold_32.png")
PLATINUM = Image.open("./assets/platinum_32.png")
FORK_ME = Image.open("./assets/forkme.png")
CENSORED = Image.open("./assets/censored.png")
UPVOTE = Image.open("./assets/upvote.png").convert("RGBA")
COMMENT = Image.open("./assets/comment.png").convert("RGBA")
CENSORED.thumbnail((THUMBNAIL_DIMENSION[0]/2, THUMBNAIL_DIMENSION[1]/2), Image.ANTIALIAS) # aspect ratio resize to fit thumbnail

def generate_thumbnail(context):
    subreddit = context["subreddit"].capitalize() 
    post = context["post"]
    score = str(post.score)
    num_comments = str(post.num_comments)
    main_text = post.title
    main_text = fill(main_text, width=25)

    thumbnail = Image.new('RGB', THUMBNAIL_DIMENSION, color=(16,16,16))
    draw = ImageDraw.Draw(thumbnail)
    font = ImageFont.truetype('./assets/Copse-Regular.ttf', 40)
    font2 = ImageFont.truetype('./assets/Copse-Regular.ttf', 45)
    font3 = ImageFont.truetype('./assets/Copse-Regular.ttf', 30)

    # clickbait girl
    aw,ah = CLICKBAIT_GIRL.size
    girl_offset = (THUMBNAIL_DIMENSION[0]-aw,THUMBNAIL_DIMENSION[1]-ah)
    thumbnail.paste(CLICKBAIT_GIRL, girl_offset, CLICKBAIT_GIRL)

    # subreddit 
    title_width, title_height = font.getsize(subreddit)
    title_offset = (20,20)
    draw.text(title_offset, subreddit, font=font, fill=(255,255,255))

    # gilds
    gold_offset = (title_offset[0] + title_width + 20, title_offset[1] + 10)
    platinum_offset = (title_offset[0] + title_width + GOLD.size[0] + 26, title_offset[1] + 10)
    thumbnail.paste(GOLD, gold_offset, GOLD)
    thumbnail.paste(PLATINUM, platinum_offset, PLATINUM)

    # main text
    main_text_offset = (20, 70)
    draw.text(main_text_offset, main_text, font=font2, fill=(255,255,255))

    # fork me
    fw,fh = FORK_ME.size
    fork_offset = (THUMBNAIL_DIMENSION[0]-fw, 0)
    thumbnail.paste(FORK_ME, fork_offset, FORK_ME)

    # upvote
    uw, uh = UPVOTE.size
    upvote_offset = (20, THUMBNAIL_DIMENSION[1]-uh-20)
    thumbnail.paste(UPVOTE, upvote_offset, UPVOTE)

    upvote_count_offset = (upvote_offset[0]+uw+10, THUMBNAIL_DIMENSION[1]-uh-20)
    draw.text(upvote_count_offset, score, font=font3, fill=(128, 128, 128))
    score_width, score_height = font3.getsize(score)
    # comments
    cw, ch = COMMENT.size
    comment_offset = (upvote_count_offset[0]+score_width+20, THUMBNAIL_DIMENSION[1]-ch-20)
    thumbnail.paste(COMMENT, comment_offset, COMMENT)

    comment_count_offset = (comment_offset[0]+cw+10, THUMBNAIL_DIMENSION[1]-ch-20)
    draw.text(comment_count_offset, num_comments, font=font3, fill=(128, 128, 128))

    video_id = context["video_id"]
    thumbnail_path = f"{THUMBNAIL_DIR}{video_id}.png"
    thumbnail.save(thumbnail_path)
    context["thumbnail_path"] = thumbnail_path
