import tamagotchi.animal as animal
import PySimpleGUI as sg
# to implement: 
# decreasing parameters with time
# memorizing objects after exit
# visualize in PySimpleGUI
# add a mini-game to entartain your pet (beat mouse/cats in 9 cells)

def global_exit():
    pass

def create_pet():

    layout = [[sg.Text('Choose a pet:')],
          [sg.Button('Cat'), sg.Button('Dog')]]

    window = sg.Window('Tamagotchi', layout)
    ev, values = window.read()
    if ev == sg.WIN_CLOSED:
        global_exit()
    #print(ev, values)
    window.close()
    layout = [[sg.Text('Write down a name:')],
          [sg.Input(key='-IN-'), sg.Button('Submit the name')]]

    window = sg.Window('Tamagotchi', layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        global_exit()
    #print(event, values)
    if event == 'Submit the name':
        window.close()
        if ev == 'Cat':
            return animal.Cat(values['-IN-'])
        if ev == 'Dog':
            return animal.Dog(values['-IN-'])


def run_mini_game():
    pass

def run(pet):
    layout = [[sg.Text('here will be your drawn pet {} soon'.format(pet.name))],
          [sg.Input(key='-IN-')],
          [sg.Button('Feed'), sg.Button('Play mini-game'), sg.Button('Go to the toilet'), sg.Exit()]]

    window = sg.Window('Tamagotchi', layout)

    while True:    # The Event Loop
        event, values = window.read()
        #print(event, values)       
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Feed':
            pass
        if event == 'Play mini-game':
            pass
        if event == 'Go to the toilet':
            pass
    window.close()

def main():
    pet = create_pet()
    run(pet)

if __name__ == '__main__':
    main()