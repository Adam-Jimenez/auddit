import subprocess

def upload_video(context):
    post = context["post"]
    subreddit = context["subreddit"]
    video_path = context["video_path"]
    title = post.title
    title = title + f" (/r/{subreddit})"

    args = ("./bin/youtubeuploader_linux_amd64", "-filename", video_path, "-title", title, "-description", title, "-privacy", "public")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print(output)

