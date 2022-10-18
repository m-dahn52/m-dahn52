#
# Drumpad Program Main
#
# Michael S. Dahn
#
# 09/15/22
#
#---------------------------------------------------------------------------------------------------------------------------
from msilib.schema import File
from xml.etree.ElementTree import TreeBuilder
import PySimpleGUI as sg      #windows and events
import numpy as np            #for arrays
import pygame
from pygame import mixer      #handles sample playback, multiple samples at once

pygame.mixer.init()
pygame.mixer.set_num_channels(9)  #9 channels, 1 for each sample in given window

#Sample Filess

#classic
cl_hi_tom = mixer.Sound(r'ExampleFilePath')   # r denotes raw string.
cl_mid_tom = mixer.Sound(r'ExampleFilePath')  
cl_lo_tom = mixer.Sound(r'ExampleFilePath')
cl_hat_cl = mixer.Sound(r'ExampleFilePath')
cl_hat_open = mixer.Sound(r'ExampleFilePath')
cl_ride = mixer.Sound(r'ExampleFilePath')
cl_kick = mixer.Sound(r'ExampleFilePath')
cl_snare = mixer.Sound(r'ExampleFilePath')
cl_cross = mixer.Sound(r'ExampleFilePath')

#brush
br_hi_tom = mixer.Sound(r'ExampleFilePath')
br_mid_tom = mixer.Sound(r'ExampleFilePath')
br_lo_tom = mixer.Sound(r'ExampleFilePath')
br_hat_cl = mixer.Sound(r'ExampleFilePath')
br_hat_open = mixer.Sound(r'ExampleFilePath')
br_ride = mixer.Sound(r'ExampleFilePath')
br_kick = mixer.Sound(r'ExampleFilePath')
br_snare = mixer.Sound(r'ExampleFilePath')
br_clave = mixer.Sound(r'ExampleFilePath')

#808 
electronic_hi_tom = mixer.Sound(r'ExampleFilePath')
electronic_mid_tom = mixer.Sound(r'ExampleFilePath')
electronic_lo_tom = mixer.Sound(r'ExampleFilePath')
electronic_hat_cl = mixer.Sound(r'ExampleFilePath')
electronic_hat_open = mixer.Sound(r'ExampleFilePath')
electronic_crash = mixer.Sound(r'ExampleFilePath')
electronic_kick = mixer.Sound(r'ExampleFilePath')
electronic_snare = mixer.Sound(r'ExampleFilePath')
electronic_rim = mixer.Sound(r'ExampleFilePath')



valid_keys = np.array(('q','w','e','a','s','d','z','x','c'))   #active keys corresponding to buttons in windows 2-4

#Menu Window
def menu_window():
    global win_ref
    win_ref = 1
    sg.theme('DarkGreen2')

    layout = [
        [sg.Text('Pick a Kit')],
        [
            sg.Button('Classic', key = '-MENUCLASSIC-'),
            sg.Button('Brush', key = '-MENUBRUSH-'),
            sg.Button('808 Kit', key = '-MENU808-'),
            sg.Button('<EMPTY>', key = '-USER_KIT-'),
            sg.Button('Import Files', key = '-BUILD-')
        ],
        [
            sg.Push(),
            sg.Button('Exit', key = '-EXIT-')
        ]
    ]
    return sg.Window('Menu', layout, resizable = False, return_keyboard_events= True)

#CLASSIC KIT WINDOW
def classic_window():                                   #TYPICAL: creates layouts for drumkit windows
    global win_ref
    win_ref = 2
    sg.theme('Topanga')

    layout = [
        [
            sg.Push(),
            sg.VSeparator(),
            sg.Text('Classic', text_color= '#00FF00'),
            sg.VSeparator(),
            sg.Text('Brush', text_color = '#FFFFFF'),
            sg.VSeparator(),
            sg.Text('808', text_color = '#FFFFFF')   
        ],
        [
            sg.Button('Conga Hi \nq', size = (10,5), key = '-C1-'),
            sg.Button('Conga Low \nw', size = (10,5), key = '-C2-'),
            sg.Button('Tom Low \ne', size = (10,5), key = '-C3-'),
        ],
        [ 
            sg.Button('Hat Close\na', size = (10,5), key = '-C4-'),
            sg.Button('Hat Open\ns', size = (10,5), key = '-C5-'),
            sg.Button('Ride\nd', size = (10,5), key = '-C6-')
        ],
        [ 
            sg.Button('Kick\nz', size = (10,5), key = '-C7-'),
            sg.Button('Snare\nx', size = (10,5), key = '-C8-'),
            sg.Button('Cross\nc', size = (10,5), key = '-C9-')
        ],
        [
            sg.Push(),
            sg.Button('RETURN', key = '-RETURN-'),
            sg.Button('Exit', key = '-EXIT-')
        ]
    ]
    return sg.Window('Classic',layout, resizable= False, return_keyboard_events= True)

def brush_window():
    global win_ref
    win_ref = 3
    sg.theme('Kayak')

    layout = [ 
        [
            sg.Push(),
            sg.VSeparator(),
            sg.Text('Classic', text_color= '#FFFFFF'),
            sg.VSeparator(),
            sg.Text('Brush', text_color = '#00FF00'),
            sg.VSeparator(),
            sg.Text('808', text_color = '#FFFFFF')   
        ],
        [
            sg.Button('Conga Hi \nq', size = (10,5), key = '-B1-'),
            sg.Button('Conga Low \nw', size = (10,5), key = '-B2-'),
            sg.Button('Tom Low \ne', size = (10,5), key = '-B3-'),
        ],
        [ 
            sg.Button('Hat Close\na', size = (10,5), key = '-B4-'),
            sg.Button('Hat Open\ns', size = (10,5), key = '-B5-'),
            sg.Button('Ride\nd', size = (10,5), key = '-B6-')
        ],
        [ 
            sg.Button('Kick\nz', size = (10,5), key = '-B7-'),
            sg.Button('Snare\nx', size = (10,5), key = '-B8-'),
            sg.Button('Cross\nc', size = (10,5), key = '-B9-')
        ],
        [
            sg.Push(),
            sg.Button('RETURN', key = '-RETURN-'),
            sg.Button('Exit', key = '-EXIT-')
        ]
    ]
    return sg.Window('Brush', layout, resizable = False,return_keyboard_events= True)

def elec_window():
    global win_ref
    win_ref = 4
    sg.theme('DarkBlue3')

    layout = [ 
        [
            sg.Push(),
            sg.VSeparator(),
            sg.Text('Classic', text_color= '#FFFFFF'),
            sg.VSeparator(),
            sg.Text('Brush', text_color = '#FFFFFF'),
            sg.VSeparator(),
            sg.Text('808', text_color = '#00FF00')   
        ],
        [
            sg.Button('Conga Hi \nq', size = (10,5), key = '-E1-'),
            sg.Button('Conga Low \nw', size = (10,5), key = '-E2-'),
            sg.Button('Tom Low \ne', size = (10,5), key = '-E3-'),
        ],
        [ 
            sg.Button('Hat Close\na', size = (10,5), key = '-E4-'),
            sg.Button('Hat Open\ns', size = (10,5), key = '-E5-'),
            sg.Button('Ride\nd', size = (10,5), key = '-E6-')
        ],
        [ 
            sg.Button('Kick\nz', size = (10,5), key = '-E7-'),
            sg.Button('Snare\nx', size = (10,5), key = '-E8-'),
            sg.Button('Cross\nc', size = (10,5), key = '-E9-')
        ],
        [
            sg.Push(),
            sg.Button('RETURN', key = '-RETURN-'),
            sg.Button('Exit', key = '-EXIT-')
        ]
    ]   
    return sg.Window('808', layout, resizable= False, return_keyboard_events= True)

menu_bar = [ 
    [ 
        '&File', ['&Open','&Save', 'Save As', 'Import Samples']
    ],
    [ 
        '&Edit', ['Rename_Button', 'Change_Theme']
    ]
]

def rename_prompt():
    layout = [ 
        [
            sg.Input('Enter New Button Name', key = '-NEW_NAME-'),
            sg.Input('Enter Button Number: (ex: 1-9)', key = '-WHICH_BUTTON-'),
            sg.Input('ENTER SAMPLE PATH', key = '-FILE_PATH-'),
            sg.Button('SET BUTTON', key = '-SET-')
        ],
        [ 
            sg.Button('Cancel', key = '-RETURN-')
        ]
    ]
    return sg.Window('BUTTON PROPERTIES', layout, resizable= False)

def user_samples(settings):  #load in from a .json file
    global win_ref
    win_ref = 5
    sg.theme('Kayak')

    layout = [ 
        [ 
            sg.Menu(menu_bar, key = '-MENU-')
        ],
        [
            
            sg.Push(),
            sg.VSeparator(),
            sg.Text('Classic', text_color= '#0000FF'),
            sg.VSeparator(),
            sg.Text('Brush', text_color = '#0000FF'),
            sg.VSeparator(),
            sg.Text('808', text_color = '#0000FF')   
        ],
        [
            sg.Button(settings_b1 +'\nq', size = (10,5), key  = '-U1-'),
            sg.Button(settings_b2+'\nw', size = (10,5), key = '-U2-'),
            sg.Button(settings_b3+'\ne', size = (10,5), key = '-U3-' ),
        ],
        [ 
            sg.Button(settings_b4+'\na', size = (10,5), key = '-U4-'),
            sg.Button(settings_b5+'\ns', size = (10,5), key = '-U5-'),
            sg.Button(settings_b6+'\nd', size = (10,5), key = '-U6-')
        ],
        [ 
            sg.Button(settings_b7+'\nz', size = (10,5), key = '-U7-'),
            sg.Button(settings_b8+'\nx', size = (10,5), key = '-U8-'),
            sg.Button(settings_b9+'\nc', size = (10,5), key = '-U9-', )
        ],
        [
            sg.Push(),
            
            sg.Button('RETURN', key = '-RETURN-'),
            sg.Button('Exit', key = '-EXIT-')
        ]
    ]
    return sg.Window("'"+ settings_title +"'", layout, resizable = False,return_keyboard_events= True)

def import_window():
    sg.theme('DarkTeal6')

    layout = [ 

        [ 
            sg.Text('Welcome To Kit Builder: Enter A kit Name'),
            sg.Input( '',key = '-KIT_TITTLE-')
        ],
        [ 
            sg.Text('1:'),
            sg.VSeparator(), 
            sg.Text('Name'),
            sg.Input('',key = '-BUTTN_1_NAME-'),
            sg.VSeparator(),
            sg.Text('Enter File Path'),
            sg.Input('', key = '-BUTTN_1_PATH-')

        ],
        [ 
            sg.Text('2:'),
            sg.VSeparator(), 
            sg.Text('Name'),
            sg.Input('',key = '-BUTTN_2_NAME-'),
            sg.VSeparator(),
            sg.Text('Enter File Path'),
            sg.Input('', key = '-BUTTN_2_PATH-')

        ],
        [ 
            sg.Text('3:'),
            sg.VSeparator(), 
            sg.Text('Name'),
            sg.Input('',key = '-BUTTN_3_NAME-'),
            sg.VSeparator(),
            sg.Text('Enter File Path'),
            sg.Input('', key = '-BUTTN_3_PATH-')

        ],[ 
            sg.Text('4:'),
            sg.VSeparator(), 
            sg.Text('Name'),
            sg.Input('',key = '-BUTTN_4_NAME-'),
            sg.VSeparator(),
            sg.Text('Enter File Path'),
            sg.Input('', key = '-BUTTN_4_PATH-')

        ],
        [ 
            sg.Text('5:'),
            sg.VSeparator(), 
            sg.Text('Name'),
            sg.Input('',key = '-BUTTN_5_NAME-'),
            sg.VSeparator(),
            sg.Text('Enter File Path'),
            sg.Input('', key = '-BUTTN_5_PATH-')

        ],
        [ 
            sg.Text('6:'),
            sg.VSeparator(), 
            sg.Text('Name'),
            sg.Input('',key = '-BUTTN_6_NAME-'),
            sg.VSeparator(),
            sg.Text('Enter File Path'),
            sg.Input('', key = '-BUTTN_6_PATH-')

        ],
        [ 
            sg.Text('7:'),
            sg.VSeparator(), 
            sg.Text('Name'),
            sg.Input('',key = '-BUTTN_7_NAME-'),
            sg.VSeparator(),
            sg.Text('Enter File Path'),
            sg.Input('', key = '-BUTTN_7_PATH-')

        ],
        [ 
            sg.Text('8:'),
            sg.VSeparator(), 
            sg.Text('Name'),
            sg.Input('',key = '-BUTTN_8_NAME-'),
            sg.VSeparator(),
            sg.Text('Enter File Path'),
            sg.Input('', key = '-BUTTN_8_PATH-')
        ],
        [ 
            sg.Text('9:'),
            sg.VSeparator(), 
            sg.Text('Name'),
            sg.Input('',key = '-BUTTN_9_NAME-'),
            sg.VSeparator(),
            sg.Text('Enter File Path'),
            sg.Input('', key = '-BUTTN__PATH-')

        ],
        [ 
            sg.Push(),
            sg.Button('SAVE PATCH', key = '-SAVE-'),
            sg.Button('RETURN', key = '-RETURN-'),
            sg.Button('Exit', key = '-EXIT-')
        ]
    ]
    return sg.Window('<KIT BUILDER>', layout, resizable= False)

def num_to_key(num_in):
    index = int(num_in)-1
    user_key_arr = np.array(("'-U1-'", "'-U2-'","'-U3-'","'-U4-'","'-U5-'", "'-U6-'","'-U7-'","'-U8-'","'-U9-'"))
    inter_key = user_key_arr[index]
    return inter_key

def save_settings():
    global settings_title, settings_b1, settings_b2, settings_b3, settings_b4, settings_b5, settings_b6, settings_b7, settings_b8, settings_b9
    settings_title = values['-KIT_TITTLE-']
    settings_b1 = values['-BUTTN_1_NAME-']
    settings_b2 = values['-BUTTN_2_NAME-']
    settings_b3 = values['-BUTTN_3_NAME-']
    settings_b4 = values['-BUTTN_4_NAME-']
    settings_b5 = values['-BUTTN_5_NAME-']
    settings_b6 = values['-BUTTN_6_NAME-']
    settings_b7 = values['-BUTTN_7_NAME-']
    settings_b8 = values['-BUTTN_8_NAME-']
    settings_b9 = values['-BUTTN_9_NAME-']
    
    


        

def sound_dir(packed_value):
    u_r = int(packed_value[0])           #unpack win_ref as an integer
    u_e = packed_value[1]               #unpack valid_key event values
    
    #print(str(unpacked_ref) + unpacked_event)
    if u_r == 2:                      #win_ref for classic window, remaining 2 windows will follow similar structure
        if u_e == 'q':                  #valid_key input 
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(cl_hi_tom))
        elif u_e == 'w':
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(cl_mid_tom))
        elif u_e == 'e':
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(cl_lo_tom))
        elif u_e == 'a':
            pygame.mixer.Channel(3).play(pygame.mixer.Sound(cl_hat_cl))
        elif u_e == 's':
            pygame.mixer.Channel(4).play(pygame.mixer.Sound(cl_hat_open))
        elif u_e == 'd':
            pygame.mixer.Channel(5).play(pygame.mixer.Sound(cl_ride))
        elif u_e == 'z':
            pygame.mixer.Channel(6).play(pygame.mixer.Sound(cl_kick))
        elif u_e == 'x':
            pygame.mixer.Channel(7).play(pygame.mixer.Sound(cl_snare))
        elif u_e == 'c':
            pygame.mixer.Channel(8).play(pygame.mixer.Sound(cl_cross))
    
    elif u_r == 3:
        if u_e == 'q':
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(br_hi_tom))
        elif u_e == 'w':
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(br_mid_tom))
        elif u_e == 'e':
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(br_lo_tom))
        elif u_e == 'a':
            pygame.mixer.Channel(3).play(pygame.mixer.Sound(br_hat_cl))
        elif u_e == 's':
            pygame.mixer.Channel(4).play(pygame.mixer.Sound(br_hat_open))
        elif u_e == 'd':
            pygame.mixer.Channel(5).play(pygame.mixer.Sound(br_ride))
        elif u_e == 'z':
            pygame.mixer.Channel(6).play(pygame.mixer.Sound(br_kick))
        elif u_e == 'x':
            pygame.mixer.Channel(7).play(pygame.mixer.Sound(br_snare))
        elif u_e == 'c':
            pygame.mixer.Channel(8).play(pygame.mixer.Sound(br_clave))
    
    elif u_r == 4:
        if u_e == 'q':
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(electronic_hi_tom))
        elif u_e == 'w':
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(electronic_mid_tom))
        elif u_e == 'e':
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(electronic_lo_tom))
        elif u_e == 'a':
            pygame.mixer.Channel(3).play(pygame.mixer.Sound(electronic_hat_cl))
        elif u_e == 's':
            pygame.mixer.Channel(4).play(pygame.mixer.Sound(electronic_hat_open))
        elif u_e == 'd':
            pygame.mixer.Channel(5).play(pygame.mixer.Sound(electronic_crash))
        elif u_e == 'z':
            pygame.mixer.Channel(6).play(pygame.mixer.Sound(electronic_kick))
        elif u_e == 'x':
            pygame.mixer.Channel(7).play(pygame.mixer.Sound(electronic_snare))
        elif u_e == 'c':
            pygame.mixer.Channel(8).play(pygame.mixer.Sound(electronic_rim))

    elif u_r == 5:
        if u_e == 'q':
           # pygame.mixer.Channel(0).play(pygame.mixer.Sound(settings_s1))
           print('<input>')
        elif u_e == 'w':
            print('<input>')
            #pygame.mixer.Channel(1).play(pygame.mixer.Sound(settings_s2))
        elif u_e == 'e':
            print('<input>')
            #pygame.mixer.Channel(2).play(pygame.mixer.Sound(settings_s3))
        elif u_e == 'a':
            print('<input>')
            #pygame.mixer.Channel(3).play(pygame.mixer.Sound(settings_s4))
        elif u_e == 's':
            print('<input>')
            #pygame.mixer.Channel(4).play(pygame.mixer.Sound(settings_s5))
        elif u_e == 'd':
            print('<input>')
           # pygame.mixer.Channel(5).play(pygame.mixer.Sound(settings_s6))
        elif u_e == 'z':
            print('<input>')
           # pygame.mixer.Channel(6).play(pygame.mixer.Sound(settings_s7))
        elif u_e == 'x':
            print('<input>')
            #pygame.mixer.Channel(7).play(pygame.mixer.Sound(settings_s8))
        elif u_e == 'c':
            print('<input>')
            #pygame.mixer.Channel(8).play(pygame.mixer.Sound(settings_s9)) 
        
    else:pass                           #error_handling for any weird events and for win_ref == 1


        


def main(*args, **kwargs):                      #main function of code, handles everything
    while True:
        rename_request = False
        jump = False
        global window 
        global event, values
        event, values = window.read()

        if event in (sg.WIN_CLOSED, '-EXIT-'):   #THIS ALLOWS YOU TO CLOSE THE WINDOW. DO NOT DELETE
            break
        elif event == '-RETURN-':                #returns any window to the main window
            window.close()
            window = menu_window()

        elif event == '-MENUCLASSIC-':           #TPYIICAL: opens drumkit windows from the menu 
            window.close()
            window = classic_window()
        elif event == '-MENUBRUSH-':
            window.close()
            window = brush_window()
        elif event == '-MENU808-':
            window.close()
            window = elec_window()
        
        elif event == '-BUILD-':
            window.close()
            window = import_window()
        if event == '-SAVE-':
            print('Patch Saved')
            save_settings()

        elif event == '-USER_KIT-':                    #create way to import files then save user settings to a .json file.
            window.close()                              #reference https://www.pysimplegui.org/en/latest/cookbook/#recipe-save-and-load-program-settings
            window = user_samples(save_settings())
            print('opened')
            if rename_request == True:
                window[determined_index].update(new_name)
                rename_request = False
                jump = False
        elif event == 'Rename_Button':
            window.close()
            window = rename_prompt()
        
        elif event == '-SET-':
            temp_name = values['-NEW_NAME-']
            temp_index = values['-WHICH_BUTTON-']
            determined_name = str("'"+temp_name + "'")
            determined_index = num_to_key(temp_index)
            inter_path_hold = values['-FILE_PATH-']
            print(determined_index)
            print(determined_name)
            window[determined_index].update(determined_name)
            

        elif event in valid_keys:                        #filters out the non_keyboard events with array valid_keys
            if win_ref in range(1,6):                  #win_ref ranges from 1 through 5
                ref_id = np.array((win_ref, event))    #Creates an array of win_ref and event to pack the values for the sound_dir function
                #print(ref_id)
                sound_dir(ref_id)                      #Checks ref ID arguments to play correct sound
        #print(new_name)
        #window.refresh()
        print(event)


new_name ='<EMPTY>'
which_char = '<EMPTY>'
inter_path_hold = '<EMPTY>'
window = menu_window()                                 #initializes the first window as the menu                            
if __name__ == "__main__":
    main()
