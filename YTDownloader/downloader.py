from pytube import YouTube


# Ask the user to input the YouTube URL
url = input("Enter the YouTube URL: ")

yt = YouTube(url)

print("Title:", yt.title)
print("Views:", yt.views)

print("Downloading...")
# Get the highest resolution stream
yd = yt.streams.get_highest_resolution()

# Download the video to the current directory
yd.download('C:/Users/perim/Videos/Video_downloads')

print("Download complete.")
