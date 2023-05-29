import PySimpleGUI as psg

def welcomScreen():
    psg.theme('Dark Red 1')
    layout = [[psg.Text("Welcome to the GUITube Downloader!")], [psg.Button('OK')]]
    window = psg.Window('WELCOME!', layout)
    while True:
        event, values = window.read()
        if event == 'OK' or event == psg.WIN_CLOSED:
            break
    window.close() 

