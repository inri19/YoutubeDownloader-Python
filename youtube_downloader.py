from pytube import YouTube
from colorama import init, Fore

def on_complete(stream, filepath):
    print("Download Complete")
    print(filepath)

def on_progress(stream, chunk, bytes_remaining):
    progress_str = f"{round(100 - (bytes_remaining / stream.filesize) * 100,2)}%"
    print(progress_str)

init()
link = input("Youtube Link : ")
video_object = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

# Information
print(Fore.CYAN + f"\nTitle : \033[39m {video_object.title}")
print(Fore.CYAN + f"Lenght :  \033[39m {round(video_object.length / 60,2)} minutes")
print(Fore.CYAN + f"Views :   \033[39m {video_object.views}")
print(Fore.CYAN + f"Author :  \033[39m {video_object.author}")

# Telechargement
print(Fore.RED + "Download :" + Fore.GREEN + "(b)est \033[39m| " + Fore.YELLOW + "(w)orst \033[39m| " + Fore.BLUE + "(a)udio \033[39m| (e)xit ")
download_choice = input("Choice : ")

match download_choice :
    case "b" :
        video_object.streams.get_highest_resolution().download(r"C:\Users\ASUS ROG GL703VM\Downloads")
    case "w" :
        video_object.streams.get_lowest_resolution().download(r"C:\Users\ASUS ROG GL703VM\Downloads")
    case "a" :
        video_object.streams.get_audio_only().download(r"C:\Users\ASUS ROG GL703VM\Downloads")
    case "e" :
        exit()