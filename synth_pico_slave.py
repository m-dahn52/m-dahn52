# Michael Dahn
#
# August 18, 2022
#
#
#----------------------------------------------------------------------------------------------------------------------

from machine import Pin, PWM,  UART
import time

uart0 = machine.UART(0, 115200)
#uart0.init(115200, bits=8, parity=None, stop=1)

#Key IN PINS
c = machine.Pin(2, Pin.IN, Pin.PULL_UP)
db = machine.Pin(3, Pin.IN,Pin.PULL_UP)
d = machine.Pin(4,  Pin.IN, Pin.PULL_UP)
eb = machine.Pin(5, Pin.IN,  Pin.PULL_UP)
e = machine.Pin(12,  Pin.IN, Pin.PULL_UP)
f = machine.Pin(14,  Pin.IN, Pin.PULL_UP)
gb = machine.Pin(15, Pin.IN,  Pin.PULL_UP)
g = machine.Pin(21,  Pin.IN, Pin.PULL_UP)
ab = machine.Pin(20, Pin.IN,  Pin.PULL_UP)
a = machine.Pin(19,  Pin.IN, Pin.PULL_UP)
bb = machine.Pin(18,  Pin.IN, Pin.PULL_UP)
b = machine.Pin(17,  Pin.IN, Pin.PULL_UP)
c8 = machine.Pin(16, Pin.IN,  Pin.PULL_UP)


    
def midi_create():
    global c,db,d,eb,e,f,gb,g,ab,a,bb,b,c8
    if c.value() == False:
        print('c')
        note = 69
        uart0.write('69 \r\n')
        while c.value() == False:
            if c.value() == True:
                print('C released')
                break

    elif db.value() == False:
        print('Db')
        note = 70
        uart0.write('70 \r\n')
        while db.value() == False:
            if db.value() == True:
                print('Db released')
                break
                
            
    elif d.value() == False:
        print('d')
        note = 71
        uart0.write('71 \r\n')
        while d.value() == False:
            if d.value() == True:
                print('D released')
                break
            
                
        
    elif eb.value() == False:
        print('Eb')
        note = 72
        uart0.write('72 \r\n')
        while eb.value() == False:
            if eb.value() == True:
                print('Eb released')
                break
        
    elif e.value() == False:
        print('E')
        note = 73
        uart0.write('73 \r\n')
        while e.value() == False:
            if e.value() == True:
                print('E released')
                break
        
    elif f.value() == False:
        print('F')
        note = 74
        uart0.write('74 \r\n')
        while f.value() == False:
            if f.value() == True:
                print('F released')
                break
            
    elif gb.value() == False:
        print('Gb')
        note = 75
        uart0.write('75')
        while gb.value() == False:
            if gb.value() == True:
                print('Gb released')
                break
            
    elif g.value() == False:
        print('G')
        note = 76
        uart0.write('76 \r\n' )
        while g.value() == False:
            if g.value() == True:
                print('G released')
                break
            
    elif ab.value() == False:
        print('Ab')
        note = 77
        uart0.write('77 \r\n')
        while ab.value() == False:
            if ab.value() == True:
                print('Ab released')
                break
            
    elif a.value() == False:
        print('A')
        note = 78
        uart0.write('78 \r\n')
        while a.value() == False:
            if a.value() == True:
                print('A released')
                break
            
    elif bb.value() == False:
        print('Bb')
        note = 79
        uart0.write('79 \r\n')
        while bb.value() == False:
            if bb.value() == True:
                print('Bb released')
                break
            
    elif b.value() == False:
        print('b')
        note = 80
        uart0.write('80 \r\n')
        while b.value() == False:
            if b.value() == True:
                print('B released')
                break
            
    elif c8.value() == False:
        print('c8')
        note = 81
        uart0.write('81 \r\n')
        while c8.value() == False:
            if c8.value() == True:
                print('C released')
                break
        
while True:
    midi_create()
