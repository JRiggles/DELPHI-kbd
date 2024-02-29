"""
D.E.L.P.H.I. keyboard - Firmware v1.1.1

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
==============================================================================
This boot file will automatically disable the circuitpython USB drive unless
the "boot" key on the connected board is pressed. The default "boot" keys for
each half are the keys with the homing dots in the 2nd row ("T" or "N" on the
default COLEMAK layout)
"""
import board
import digitalio as dio
import storage
from supervisor import set_usb_identification

set_usb_identification(manufacturer='J.Riggles', product='DELPHI_KBD')

DRIVE_NAME = storage.getmount('/').label
print(DRIVE_NAME)

if DRIVE_NAME == 'DELPHI_L':  # left half
    col_driver = dio.DigitalInOut(board.A1)
elif DRIVE_NAME == 'DELPHI_R':  # right half
    col_driver = dio.DigitalInOut(board.A2)
else:
    raise RuntimeError(
        f'Unrecognized CircuitPython drive name "{DRIVE_NAME}"; '
        'must be either "DELPHI_L" or "DELPHI_R"'
    )

col_driver.direction = dio.Direction.OUTPUT
col_driver.value = True

boot_key = dio.DigitalInOut(board.RX)
boot_key.direction = dio.Direction.INPUT
boot_key.pull = dio.Pull.DOWN

# mount the circuitpython drive only if the "boot" key on the connected board
# is pressed
# ("T" or "N" on the default layout - the keys with homing dots in the 2nd row)
try:
    if boot_key.value:
        storage.enable_usb_drive()
    else:
        storage.disable_usb_drive()
except Exception as err:
    print(str(err))
else:
    print('BOOT OK')
