from pytube import YouTube


link = input("masukan link :")
yt = YouTube(link)

print("judul :",yt.title)
ys = yt.streams.get_highest_resolution()
print("Downloading...")
ys.download()
print("succes download", yt.title)

