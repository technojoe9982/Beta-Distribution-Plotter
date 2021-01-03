import PySimpleGUI as sg

'''
this python file is for another pop out window which shows the maths of
how the cumulative probability  function works
'''

def explanation2():
    layout1 = [
        [sg.Image(filename = 'betacdf.PNG')]


    ]

    window3 = sg.Window('Probability Densities', layout1)


    while True:
        event, values = window3.read()



        if event in (sg.WIN_CLOSED, 'Cancel'):
            #event for closing window
            break


        window3.close()
