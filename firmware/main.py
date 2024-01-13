"""
D.E.L.P.H.I. keyboard - Firmware v1.0.0

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

from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
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

# instantiate modules
holdtap = HoldTap()
keyboard.modules.append(holdtap)

layers = Layers()
keyboard.modules.append(layers)

# enable split - data pin SDA1 is the STEMMA QT data pin
split = Split(data_pin=bd.SDA1, use_pio=True, split_flip=False)
keyboard.modules.append(split)  # enable split

keyboard.keymap = [
    [  # layer 0 (default)
        KC.NO, KC.NO, KC.W, KC.F, KC.P, KC.G,  # row 1 Left
        KC.J, KC.L, KC.U, KC.Y, KC.NO, KC.NO,  # row 1 Right

        KC.TAB, KC.Q, KC.R, KC.S, KC.T, KC.D,  # 2L
        KC.H, KC.N, KC.E, KC.I, KC.SCLN, KC.QUOT,  # 2R

        KC.BKDL, KC.A, KC.X, KC.C, KC.V, KC.B,  # 3L
        KC.K, KC.M, KC.COMMA, KC.DOT, KC.O, KC.HT(KC.ENT, KC.RSFT),  # 3R

        KC.LCTL, KC.Z,  KC.NO, KC.LALT, KC.LGUI, KC.MO(1),  # 4L
        KC.HT(KC.SPC, KC.MO(2)), KC.NO, KC.SLSH, KC.NO, KC.LPRN, KC.RPRN,  # 4R
    ],
    [  # layer 1
        KC.NO, KC.NO, KC.N2, KC.N3, KC.N4, KC.N5,  # 1R
        KC.N6, KC.N7, KC.N8, KC.N9, KC.NO, KC.NO,  # 1L

        KC.GESC, KC.N1, KC.NO, KC.NO, KC.NO, KC.NO,  # 2L
        KC.NO, KC.N4, KC.N5, KC.N6, KC.N0, KC.BSLS,  # 2R

        KC.DEL, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,  # 3L
        KC.NO, KC.N1, KC.N2, KC.N3, KC.NO, KC.TRNS,  # 3R

        KC.TRNS, KC.NO,  KC.NO, KC.TRNS, KC.TRNS, KC.TRNS,  # 4L
        KC.TRNS, KC.NO, KC.N0, KC.NO, KC.LBRC, KC.RBRC,  # 4R
    ],
    [  # layer 2
        KC.NO, KC.NO, KC.AT, KC.HASH, KC.DLR, KC.PERC,  # 1R
        KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.NO, KC.NO,  # 1L

        KC.TILD, KC.EXLM, KC.NO, KC.NO, KC.NO, KC.NO,  # 2L
        KC.NO, KC.UP, KC.MINS, KC.EQL, KC.RPRN, KC.PIPE,  # 2R

        KC.TRNS, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,  # 3L
        KC.LEFT, KC.DOWN, KC.RGHT, KC.NO, KC.NO, KC.TRNS,  # 3R

        KC.TRNS, KC.NO,  KC.NO, KC.TRNS, KC.TRNS, KC.TRNS,  # 4L
        KC.TRNS, KC.NO, KC.NO, KC.NO, KC.LCBR, KC.RCBR,  # 4R
    ],
]


if __name__ == '__main__':
    keyboard.go()
