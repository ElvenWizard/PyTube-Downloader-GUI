import PySimpleGUI as psg
from pytube import YouTube as y

class YToob:
    def __init__(self):
        self.GUI = GUI()
        self.l_v = self.GUI.link
        self.yt = y(self.l_v,)
        self.ttl = self.yt.title
        self.aut = self.yt.author
        self.leng = self.yt.length

    
    def Down():
        y.download("\Youtube Output",None,"ZZ-Downloader",True,15,3)


class GUI:

    
    def __init__(self,link):
        self.link = link

    def WelcomeScreen():
        psg.theme('Dark Red 1')
        layout = [[psg.Text("Welcome to the GUITube Downloader!")], [psg.Button('OK')]]
        window = psg.Window('WELCOME!', layout)
        
        while True:
            event = window.read()
            if event == 'OK' or event == psg.WIN_CLOSED:
                break
        window.close()
                

    def getlink(self):
        psg.theme('Dark Red 1')
        layout = [[psg.Text('Please paste the link to the video below:')],
                [psg.InputText()], 
                [psg.Button('OK')]
                ]
        window = psg.Window('Insert Video', layout)
        
        while True:
            event, values = window.read()
            if event == psg.WIN_CLOSED:
                window.close()
                break
            elif event == 'OK':
                self.link = values[0]
                print(f'Link entered: {self.link}')
                break

    def dwnldinterf():
        psg.theme('Dark Red 1')
        layout = [[psg.Text('Title:'), psg.Text('Length of Video:'), psg.Text('Author:')],
                  [psg.Text(YToob.ttl), psg.Text(YToob.leng), psg.Text(YToob.aut)],
                  [psg.Button('Download')]]
        window = psg.Window('Downloader', layout)

        while True:
            event = window.read()
            if event == 'Download':
                YToob.Down()
            else:
                break

    """def quit():
        psg.theme('Dark Red 1')
        layout = [[psg.Text('Are you sure you want to quit?')],
                  [psg.Button('Yes'), psg.Button('No')]]
        window = psg.Window('Quit?', layout)

        while True:
            event, values = window.read()
            if event.window == 'Yes':
                window.close_destroys_window(True)
            else:
                window.close()"""
def main():
    GUI.WelcomeScreen()
    GUI.getlink()
    GUI.dwnldinterf()
main()
    