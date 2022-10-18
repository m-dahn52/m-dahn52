#
# Michael Dahn 
#
# September 16, 2022
#
#----------------------------------------------------------------------------------------------------------------------
import machine
from machine import Pin,PWM, UART

uart0 = UART(0, 115200)

#Rotary Encoder Pins
step_pin = machine.Pin(7, Pin.IN, Pin.PULL_UP)                       #TriggerPin: clk, was pin 0
dir_pin = machine.Pin(12, Pin.IN, Pin.PULL_UP)                       #Direction: DT, was pin 1
button_pin = machine.Pin(2, Pin.IN, Pin.PULL_UP)                     #Encoder Press: SW

#7 segment display Pins
pins = [
    Pin(20, Pin.OUT),                                                #middle 1
    Pin(21, Pin.OUT),                                                #top left 1
    Pin(22, Pin.OUT),                                                #top 1
    Pin(26, Pin.OUT),                                                #top right 1
    Pin(9, Pin.OUT),                                                 #bottom right 1
    Pin(10, Pin.OUT),                                                #bottom 1
    Pin(11, Pin.OUT),                                                #bottom left 1
    Pin(8, Pin.OUT),                                                 #dot 1
    Pin(16, Pin.OUT),                                                #middle 2
    Pin(17, Pin.OUT),                                                #top left 2 
    Pin(18, Pin.OUT),                                                #top 2 
    Pin(19, Pin.OUT),                                                #top right 2 
    Pin(13, Pin.OUT),                                                #bottom right 2
    Pin(14, Pin.OUT),                                                #bottom 2
    Pin(15, Pin.OUT),                                                #bottom left 2
    #Pin(12, Pin.OUT)                                                #dot 2, No longer active
    ]

#button and LED PINS
b1 = machine.Pin(6, Pin.IN, Pin.PULL_UP) #button 1
b2 = machine.Pin(27, Pin.IN, Pin.PULL_UP) #button 2
b3 = machine.Pin(28, Pin.IN, Pin.PULL_UP) #button 3
l1 = Pin(3, Pin.OUT) #LED 1
l2 = Pin(4, Pin.OUT) #LED 2
l3 = Pin(5, Pin.OUT) #LED 3

l1.off()
l2.off()
l3.off()

#INTEGERS 0-99 on 7-segement Display
chars =  [
    #----------1-----------|   |---------2----------------|
    [1, 0, 0, 0, 0, 0, 0, 0,   1, 0, 0, 0, 0, 0, 0, 0], #00
    [1, 0, 0, 0, 0, 0, 0, 0,   1, 1, 1, 0, 0, 1, 1, 1], #01
    [1, 0, 0, 0, 0, 0, 0, 0,   0, 1, 0, 0, 1, 0, 0, 0], #02
    [1, 0, 0, 0, 0, 0, 0, 0,   0, 1, 0, 0, 0, 0, 1, 0], #03
    [1, 0, 0, 0, 0, 0, 0, 0,   0, 0, 1, 0, 0, 1, 1, 0], #04
    [1, 0, 0, 0, 0, 0, 0, 0,   0, 0, 0, 1, 0, 0, 1, 0], #05
    [1, 0, 0, 0, 0, 0, 0, 0,   0, 0, 0, 1, 0, 0, 0, 0], #06
    [1, 0, 0, 0, 0, 0, 0, 0,   1, 1, 0, 0, 0, 1, 1, 1], #07
    [1, 0, 0, 0, 0, 0, 0, 0,   0, 0, 0, 0, 0, 0, 0, 0], #08
    [1, 0, 0, 0, 0, 0, 0, 0,   0, 0, 0, 0, 0, 0, 1, 0], #09
    [1, 1, 1, 0, 0, 1, 1, 1,   1, 0, 0, 0, 0, 0, 0, 0], #10
    [1, 1, 1, 0, 0, 1, 1, 1,   1, 1, 1, 0, 0, 1, 1, 1], #11
    [1, 1, 1, 0, 0, 1, 1, 1,   0, 1, 0, 0, 1, 0, 0, 0], #12
    [1, 1, 1, 0, 0, 1, 1, 1,   0, 1, 0, 0, 0, 0, 1, 0], #13
    [1, 1, 1, 0, 0, 1, 1, 1,   0, 0, 1, 0, 0, 1, 1, 0], #14
    [1, 1, 1, 0, 0, 1, 1, 1,   0, 0, 0, 1, 0, 0, 1, 0], #15
    [1, 1, 1, 0, 0, 1, 1, 1,   0, 0, 0, 1, 0, 0, 0, 0], #16
    [1, 1, 1, 0, 0, 1, 1, 1,   1, 1, 0, 0, 0, 1, 1, 1], #17
    [1, 1, 1, 0, 0, 1, 1, 1,   0, 0, 0, 0, 0, 0, 0, 0], #18
    [1, 1, 1, 0, 0, 1, 1, 1,   0, 0, 0, 0, 0, 0, 1, 0], #19
    [0, 1, 0, 0, 1, 0, 0, 0,   1, 0, 0, 0, 0, 0, 0, 0], #20
    [0, 1, 0, 0, 1, 0, 0, 0,   1, 1, 1, 0, 0, 1, 1, 1], #21
    [0, 1, 0, 0, 1, 0, 0, 0,   0, 1, 0, 0, 1, 0, 0, 0], #22
    [0, 1, 0, 0, 1, 0, 0, 0,   0, 1, 0, 0, 0, 0, 1, 0], #23
    [0, 1, 0, 0, 1, 0, 0, 0,   0, 0, 1, 0, 0, 1, 1, 0], #24
    [0, 1, 0, 0, 1, 0, 0, 0,   0, 0, 0, 1, 0, 0, 1, 0], #25
    [0, 1, 0, 0, 1, 0, 0, 0,   0, 0, 0, 1, 0, 0, 0, 0], #26
    [0, 1, 0, 0, 1, 0, 0, 0,   1, 1, 0, 0, 0, 1, 1, 1], #27
    [0, 1, 0, 0, 1, 0, 0, 0,   0, 0, 0, 0, 0, 0, 0, 0], #28
    [0, 1, 0, 0, 1, 0, 0, 0,   0, 0, 0, 0, 0, 0, 1, 0], #29
    [0, 1, 0, 0, 0, 0, 1, 0,   1, 0, 0, 0, 0, 0, 0, 0], #30
    [0, 1, 0, 0, 0, 0, 1, 0,   1, 1, 1, 0, 0, 1, 1, 1], #31
    [0, 1, 0, 0, 0, 0, 1, 0,   0, 1, 0, 0, 1, 0, 0, 0], #32
    [0, 1, 0, 0, 0, 0, 1, 0,   0, 1, 0, 0, 0, 0, 1, 0], #33
    [0, 1, 0, 0, 0, 0, 1, 0,   0, 0, 1, 0, 0, 1, 1, 0], #34
    [0, 1, 0, 0, 0, 0, 1, 0,   0, 0, 0, 1, 0, 0, 1, 0], #35
    [0, 1, 0, 0, 0, 0, 1, 0,   0, 0, 0, 1, 0, 0, 0, 0], #36
    [0, 1, 0, 0, 0, 0, 1, 0,   1, 1, 0, 0, 0, 1, 1, 1], #37
    [0, 1, 0, 0, 0, 0, 1, 0,   0, 0, 0, 0, 0, 0, 0, 0], #38
    [0, 1, 0, 0, 0, 0, 1, 0,   0, 0, 0, 0, 0, 0, 1, 0], #39
    [0, 0, 1, 0, 0, 1, 1, 0,   1, 0, 0, 0, 0, 0, 0, 0], #40
    [0, 0, 1, 0, 0, 1, 1, 0,   1, 1, 1, 0, 0, 1, 1, 1], #41
    [0, 0, 1, 0, 0, 1, 1, 0,   0, 1, 0, 0, 1, 0, 0, 0], #42
    [0, 0, 1, 0, 0, 1, 1, 0,   0, 1, 0, 0, 0, 0, 1, 0], #43
    [0, 0, 1, 0, 0, 1, 1, 0,   0, 0, 1, 0, 0, 1, 1, 0], #44
    [0, 0, 1, 0, 0, 1, 1, 0,   0, 0, 0, 1, 0, 0, 1, 0], #45
    [0, 0, 1, 0, 0, 1, 1, 0,   0, 0, 0, 1, 0, 0, 0, 0], #46
    [0, 0, 1, 0, 0, 1, 1, 0,   1, 1, 0, 0, 0, 1, 1, 1], #47
    [0, 0, 1, 0, 0, 1, 1, 0,   0, 0, 0, 0, 0, 0, 0, 0], #48
    [0, 0, 1, 0, 0, 1, 1, 0,   0, 0, 0, 0, 0, 0, 1, 0], #49
    [0, 0, 0, 1, 0, 0, 1, 0,   1, 0, 0, 0, 0, 0, 0, 0], #50
    [0, 0, 0, 1, 0, 0, 1, 0,   1, 1, 1, 0, 0, 1, 1, 1], #51
    [0, 0, 0, 1, 0, 0, 1, 0,   0, 1, 0, 0, 1, 0, 0, 0], #52
    [0, 0, 0, 1, 0, 0, 1, 0,   0, 1, 0, 0, 0, 0, 1, 0], #53
    [0, 0, 0, 1, 0, 0, 1, 0,   0, 0, 1, 0, 0, 1, 1, 0], #54
    [0, 0, 0, 1, 0, 0, 1, 0,   0, 0, 0, 1, 0, 0, 1, 0], #55
    [0, 0, 0, 1, 0, 0, 1, 0,   0, 0, 0, 1, 0, 0, 0, 0], #56
    [0, 0, 0, 1, 0, 0, 1, 0,   1, 1, 0, 0, 0, 1, 1, 1], #57
    [0, 0, 0, 1, 0, 0, 1, 0,   0, 0, 0, 0, 0, 0, 0, 0], #58
    [0, 0, 0, 1, 0, 0, 1, 0,   0, 0, 0, 0, 0, 0, 1, 0], #59
    [0, 0, 0, 1, 0, 0, 0, 0,   1, 0, 0, 0, 0, 0, 0, 0], #60
    [0, 0, 0, 1, 0, 0, 0, 0,   1, 1, 1, 0, 0, 1, 1, 1], #61
    [0, 0, 0, 1, 0, 0, 0, 0,   0, 1, 0, 0, 1, 0, 0, 0], #62
    [0, 0, 0, 1, 0, 0, 0, 0,   0, 1, 0, 0, 0, 0, 1, 0], #63
    [0, 0, 0, 1, 0, 0, 0, 0,   0, 0, 1, 0, 0, 1, 1, 0], #64
    [0, 0, 0, 1, 0, 0, 0, 0,   0, 0, 0, 1, 0, 0, 1, 0], #65
    [0, 0, 0, 1, 0, 0, 0, 0,   0, 0, 0, 1, 0, 0, 0, 0], #66
    [0, 0, 0, 1, 0, 0, 0, 0,   1, 1, 0, 0, 0, 1, 1, 1], #67
    [0, 0, 0, 1, 0, 0, 0, 0,   0, 0, 0, 0, 0, 0, 0, 0], #68
    [0, 0, 0, 1, 0, 0, 0, 0,   0, 0, 0, 0, 0, 0, 1, 0], #69
    [1, 1, 0, 0, 0, 1, 1, 1,   1, 0, 0, 0, 0, 0, 0, 0], #70
    [1, 1, 0, 0, 0, 1, 1, 1,   1, 1, 1, 0, 0, 1, 1, 1], #71
    [1, 1, 0, 0, 0, 1, 1, 1,   0, 1, 0, 0, 1, 0, 0, 0], #72
    [1, 1, 0, 0, 0, 1, 1, 1,   0, 1, 0, 0, 0, 0, 1, 0], #73
    [1, 1, 0, 0, 0, 1, 1, 1,   0, 0, 1, 0, 0, 1, 1, 0], #74
    [1, 1, 0, 0, 0, 1, 1, 1,   0, 0, 0, 1, 0, 0, 1, 0], #75
    [1, 1, 0, 0, 0, 1, 1, 1,   0, 0, 0, 1, 0, 0, 0, 0], #76
    [1, 1, 0, 0, 0, 1, 1, 1,   1, 1, 0, 0, 0, 1, 1, 1], #77
    [1, 1, 0, 0, 0, 1, 1, 1,   0, 0, 0, 0, 0, 0, 0, 0], #78
    [1, 1, 0, 0, 0, 1, 1, 1,   0, 0, 0, 0, 0, 0, 1, 0], #79
    [0, 0, 0, 0, 0, 0, 0, 0,   1, 0, 0, 0, 0, 0, 0, 0], #80
    [0, 0, 0, 0, 0, 0, 0, 0,   1, 1, 1, 0, 0, 1, 1, 1], #81
    [0, 0, 0, 0, 0, 0, 0, 0,   0, 1, 0, 0, 1, 0, 0, 0], #82
    [0, 0, 0, 0, 0, 0, 0, 0,   0, 1, 0, 0, 0, 0, 1, 0], #83
    [0, 0, 0, 0, 0, 0, 0, 0,   0, 0, 1, 0, 0, 1, 1, 0], #84
    [0, 0, 0, 0, 0, 0, 0, 0,   0, 0, 0, 1, 0, 0, 1, 0], #85
    [0, 0, 0, 0, 0, 0, 0, 0,   0, 0, 0, 1, 0, 0, 0, 0], #86
    [0, 0, 0, 0, 0, 0, 0, 0,   1, 1, 0, 0, 0, 1, 1, 1], #87
    [0, 0, 0, 0, 0, 0, 0, 0,   0, 0, 0, 0, 0, 0, 0, 0], #88
    [0, 0, 0, 0, 0, 0, 0, 0,   0, 0, 0, 0, 0, 0, 1, 0], #89
    [0, 0, 0, 0, 0, 0, 1, 0,   1, 0, 0, 0, 0, 0, 0, 0], #90
    [0, 0, 0, 0, 0, 0, 1, 0,   1, 1, 1, 0, 0, 1, 1, 1], #91
    [0, 0, 0, 0, 0, 0, 1, 0,   0, 1, 0, 0, 1, 0, 0, 0], #92
    [0, 0, 0, 0, 0, 0, 1, 0,   0, 1, 0, 0, 0, 0, 1, 0], #93
    [0, 0, 0, 0, 0, 0, 1, 0,   0, 0, 1, 0, 0, 1, 1, 0], #94
    [0, 0, 0, 0, 0, 0, 1, 0,   0, 0, 0, 1, 0, 0, 1, 0], #95
    [0, 0, 0, 0, 0, 0, 1, 0,   0, 0, 0, 1, 0, 0, 0, 0], #96
    [0, 0, 0, 0, 0, 0, 1, 0,   1, 1, 0, 0, 0, 1, 1, 1], #97
    [0, 0, 0, 0, 0, 0, 1, 0,   0, 0, 0, 0, 0, 0, 0, 0], #98
    [0, 0, 0, 0, 0, 0, 1, 0,   0, 0, 0, 0, 0, 0, 1, 0], #99
]

def patch():                                                         #Determines the patch to use
                                             
    global button_down
    global patch_val
    global chars
     
    val_change = False
    previous_value = True
    
    #active_val  = val
    if previous_value != step_pin.value():
        if step_pin.value() == False:
            if dir_pin.value() == False:
                if patch_val > 1 and patch_val <= 99:
                    patch_val = patch_val -1
                    print(patch_val)
                    #print(active_val)
                    val_change = True
                    
                
            else:
                if patch_val >= 0 and patch_val < 99:
                    patch_val = patch_val +1
                    print(patch_val)
                    #print(active_val)
                    val_change = True
                    
                
        previous_value = step_pin.value()
        
    if button_pin.value() == False and not button_down:
        print('Button Push')
        #active_val = val
        #print(active_val)
        button_down = True
        
        
    if button_pin.value() == True and button_down:
        button_down = False
        
    elif val_change == True:
        for i in range(len(chars)):
            for j in range(len(pins)):
                try:
                    pins[j].value(chars[patch_val][j])
                except IndexError:
                   pins[j].value(chars[0][0])
    return(patch_val)

#--------------------------EDIT PATCH--------------------------------             
def edit():                                                          #Edits the waveform
    global previous_value
    global button_down
    global edit_val
    global chars
    val_change = False
    #active_val  = val
    if previous_value != step_pin.value():
        if step_pin.value() == False:
            if dir_pin.value() == False:
                if edit_val > 1 and edit_val <= 99:
                    edit_val = edit_val -1
                    print(edit_val)
                    #print(active_val)
                    val_change = True
                    
                
            else:
                if edit_val >= 0 and edit_val < 99:
                    edit_val = edit_val +1
                    print(edit_val)
                    #print(active_val)
                    val_change = True
                    
                
        previous_value = step_pin.value()
        
    if button_pin.value() == False and not button_down:
        print('Button Push')
        #active_val = val
        #print(active_val)
        button_down = True
        
        
    if button_pin.value() == True and button_down:
        button_down = False
        
    elif val_change == True:
        for i in range(len(chars)):
            for j in range(len(pins)):
                try:
                    pins[j].value(chars[edit_val][j])
                except IndexError:
                   pins[j].value(chars[0][0])

    return(edit_val)

#--------------------------------VOLUME--------------------------------
def volume():                                                        #Sets the volume of the synth
    global previous_value
    global button_down
    global volume_val
    global chars
    val_change = False
    #active_val  = val
    if previous_value != step_pin.value():
        if step_pin.value() == False:
            if dir_pin.value() == False:
                if volume_val > 1 and volume_val < 11:
                    volume_val = volume_val -1
                    print(volume_val)
                    val_change = True
                    
                
            else:
                if volume_val >= 0 and volume_val < 10:
                    volume_val = volume_val +1
                    print(volume_val)
                    val_change = True
                    
                
        previous_value = step_pin.value()
        
    if button_pin.value() == False and not button_down:     #set a value with the button press
        print('Button Push')
        #active_val = val
        button_down = True
        
        
    if button_pin.value() == True and button_down:
        button_down = False
        
    elif val_change == True:
        for i in range(len(chars)):
            for j in range(len(pins)):
                try:
                    pins[j].value(chars[volume_val][j])
                except IndexError:
                   pins[j].value(chars[0][0])
                   
    return(volume_val)


def main():                                                          #Selects the function of the rotary encoder and display
    #Initialize Variables
    #RE
    global mtof                                                      #midi to frequency var
    global b1, b2, b3, l1, l2,l3                                     #Button and LED var
    
    global menu_num
    menu_num = 0                                                     #initialize variable menu_num
    while True:
        if b1.value() == False:                                          #Typical Button select: 
            l1.on()                                                         #Set corrisponding LED states
            l2.off()
            l3.off()
            menu_num = 1                                                    #Set menu_num to corresponding number
            print('menu_num = 1')
            while menu_num == 1:                                            #while loop to run corresponding function
                patch()	                                                    #corresponding function
            
                if b2.value() == False:                                     #Set up conditions to break loop
                    break
                elif b3.value() == False:
                    break
                elif uart0.any() > 0:
                    l1.off()
                    break
    
                
        elif b2.value() == False:
            l1.off()
            l2.on()
            l3.off()
            menu_num = 2
            print('menu_num = 2')
            while menu_num == 2:
                edit()
            
                if b1.value() == False:
                    break
                elif b3.value() == False:
                    break
                elif uart0.any() > 0:
                    l2.off()
                    break
            
            
        elif b3.value() == False:
            l1.off()
            l2.off()
            l3.on()
            menu_num = 3
            print('menu_num = 3')
            while menu_num == 3:
                volume()
            
                if b1.value() == False:
                    break
                elif b2.value() == False:
                    break
                elif uart0.any() > 0:
                    l3.off()
                    break
            
        if uart0.any() > 0:                                              #Sub-In for an interupt request
            data = uart0.read()
            note_read = int(data)                                           #Invalid syntax for integer with base 10
            #print(data)
            if note_read in range(69,81):                                   # Slave transmits '69-81' as str
                print(data)
                #mtof = int(440*2**((note_read - 69)/12))                   # '**' =  exponential operator; '^' =  XOR operator
    
            midi_amp = (volume_val / 10)
            print(midi_amp)


previous_value = True
button_down = False
patch_val = 1
edit_val = 1
volume_val = 1

if __name__ == "__main__":
    main()
