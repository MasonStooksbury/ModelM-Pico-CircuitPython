from machine import Pin
from time import ticks_ms
import pyb

# This script runs after boot.py

#
#  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15      26 22 21 20 19 18 17 16
# |                                     |    |                       |
#
#
#

key_map = {
    'A': {'S': {'key': 'LCTRL'}, 'W': {'key': 'RCTRL'}},
    'B': {'W': {'key': 'RSHIFT'}},
    'C': {'Q': {'key': 'ESCAPE'},
       'S': {'key': 'BACKTICK'},
       'T': {'key': '1'},
       'U': {'key': 'Q'},
       'V': {'key': 'A'},
       'W': {'key': 'Z'}},
    'D': {'S': {'key': 'F1'},
       'T': {'key': '2'},
       'U': {'key': 'W'},
       'V': {'key': 'S'},
       'W': {'key': 'X'}},
    'E': {'E': {'key': 'F2'},
       'Q': {'key': 'F4'},
       'T': {'key': '3'},
       'U': {'key': 'E'},
       'V': {'key': 'D'},
       'W': {'key': 'C'}},
    'F': {'Q': {'key': 'G'},
       'S': {'key': '5'},
       'T': {'key': '4'},
       'U': {'key': 'R'},
       'V': {'key': 'F'},
       'W': {'key': 'V'},
       'X': {'key': 'B'}},
    'G': {'Q': {'key': 'ENTER'},
       'S': {'key': 'F9'},
       'T': {'key': 'F10'},
       'V': {'key': 'BACKSLASH'},
       'X': {'key': 'SPACE'}},
    'H': {'Q': {'key': 'H'},
       'S': {'key': '6'},
       'T': {'key': '7'},
       'U': {'key': 'U'},
       'V': {'key': 'J'},
       'W': {'key': 'M'},
       'X': {'key': 'N'}},
    'I': {'Q': {'key': 'F6'},
       'S': {'key': 'PLUS'},
       'T': {'key': '8'},
       'U': {'key': 'I'},
       'V': {'key': 'K'},
       'W': {'key': 'COMMA'}},
    'J': {'S': {'key': 'F8'},
       'T': {'key': '9'},
       'U': {'key': 'O'},
       'V': {'key': 'L'},
       'W': {'key': 'PERIOD'}},
    'K': {'Q': {'key': 'QUOTE'},
       'S': {'key': 'MINUS'},
       'T': {'key': '0'},
       'U': {'key': 'P'},
       'V': {'key': 'SEMICOLON'},
       'X': {'key': 'QUESTION'}},
    'L': {'S': {'key': 'DELETE'},
       'T': {'key': 'F11'},
       'U': {'key': 'NUM7'},
       'V': {'key': 'NUM1'},
       'W': {'key': 'NUM LOCK'},
       'X': {'key': 'DOWN'}},
    'M': {'Q': {'key': 'NUM0'},
       'S': {'key': 'INSERT'},
       'T': {'key': 'F12'},
       'U': {'key': 'NUM8'},
       'V': {'key': 'NUM2'},
       'W': {'key': 'NUMSLASH'},
       'X': {'key': 'RIGHT'}},
    'N': {'Q': {'key': 'NUMPERIOD'},
       'S': {'key': 'PG UP'},
       'T': {'key': 'PG DOWN'},
       'U': {'key': 'NUM9'},
       'V': {'key': 'NUM3'},
       'W': {'key': 'NUMASTER'},
       'X': {'key': 'NUMMINUS'}},
    'O': {'Q': {'key': 'UP'},
       'S': {'key': 'HOME'},
       'T': {'key': 'END'},
       'U': {'key': 'NUMPLUS'},
       'V': {'key': 'NUMENTER'},
       'W': {'key': 'PAUSE'},
       'X': {'key': 'LEFT'}},
    'P': {'Q': {'key': 'LALT'},
       'T': {'key': 'PRINT'},
       'U': {'key': 'SCROLL'},
       'X': {'key': 'RALT'}}
}





# Columns
A = {'pin': Pin(0, Pin.OUT), 'name': 'A'}
B = {'pin': Pin(1, Pin.OUT), 'name': 'B'}
C = {'pin': Pin(2, Pin.OUT), 'name': 'C'}
D = {'pin': Pin(3, Pin.OUT), 'name': 'D'}
E = {'pin': Pin(4, Pin.OUT), 'name': 'E'}
F = {'pin': Pin(5, Pin.OUT), 'name': 'F'}
G = {'pin': Pin(6, Pin.OUT), 'name': 'G'}
H = {'pin': Pin(7, Pin.OUT), 'name': 'H'}
I = {'pin': Pin(8, Pin.OUT), 'name': 'I'}
J = {'pin': Pin(9, Pin.OUT), 'name': 'J'}
K = {'pin': Pin(10, Pin.OUT), 'name': 'K'}
L = {'pin': Pin(11, Pin.OUT), 'name': 'L'}
M = {'pin': Pin(12, Pin.OUT), 'name': 'M'}
N = {'pin': Pin(13, Pin.OUT), 'name': 'N'}
O = {'pin': Pin(14, Pin.OUT), 'name': 'O'}
P = {'pin': Pin(15, Pin.OUT), 'name': 'P'}

# Rows
Q = {'pin': Pin(16, Pin.IN, Pin.PULL_DOWN), 'name': 'Q'}
R = {'pin': Pin(17, Pin.IN, Pin.PULL_DOWN), 'name': 'R'}
S = {'pin': Pin(18, Pin.IN, Pin.PULL_DOWN), 'name': 'S'}
T = {'pin': Pin(19, Pin.IN, Pin.PULL_DOWN), 'name': 'T'}
U = {'pin': Pin(20, Pin.IN, Pin.PULL_DOWN), 'name': 'U'}
V = {'pin': Pin(21, Pin.IN, Pin.PULL_DOWN), 'name': 'V'}
W = {'pin': Pin(22, Pin.IN, Pin.PULL_DOWN), 'name': 'W'}
X = {'pin': Pin(26, Pin.IN, Pin.PULL_DOWN), 'name': 'X'}


cols = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P]
rows = [Q,R,S,T,U,V,W,X]

pin_dict = {}

for col in cols:
    pin_dict[col['name']] = {}
    for row in rows:
        pin_dict[col['name']][row['name']] = {
            'current_pin_state': 0,
            'last_pin_state': 0,
            'last_pin_state_change': 0,
            'last_debounce_time': 0,
            'last_actual_state': 0,
            'actual_state': 0
        }




debounceDelay = 0


loop = True
while loop:
    for col in cols:
        col['pin'].on()
        for row in rows:
            pin = pin_dict[col['name']][row['name']]

            pin['current_pin_state'] = row['pin'].value()
            current_time = ticks_ms()

            currentBtnState = pin['current_pin_state']

            if currentBtnState != pin['last_pin_state']:
                pin['last_debounce_time'] = current_time
            
            if (current_time - pin['last_debounce_time']) > debounceDelay:
                pin['actual_state'] = currentBtnState
            
            if (pin['last_actual_state'] == 0) and (pin['actual_state'] == 1):
                print(key_map[col['name']][row['name']]['key'])
            
            pin['last_actual_state'] = pin['actual_state']
            pin['last_pin_state'] = pin['current_pin_state']
        col['pin'].off()