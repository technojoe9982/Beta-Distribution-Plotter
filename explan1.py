import PySimpleGUI as sg

'''
this python file is for a second pop out window which shows the maths of
how the probability density function works
'''

def explanation1():
    layout1 = [
        [sg.Image(filename = 'betapdf.PNG')]


    ]

    window2 = sg.Window('Probability Densities', layout1)


    while True:
        event, values = window2.read()



        if event in (sg.WIN_CLOSED, 'Cancel'):
            #event for closing window
            break


        window2.close()
