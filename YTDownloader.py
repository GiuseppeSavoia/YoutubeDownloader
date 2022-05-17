# importing YouTube from pytube module
from pytube import YouTube


def download():
    # assign video link to a variable
    video_link = input("Paste the url of the Youtube video -> ")

    # assign path to a variable
    directory = input("Paste the path of the directory -> ")

    # passing that link variable to YouTube function
    video = YouTube(video_link)

    # downloading video,res to regulate the quality of the video
    video.streams.filter(res='1080p').first().download(directory)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    download()
