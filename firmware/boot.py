"""
This boot file will automatically disable the circuitpython USB drive unless
the "boot" key on the connected board is pressed. The default "boot" keys for
each half are the keys with the homing dots in the 2nd row ("T" or "N" on the 
default COLEMAK layout)
"""
import board
import digitalio as dio
import storage

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

# mount the circuitpython drive only if the board's "boot" key is pressed
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
