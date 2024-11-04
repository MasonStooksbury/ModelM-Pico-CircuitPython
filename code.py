import time
import board
import digitalio
import adafruit_ticks
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode


kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

key_map = {
 'A': {'S': {'keyname': 'LEFT_CONTROL', 'keycode': '224'},
       'W': {'keyname': 'RIGHT_CONTROL', 'keycode': '228'}},
 'B': {'W': {'keyname': 'RIGHT_SHIFT', 'keycode': '229'}},
 'C': {'Q': {'keyname': 'ESCAPE', 'keycode': '41'},
       'S': {'keyname': 'GRAVE_ACCENT', 'keycode': '53'},
       'T': {'keyname': 'ONE', 'keycode': '30'},
       'U': {'keyname': 'Q', 'keycode': '20'},
       'V': {'keyname': 'A', 'keycode': '4'},
       'W': {'keyname': 'Z', 'keycode': '29'}},
 'D': {'S': {'keyname': 'F1', 'keycode': '58'},
       'T': {'keyname': 'TWO', 'keycode': '31'},
       'U': {'keyname': 'W', 'keycode': '26'},
       'V': {'keyname': 'S', 'keycode': '22'},
       'W': {'keyname': 'X', 'keycode': '27'}},
 'E': {'Q': {'keyname': 'F4', 'keycode': '61'},
       'S': {'keyname': 'F2', 'keycode': '59'},
       'T': {'keyname': 'THREE', 'keycode': '32'},
       'U': {'keyname': 'E', 'keycode': '8'},
       'V': {'keyname': 'D', 'keycode': '7'},
       'W': {'keyname': 'C', 'keycode': '6'}},
 'F': {'Q': {'keyname': 'G', 'keycode': '10'},
       'S': {'keyname': 'FIVE', 'keycode': '34'},
       'T': {'keyname': 'FOUR', 'keycode': '33'},
       'U': {'keyname': 'R', 'keycode': '21'},
       'V': {'keyname': 'F', 'keycode': '9'},
       'W': {'keyname': 'V', 'keycode': '25'},
       'X': {'keyname': 'B', 'keycode': '5'}},
 'G': {'Q': {'keyname': 'F5', 'keycode': '62'},
       'S': {'keyname': 'F9', 'keycode': '66'},
       'T': {'keyname': 'F10', 'keycode': '67'},
       'V': {'keyname': 'BACKSLASH', 'keycode': '49'},
       'W': {'keyname': 'ENTER', 'keycode': '40'},
       'X': {'keyname': 'SPACE', 'keycode': '44'}},
 'H': {'Q': {'keyname': 'H', 'keycode': '11'},
       'S': {'keyname': 'SIX', 'keycode': '35'},
       'T': {'keyname': 'SEVEN', 'keycode': '36'},
       'U': {'keyname': 'U', 'keycode': '24'},
       'V': {'keyname': 'J', 'keycode': '13'},
       'W': {'keyname': 'M', 'keycode': '16'},
       'X': {'keyname': 'N', 'keycode': '17'}},
 'I': {'Q': {'keyname': 'F6', 'keycode': '63'},
       'S': {'keyname': 'EQUALS', 'keycode': '46'},
       'T': {'keyname': 'EIGHT', 'keycode': '37'},
       'U': {'keyname': 'I', 'keycode': '12'},
       'V': {'keyname': 'K', 'keycode': '14'},
       'W': {'keyname': 'COMMA', 'keycode': '54'}},
 'J': {'S': {'keyname': 'F8', 'keycode': '65'},
       'T': {'keyname': 'NINE', 'keycode': '38'},
       'U': {'keyname': 'O', 'keycode': '18'},
       'V': {'keyname': 'L', 'keycode': '15'},
       'W': {'keyname': 'PERIOD', 'keycode': '55'}},
 'K': {'Q': {'keyname': 'QUOTE', 'keycode': '52'},
       'S': {'keyname': 'MINUS', 'keycode': '45'},
       'T': {'keyname': 'ZERO', 'keycode': '39'},
       'U': {'keyname': 'P', 'keycode': '19'},
       'V': {'keyname': 'SEMICOLON', 'keycode': '51'},
       'X': {'keyname': 'FORWARD_SLASH', 'keycode': '56'}},
 'L': {'S': {'keyname': 'DELETE', 'keycode': '76'},
       'T': {'keyname': 'F11', 'keycode': '68'},
       'U': {'keyname': 'KEYPAD_SEVEN', 'keycode': '95'},
       'V': {'keyname': 'KEYPAD_ONE', 'keycode': '89'},
       'W': {'keyname': 'KEYPAD_NUMLOCK', 'keycode': '83'},
       'X': {'keyname': 'DOWN_ARROW', 'keycode': '81'}},
 'M': {'Q': {'keyname': 'KEYPAD_ZERO', 'keycode': '98'},
       'S': {'keyname': 'INSERT', 'keycode': '73'},
       'T': {'keyname': 'F12', 'keycode': '69'},
       'U': {'keyname': 'KEYPAD_EIGHT', 'keycode': '96'},
       'V': {'keyname': 'KEYPAD_TWO', 'keycode': '90'},
       'W': {'keyname': 'KEYPAD_FORWARD_SLASH', 'keycode': '84'},
       'X': {'keyname': 'RIGHT_ARROW', 'keycode': '79'}},
 'N': {'Q': {'keyname': 'KEYPAD_PERIOD', 'keycode': '99'},
       'S': {'keyname': 'PAGE_UP', 'keycode': '75'},
       'T': {'keyname': 'PAGE_DOWN', 'keycode': '78'},
       'U': {'keyname': 'KEYPAD_NINE', 'keycode': '97'},
       'V': {'keyname': 'KEYPAD_THREE', 'keycode': '91'},
       'W': {'keyname': 'KEYPAD_ASTERISK', 'keycode': '85'},
       'X': {'keyname': 'KEYPAD_MINUS', 'keycode': '86'}},
 'O': {'Q': {'keyname': 'UP_ARROW', 'keycode': '82'},
       'S': {'keyname': 'HOME', 'keycode': '74'},
       'T': {'keyname': 'END', 'keycode': '77'},
       'U': {'keyname': 'KEYPAD_PLUS', 'keycode': '87'},
       'V': {'keyname': 'KEYPAD_ENTER', 'keycode': '96'},
       'W': {'keyname': 'PAUSE', 'keycode': '72'},
       'X': {'keyname': 'LEFT_ARROW', 'keycode': '80'}},
 'P': {'Q': {'keyname': 'LEFT_ALT', 'keycode': '226'},
       'T': {'keyname': 'PRINT_SCREEN', 'keycode': '70'},
       'U': {'keyname': 'SCROLL_LOCK', 'keycode': '71'},
       'X': {'keyname': 'RIGHT_ALT', 'keycode': '230'}}
}


# Columns
A = {'pin': digitalio.DigitalInOut(board.GP0), 'name': 'A'}
B = {'pin': digitalio.DigitalInOut(board.GP1), 'name': 'B'}
C = {'pin': digitalio.DigitalInOut(board.GP2), 'name': 'C'}
D = {'pin': digitalio.DigitalInOut(board.GP3), 'name': 'D'}
E = {'pin': digitalio.DigitalInOut(board.GP4), 'name': 'E'}
F = {'pin': digitalio.DigitalInOut(board.GP5), 'name': 'F'}
G = {'pin': digitalio.DigitalInOut(board.GP6), 'name': 'G'}
H = {'pin': digitalio.DigitalInOut(board.GP7), 'name': 'H'}
I = {'pin': digitalio.DigitalInOut(board.GP8), 'name': 'I'}
J = {'pin': digitalio.DigitalInOut(board.GP9), 'name': 'J'}
K = {'pin': digitalio.DigitalInOut(board.GP10), 'name': 'K'}
L = {'pin': digitalio.DigitalInOut(board.GP11), 'name': 'L'}
M = {'pin': digitalio.DigitalInOut(board.GP12), 'name': 'M'}
N = {'pin': digitalio.DigitalInOut(board.GP13), 'name': 'N'}
O = {'pin': digitalio.DigitalInOut(board.GP14), 'name': 'O'}
P = {'pin': digitalio.DigitalInOut(board.GP15), 'name': 'P'}

# Rows
Q = {'pin': digitalio.DigitalInOut(board.GP16), 'name': 'Q'}
R = {'pin': digitalio.DigitalInOut(board.GP17), 'name': 'R'}
S = {'pin': digitalio.DigitalInOut(board.GP18), 'name': 'S'}
T = {'pin': digitalio.DigitalInOut(board.GP19), 'name': 'T'}
U = {'pin': digitalio.DigitalInOut(board.GP20), 'name': 'U'}
V = {'pin': digitalio.DigitalInOut(board.GP21), 'name': 'V'}
W = {'pin': digitalio.DigitalInOut(board.GP22), 'name': 'W'}
X = {'pin': digitalio.DigitalInOut(board.GP26), 'name': 'X'}


cols = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P]
rows = [Q,R,S,T,U,V,W,X]

# Set all columns as outputs
for col in cols:
    col['pin'].switch_to_output()

# Set all rows as inputs and set the pulldown resistors
for row in rows:
    row['pin'].switch_to_input(pull=digitalio.Pull.DOWN)


# Initialize the dictionary we will use to track pin states and info
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
            'actual_state': 0,
            'holding_state': False,
            'start_hold_time': 0,
        }


# Initialize a dictionary with all of the modifier keys so we can check them separately later
modifier_dict = {}
for k,v in key_map.items():
    for k2,v2 in v.items():
        if 'SHIFT' in v2['keyname'] or 'ALT' in v2['keyname'] or 'CONTROL' in v2['keyname']:
            modifier_dict[v2['keyname']] = {'col': k, 'row': k2}



def getPin(matrix_letter):
    for col in cols:
        if matrix_letter == col['name']:
            return col['pin']
    for row in rows:
        if matrix_letter == row['name']:
            return row['pin']


def checkModifiers():
    is_shift = False
    is_alt = False
    is_ctrl = False

    for k,v in modifier_dict.items():
        column_pin = getPin(v['col'])
        row_pin = getPin(v['row'])

        column_pin.value = True
        if 'SHIFT' in k:
            is_shift = row_pin.value
        if 'ALT' in k:
            is_alt = row_pin.value
        if 'CONTROL' in k:
            is_ctrl = row_pin.value
        column_pin.value = False

    return is_shift, is_alt, is_ctrl




debounceDelay = 0
#holdTimeCheck = 50
holdTimeCheck = 225
is_modifier = False

loop = True
while loop:
    is_shift, is_alt, is_ctrl = checkModifiers()

    for col in cols:
        col['pin'].value = True
        for row in rows:
            pin = pin_dict[col['name']][row['name']]
            keyname = 'wee'
            try:
                keyname = key_map[col['name']][row['name']]['keyname']
            except:
                pass

            # Set if it's a modifier so we can skip them. Stuff gets super weird if we don't
            is_modifier = 'SHIFT' in keyname or 'ALT' in keyname or 'CONTROL' in keyname

            pin['current_pin_state'] = row['pin'].value

            current_time = adafruit_ticks.ticks_ms()

            currentBtnState = pin['current_pin_state']

            if currentBtnState != pin['last_pin_state']:
                pin['last_debounce_time'] = current_time

            if (current_time - pin['last_debounce_time']) > debounceDelay:
                pin['actual_state'] = currentBtnState

            if not is_modifier and (pin['last_actual_state'] == 0) and (pin['actual_state'] == 1):
                keycode = int(key_map[col['name']][row['name']]['keycode'])
                keyname = key_map[col['name']][row['name']]['keyname']
                if is_shift:
                    kbd.press(Keycode.SHIFT, keycode)
                    kbd.release(Keycode.SHIFT)
                elif is_alt:
                    kbd.press(Keycode.ALT, keycode)
                    kbd.release(Keycode.ALT)
                elif is_ctrl:
                    print('first')
                    kbd.press(Keycode.CONTROL, keycode)
                    kbd.release(Keycode.CONTROL)
                else:
                    kbd.press(keycode)
                print('pressed', col['name'], row['name'], key_map[col['name']][row['name']]['keyname'])
            elif not is_modifier and (pin['last_actual_state'] == 1) and (pin['actual_state'] == 1):
                #if not pin['holding_state']:
                    #kbd.release(int(key_map[col['name']][row['name']]['keycode']))
                if pin['start_hold_time'] == 0:
                    pin['start_hold_time'] = current_time
                print((current_time - pin['start_hold_time']) > holdTimeCheck)
                if pin['start_hold_time'] > 0 and (current_time - pin['start_hold_time']) > holdTimeCheck:
                    keycode = int(key_map[col['name']][row['name']]['keycode'])
                    pin['holding_state'] = True
                    if is_shift:
                        kbd.press(Keycode.SHIFT, keycode)
                        kbd.release(Keycode.SHIFT)
                    elif is_alt:
                        kbd.press(Keycode.ALT, keycode)
                        kbd.release(Keycode.ALT)
                    elif is_ctrl:
                        print('second')
                        kbd.press(Keycode.CONTROL, keycode)
                        kbd.release(Keycode.CONTROL)
                    else:
                        print('hold press')
                        kbd.press(keycode)
                    #print('holding', col['name'], row['name'], key_map[col['name']][row['name']]['keyname'])
            elif (pin['last_actual_state'] == 1) and (pin['actual_state'] == 0):
                keycode = int(key_map[col['name']][row['name']]['keycode'])
                pin['start_hold_time'] = 0
                pin['holding_state'] = False
                kbd.release(keycode)
                print('released', col['name'], row['name'], key_map[col['name']][row['name']]['keyname'])
            pin['last_actual_state'] = pin['actual_state']
            pin['last_pin_state'] = pin['current_pin_state']
        col['pin'].value = False










