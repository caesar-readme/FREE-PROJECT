# PIP INSTALL colorama pytube pytfiglet

from colorama import Style, Fore
from pytube import Playlist, YouTube
import pyfiglet
import time
import os



def displayTerminal():
    print(Fore.RED + pyfiglet.figlet_format('YT Downloader', font='small') + Style.RESET_ALL)
    print(f'{Fore.RED}🎥{Style.RESET_ALL}{Fore.GREEN} Tools Youtube Downloader{Style.RESET_ALL}')
    print(f'{Fore.RED}   Version:{Style.RESET_ALL}{Fore.GREEN} 1.0{Style.RESET_ALL}')
    print(f'{Fore.RED}   Author:{Style.RESET_ALL}{Fore.GREEN} https://www.instagram.com/caesarr_id/{Style.RESET_ALL}')
    print()

class YoutubeDownloader:
    def __init__(self, url):
        self.url = url

    def YPlaylist(self, queryRES):
        os.system('cls' if os.name == 'nt' else 'clear')
        displayTerminal()
        p = Playlist(self.url)
        print('Please Wait Starting Downloading...')
        for video in p.videos:
            x = video.streams.filter(mime_type="video/mp4", res=queryRES, type="video").first()
            print(f'Downloading Video: {Fore.GREEN}{video.title}{Style.RESET_ALL}')
            
            if x:
                path = r'C:\Users\Babang\Videos'  # Ubah lokasi download sesuai kebutuhan
                x.download(path)
                print(f'{Fore.GREEN}Download Successful ~{Style.RESET_ALL}')

    def singleDownload(self, queryRES):
        os.system('cls' if os.name == 'nt' else 'clear')
        displayTerminal()
        
        s = YouTube(self.url)
        print('Please Wait Starting Downloading...')

        streams = s.streams.filter(progressive=True,res=queryRES,file_extension='mp4')
        for stream in streams:
            path = r'C:\Users\Babang\Videos'  # Ubah lokasi download sesuai kebutuhan
            stream.download(path)
            print(f'{Fore.GREEN}Download Successful ~{Style.RESET_ALL}')




    def SolutionChoice(self, query):
        if query == '1':
            self.YPlaylist("1080p") or self.singleDownload("1080p")

        elif query == '2':
            self.YPlaylist("720p") or self.singleDownload("720p")

        elif query == '3':
            self.YPlaylist("480p") or self.singleDownload("480p")

        else:
            print(f'{Fore.RED}Resolution Choice Error{Style.RESET_ALL}')

displayTerminal()

def Term():
    time.sleep(0.5)
    print(f'{Fore.GREEN}--- Resolution Choice ---{Style.RESET_ALL}')
    print(f'{Fore.GREEN}🔑 1. 1080p{Style.RESET_ALL}')
    print(f'{Fore.GREEN}🔑 2. 720p{Style.RESET_ALL}')
    print(f'{Fore.GREEN}🔑 3. 480p{Style.RESET_ALL}')


print('-- Choices --')
print('1. Playlist Video Download')
print(f'2. Single Video Download -> {Fore.YELLOW} Sedang Maitance {Style.RESET_ALL}')
choice = input('Choose (1/2): ')

if choice == '1':
    url = input('Enter Playlist URL: ')
    Term()
    yt = YoutubeDownloader(url)
    
    while True:
        reso = input('Choose option (1/2/3): ')
        
        if reso in ['1', '2', '3']:
            yt.SolutionChoice(reso)
            break
        else:
            print(f'{Fore.RED}Invalid Resolution Choice!{Style.RESET_ALL}')
elif choice == '2':
    print(f'2. Single Video Download -> {Fore.YELLOW} Sedang Maitance {Style.RESET_ALL}')
    # url = input('Enter Single URL: ')
    # Term()
    # yt = YoutubeDownloader(url)
    
    # while True:
    #     reso = input('Choose option (1/2/3): ')
        
    #     if reso in ['1', '2', '3']:
    #         yt.SolutionChoice(reso)
    #         break
    #     else:
    #         print(f'{Fore.RED}Invalid Resolution Choice!{Style.RESET_ALL}')
else:
    print(f'{Fore.RED}Invalid Choice{Style.RESET_ALL}')
