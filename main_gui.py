import PySimpleGUI as sg

sg.theme('Blue')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Combo(["Augspurger", "Biddle Butte RS", "Butler Grade Level 1", "Butler Grade Level 2", "Butler Grade Level 3",
                      "Forest Grove", "Goodnoe Hills Level 1", "Goodnoe Hills Level 2", "Hood River", "Horse Heaven",
                      "Kennewick Level 1", "Kennewick Level 2", "Mary's Peak RS", "Megler RS", "Mt Hebo RS", "Naselle RS",
                      "Roosevelt RS", "Seven Mile Hill Level 1", "Seven Mile Hill Level 2", "Shaniko RS", "Sunnyside RS",
                      "Tillamook", "Troutdale", "Wasco"], default_value="Station")],
            [sg.Combo(["2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010"], default_value="Year")],
            [sg.Combo(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"], default_value="Month")],
          [sg.Button('Search')]]



# Create the Window
window = sg.Window('Window Title', layout, size=(500,500))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()