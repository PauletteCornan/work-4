import PySimpleGUI as sg
import pyttsx3

ENGINE_VARIABLE_SO_REPLACE = pyttsx3.init()
VOICE_VARIABLE_SO_REPLACE = ENGINE_VARIABLE_SO_REPLACE.getProperty('voices')



layout = [    [sg.Text('Select the type of voice:',text_color='white',background_color='black'),sg.Radio('Male', 'RADIO1', default=True, key='male',background_color='red'),sg.Radio('Female', 'RADIO1', key='female',background_color='red')],
     [sg.Text('Enter text to speak:',text_color='white',background_color='blue',)],
          
    [sg.InputText(key='input'),sg.Button('Speak',button_color='orange')],
   
    
]

window = sg.Window('TEXT TO SPEECH', layout,background_color='blue')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['input']
        if values['male']:
            ENGINE_VARIABLE_SO_REPLACE.setProperty('voice', VOICE_VARIABLE_SO_REPLACE[0].id)
        elif values['female']:
           ENGINE_VARIABLE_SO_REPLACE.setProperty('voice', VOICE_VARIABLE_SO_REPLACE[1].id) 
    
        ENGINE_VARIABLE_SO_REPLACE.say(text)
        ENGINE_VARIABLE_SO_REPLACE.runAndWait()

window.close()