from PIL import Image, ImageDraw, ImageFont
from textwrap import fill

THUMBNAIL_DIMENSION = (640, 360)
CLICKBAIT_GIRL = Image.open('./assets/clickbait.png')
CLICKBAIT_GIRL.thumbnail((THUMBNAIL_DIMENSION[0]/2, THUMBNAIL_DIMENSION[1]/2), Image.ANTIALIAS) # aspect ratio resize to fit thumbnail
GOLD = Image.open("./assets/gold_32.png")
PLATINUM = Image.open("./assets/platinum_32.png")
FORK_ME = Image.open("./assets/forkme.png")
CENSORED = Image.open("./assets/censored.png")
CENSORED.thumbnail((THUMBNAIL_DIMENSION[0]/2, THUMBNAIL_DIMENSION[1]/2), Image.ANTIALIAS) # aspect ratio resize to fit thumbnail

def generate_thumbnail(context):
    subreddit = context["subreddit"].capitalize() 
    main_text = context["post"].title
    main_text = fill(main_text, width=40)

    thumbnail = Image.new('RGB', THUMBNAIL_DIMENSION, color=(16,16,16))
    draw = ImageDraw.Draw(thumbnail)
    font = ImageFont.truetype('./assets/Copse-Regular.ttf', 40)
    font2 = ImageFont.truetype('./assets/Copse-Regular.ttf', 30)

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
    main_text_offset = (20, 80)
    draw.text(main_text_offset, main_text, font=font2, fill=(255,255,255))

    # fork me
    fw,fh = FORK_ME.size
    fork_offset = (THUMBNAIL_DIMENSION[0]-fw, 0)
    thumbnail.paste(FORK_ME, fork_offset, FORK_ME)

    # censored
    cw, ch = CENSORED.size
    censored_offset = (80, THUMBNAIL_DIMENSION[1]-ch-10)
    thumbnail.paste(CENSORED, censored_offset, CENSORED)

    # clickbait girl
    aw,ah = CLICKBAIT_GIRL.size
    girl_offset = (THUMBNAIL_DIMENSION[0]-aw,THUMBNAIL_DIMENSION[1]-ah)
    thumbnail.paste(CLICKBAIT_GIRL, girl_offset, CLICKBAIT_GIRL)

    video_id = context["video_id"]
    thumbnail_path = f"./thumbnails/{video_id}.png"
    thumbnail.save(thumbnail_path)
    context["thumbnail_path"] = thumbnail_path
