"""
D.E.L.P.H.I. keyboard - Firmware v1.1.0

MIT License

Copyright (c) 2022-24 John Riggles

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
from kmk.modules.oneshot import OneShot
from kmk.modules.split import Split
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
# keyboard.debug_enabled = True
keyboard.diode_orientation = DiodeOrientation.COL2ROW
# keyboard.rollover_cols_every_rows = 4

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
holdtap = HoldTap()
keyboard.modules.append(holdtap)

oneshot = OneShot()
keyboard.modules.append(oneshot)

layers = Layers()
keyboard.modules.append(layers)

# enable split - data pin SDA1 is the STEMMA QT data pin
split = Split(data_pin=bd.SDA1, use_pio=True, split_flip=False)
keyboard.modules.append(split)  # enable split

stringyKeymaps = StringyKeymaps()
keyboard.extensions.append(stringyKeymaps)

keyboard.keymap = [
    [  # layer 0 (default)
        # row 1 left
        'NO', 'NO', 'W', 'F', 'P', 'G',
        # row 1 right
        'J', 'L', 'U', 'Y', 'NO', 'NO',
        # row 2 left
        'TAB', 'Q', 'R', 'S', 'T', 'D',
        # row 2 right
        'H', 'N', 'E', 'I', 'SCOLON', 'QUOTE',
        # row 3 left
        'BKDL', 'A', 'X', 'C', 'V', 'B',
        # row 3 right
        'K', 'M', 'COMMA', 'DOT', 'O', 'ENTER',
        # row 4 left
        KC.HT(KC.OS(KC.LCTRL), KC.LSHIFT), 'Z',  'NO', 'LALT', 'LGUI',
        KC.MO(1),
        # row 4 right
        KC.LT(2, KC.SPACE), 'NO', 'SLASH', 'NO', 'LEFT_PAREN',
        KC.HT(KC.RIGHT_PAREN, KC.RSHIFT),
    ],
    [  # layer 1
        # row 1 left
        'NO', 'NO', 'N2', 'N3', 'N4', 'N5',
        # row 1 right
        'N6', 'N7', 'N8', 'N9', 'NO', 'NO',
        # row 2 left
        'GESC', 'N1', 'NO', 'NO', 'NO', 'NO',
        # row 2 right
        'NO', 'N4', 'N5', 'N6', 'N0', 'BSLASH',
        # row 3 left
        'TRNS', 'NO', 'NO', 'NO', 'NO', 'NO',
        # row 3 right
        'NO', 'N1', 'N2', 'N3', 'NO', 'TRNS',
        # row 4 left
        'TRNS', 'NO',  'NO', 'TRNS', 'TRNS', 'TRNS',
        # row 4 right
        'TRNS', 'NO', 'N0', 'NO', 'LBRACKET',
        KC.HT(KC.RBRACKET, KC.RSHIFT),

    ],
    [  # layer 2
        # row 1 left
        'NO', 'NO', 'AT', 'HASH', 'DOLLAR', 'PERCENT',
        # row 1 right
        'CIRCUMFLEX', 'AMPERSAND', 'ASTERISK', 'LEFT_PAREN', 'NO', 'NO',
        # row 2 left
        'TILDE', 'EXCLAIM', 'NO', 'NO', 'PGUP', 'NO',
        # row 2 right
        'NO', 'UP', 'MINUS', 'EQUAL', 'RIGHT_PAREN', 'PIPE',
        # row 3 left
        'TRNS', 'NO', 'NO', 'HOME', 'PGDOWN', 'END',
        # row 3 right
        'LEFT', 'DOWN', 'RGHT', 'NO', 'NO', 'TRNS',
        # row 4 left
        'TRNS', 'NO',  'NO', 'TRNS', 'TRNS', 'TRNS',
        # row 4 right
        'TRNS', 'NO', 'NO', 'NO', 'LEFT_CURLY_BRACE',
        KC.HT(KC.RIGHT_CURLY_BRACE, KC.RSHIFT),
    ],
]


if __name__ == '__main__':
    keyboard.go()
