import FreeSimpleGUI as psg
from pytubefix import YouTube as y
from pathlib import Path as p

class Downloader:
    def __init__(self):
        self.link = ""
        self.yt = None
        self.ttl = ""
        self.aut = ""
        self.leng = ""

    def down(self):
        self.yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=str(p.home() / 'Downloads'))
        print('Downloaded!')
        confirm = psg.popup_yes_no('Downloaded! Saved to downloads folder. Do you want to download another video?')
        if confirm == 'Yes':
            self.main()
        else:
            exit()
        

    def welcome_screen(self):
        psg.theme('Dark Red 1')
        layout = [[psg.Text("Welcome to the GUITube Downloader!")], [psg.Button('OK')]]
        window = psg.Window('WELCOME!', layout)

        while True:
            event, values = window.read()
            print(values)
            if event == 'OK':
                window.close()
                break
            elif event == psg.WINDOW_CLOSED:
                window.close()
                exit()

    def get_link(self):
        psg.theme('Dark Red 1')
        layout = [[psg.Text('Please paste the link to the video below:')],
                  [psg.InputText()],
                  [psg.Button('OK')]
                  ]
        window = psg.Window('Insert Video', layout)

        while True:
            event, values = window.read()
            if event == psg.WINDOW_CLOSED:
                window.close()
                exit()
            elif event == 'OK':
                self.link = values[0]
                print(f'Link entered: {self.link}')
                break
        window.close()

    def download_interface(self):
        psg.theme('Dark Red 1')
        layout = [[psg.Text('Title:'), psg.Text('Length of Video:'), psg.Text('Author:')],
                  [psg.Text(self.ttl), psg.Text(str(self.leng)), psg.Text(self.aut)],
                  [psg.Button('Download')]]
        window = psg.Window('Downloader', layout)

        while True:
            event, _ = window.read()
            if event == 'Download':
                self.down()
            else:
                window.close()
                exit()
    
    def main(self):
        self.welcome_screen()
        self.get_link()
        self.yt = y(self.link)
        self.ttl = self.yt.title
        self.aut = self.yt.author
        self.leng = self.yt.length
        self.download_interface()


if __name__ == '__main__':
    downloader = Downloader()
    downloader.main()
