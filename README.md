# DELPHI-kbd

Hardware v1.0 &copy; 2022 - Software v1.0 &copy; 2024

## Dual Ergolinear Low-Profile Human Interface ##
DELPHI is a minimal split mechanical keyboard designed to combine ergonomics and an ortholinear layout into a small form factor.

<img src="/images/DELPHI photo.png" height="600" alt="Photo of assembled keyboard">
 
*PCB front view*

<img src="/images/front view.png" height="300" alt="PCB render front view">

*PCB rear view*

<img src="/images/rear view.png" height="300"  alt="PCB render rear view">

*Layout (yes, it's [COLEMAK](https://en.wikipedia.org/wiki/Colemak))*

<img src="/images/delphi_kle_layout.png" height="290"  alt="Keyboard Layout Editor layout">

## Features
- Kailh "Choc" low-profile mechanical switches
- Hot-swappable sockets
- Split board (optional, I suppose)
- 40-42 keys (40%)
- Thumb cluster on each half supports a 3&times;1U or a 1&times;1U + 1&times;2U layout
- Outermost 2 columns on each half are staggered down 1U for easier pinky reach
- Wired connection to PC (either half can be connected via USB)
- Wired connection between Left and Right boards
- Dimensions: 4.65" &times; 3.15" (118mm &times; 80mm) [each half]
- Adafruit QT Py RP2040 microcontroller (2x)
  - USB C
  - Raspberry Pi RP2040 chip
  - STEMMA QT connector (a.k.a. QWiic) [used to connect the two halves over I2C]

## Software
- [CircuitPython 8.2.9](https://circuitpython.org/board/adafruit_qtpy_rp2040/)
- [KMK Firmware](https://github.com/KMKfw/kmk_firmware)

## Software Setup

The setup for DELPHI essentially follows the [Quick Start Guide](http://kmkfw.io/docs/Getting_Started#tldr-quick-start-guide) for KMK:

1. Connect the **LEFT** half of DELPHI to your computer via USB
2. Download and install [CircuitPython 8.2.9](https://circuitpython.org/board/adafruit_qtpy_rp2040/) for the Adafruit QT Py RP2040
3. [Rename](https://learn.adafruit.com/welcome-to-circuitpython/renaming-circuitpy) the `CIRCUITPY` USB drive to `DELPHI_L` *(must be exactly this!)*
4. Download and unzip the [KMK Firmware](https://github.com/KMKfw/kmk_firmware)
5. Download DELPHI [boot.py](https://github.com/JRiggles/DELPHI-kbd/blob/main/firmware/boot.py)
6. Download DELPHI [main.py](https://github.com/JRiggles/DELPHI-kbd/blob/main/firmware/main.py)
7. Copy the `kmk` folder to the root of the `DELPHI_L` drive
8. Copy `boot.py` to the root of the `DELPHI_L` drive
9. Copy `main.py` to the root of the `DELPHI_L` drive
10. Eject the `DELPHI_L` USB drive and disconnect it from your computer
    
*This final step is only necessary if you intend to connect DELPHI to your computer via the **RIGHT** half - completing this step will allow you to connect either half of DELPHI to your computer*

11. Repeat these steps for the **RIGHT** half of DELPHI, being sure to rename the `CIRCUITPY` drive to `DELPHI_R` at step 3 *(must be exactly this!)*

### TODO
- Bottom plate [in progress]
- Top plate [in progress]
- 3D-printed case?
- Build guide?
