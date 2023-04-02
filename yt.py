from pytube import YouTube
link = str(input("paste link: "))

video = YouTube(url=link)

qualities = video.streams.all()

vid = list(enumerate(qualities))
for quality in vid:
    print(quality)

print()

choice = int(input("Enter quality you want to download:"))

qualities[choice].download()
print("✔️Downloaded successfully")