"""
D.E.L.P.H.I. keyboard - Firmware v1.2.0

MIT License

Copyright (c) 2022-25 John Riggles

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import board as bd
from storage import getmount

from kmk.extensions.stringy_keymaps import StringyKeymaps
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.macros import Delay, Macros, Press, Release
from kmk.modules.split import Split
from kmk.modules.sticky_keys import StickyKeys
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
# keyboard.debug_enabled = True
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.rollover_cols_every_rows = 4

# get drive name to determine which row/col pinout to use (left or right)
# so we can use the same main.py for both halves
DRIVE_NAME = getmount('/').label

if DRIVE_NAME == 'DELPHI_L':  # left half
    keyboard.col_pins = (bd.SCL, bd.SDA, bd.A3, bd.A2, bd.A1, bd.A0)
    keyboard.row_pins = (bd.TX, bd.RX, bd.SCK, bd.MISO)
elif DRIVE_NAME == 'DELPHI_R':  # right half
    keyboard.col_pins = (bd.A1, bd.A2, bd.A3, bd.SDA, bd.SCL, bd.TX)
    keyboard.row_pins = (bd.MOSI, bd.RX, bd.SCK, bd.MISO)
else:
    raise RuntimeError(
        f'Unrecognized CircuitPython drive name "{DRIVE_NAME}"; '
        'must be either "DELPHI_L" or "DELPHI_R"'
    )

# instantiate modules and extensions
keyboard.modules.append(HoldTap())
keyboard.modules.append(Layers())
keyboard.modules.append(Macros())
keyboard.modules.append(StickyKeys())
# enable split - data pin SDA1 is the STEMMA QT data pin
split = Split(data_pin=bd.SDA1, use_pio=True, split_flip=False)
keyboard.modules.append(split)  # enable split
# enable stringy keymaps
stringyKeymaps = StringyKeymaps()
keyboard.extensions.append(stringyKeymaps)

# macros
CTL_ALT_DEL = KC.MACRO(
    Press(KC.LCTL),
    Press(KC.LALT),
    Press(KC.DELETE),
    Delay(25),
    Release(KC.LCTL),
    Release(KC.LALT),
    Release(KC.DELETE),
)
# hold-tap keys
SHIFT_CTRL = KC.HT(KC.SK(KC.LSHIFT), KC.LCTRL)  # tap LSHIFT, hold LCTRL
SHIFT_ENTER = KC.HT(KC.ENTER, KC.RSHIFT, prefer_hold=True)

# keymap
keyboard.keymap = [
    [  # layer 0 (default)
        # row 1 left                                        # row 1 right
        'NO', 'NO', 'W', 'F', 'P', 'G',                     'J', 'L', 'U', 'Y', 'NO', 'NO',
        # row 2 left                                        # row 2 right
        'TAB', 'Q', 'R', 'S', 'T', 'D',                     'H', 'N', 'E', 'I', 'SCOLON', 'QUOTE',
        # row 3 left                                        # row 3 right
        'BSPACE', 'A', 'X', 'C', 'V', 'B',                  'K', 'M', 'COMMA', 'DOT', 'O', SHIFT_ENTER,
        # row 4 left                                        # row 4 right
        SHIFT_CTRL, 'Z',  'NO', 'LALT', 'LGUI', KC.MO(1),   KC.LT(2, KC.SPACE), 'NO', 'SLASH', 'NO', 'LPRN', 'RPRN',
    ],
    [  # layer 1
        # row 1 left                                        # row 1 right
        'NO', 'NO', 'N2', 'N3', 'N4', 'N5',                 'N6', 'N7', 'N8', 'N9', 'NO', 'NO',
        # row 2 left                                        # row 2 right
        'ESCAPE', 'N1', 'NO', 'NO', 'NO', 'NO',             'NO', 'N4', 'N5', 'N6', 'N0', 'BSLASH',
        # row 3 left                                        # row 3 right
        'DELETE', 'NO', 'NO', 'NO', 'NO', 'NO',             'NO', 'N1', 'N2', 'N3', 'DOT', 'TRNS',
        # row 4 left                                            # row 4 right
        'TRNS', CTL_ALT_DEL,  'NO', 'TRNS', 'TRNS', 'TRNS',    'TRNS', 'NO', 'N0', 'NO', 'LBRC', 'RBRC',
    ],
    [  # layer 2
        # row 1 left                                        # row 1 right
        'NO', 'NO', 'AT', 'HASH', 'DOLLAR', 'PERCENT',      'CIRCUMFLEX', 'AMPERSAND', 'ASTERISK', 'LPRN', 'NO', 'NO',
        # row 2 left                                        # row 2 right
        'TILDE', 'EXCLAIM', 'NO', 'NO', 'PGUP', 'NO',       'NO', 'UP', 'MINUS', 'EQUAL', 'RPRN', 'PIPE',
        # row 3 left                                        # row 3 right
        'TRNS', 'NO', 'NO', 'HOME', 'PGDOWN', 'END',        'LEFT', 'DOWN', 'RGHT', 'UNDS', 'PLUS', 'TRNS',
        # row 4 left                                        # row 4 right
        'TRNS', 'GRAVE',  'NO', 'TRNS', 'TRNS', 'TRNS',     'TRNS', 'NO', 'QUESTION', 'NO', 'LCBR', 'RCBR',
    ],
]


if __name__ == '__main__':
    keyboard.go()
