# DELPHI-kbd

Hardware v1.0.0 &copy; 2022 - Software v1.0.0 &copy; 2024

## Dual Ergolinear Low-Profile Human Interface ##
DELPHI is a minimal split mechanical keyboard designed to combine ergonomics and an ortholinear layout into a small form factor.

<p align="center">
    <img src="/images/DELPHI photo.png" height="600" alt="Photo of assembled keyboard">
    <br/>
    <br/>
</p>

<p align="center">
    <img src="/images/DELPHI kbd front.png" height="322" alt="PCB render front view">
    <br/>
    PCB front view
</p>

<p align="center">
    <img src="/images/DELPHI kbd rear.png" height="322"  alt="PCB render rear view">
    <br/>
    PCB rear view
</p>

<p align="center">
    <img src="/images/delphi_kle_layout.png" height="290"  alt="Keyboard Layout Editor layout">
    <br/>
    <a href="http://www.keyboard-layout-editor.com/##@_name=D.E.L.P.H.I.%20FULL&author=John%20Riggles&pcb:false&plate:false%3B&@_x:2&c=%231f1f1f&t=%23ffffff&p=CHICKLET%3B&=2%0A%0A%0A%2F@%0A%0A%0A%0A%0A%0AW&=3%0A%0A%0A%23%0A%0A%0A%0A%0A%0AF&=4%0A%0A%0A$%0A%0A%0A%0A%0A%0AP&=5%0A%0A%0A%25%0A%0A%0A%0A%0A%0AG&_x:1%3B&=6%0A%0A%0A%5E%0A%0A%0A%0A%0A%0AJ&=7%0A%0A%0A%2F&%0A%0A%0A%0A%0A%0AL&=8%0A%0A%0A*%0A%0A%0A%0A%0A%0AU&=9%0A%0A%0A(%0A%0A%0A%0A%0A%0AY%3B&@=GESC%0A%0A%0A~%0A%0A%0A%0A%0A%0ATAB&=1%0A%0A%0A!%0A%0A%0A%0A%0A%0AQ&_a:7%3B&=R&=S&_n:true%3B&=T&=D&_x:1%3B&=H&_a:4&n:true%3B&=4%0A%0A%0AUP%0A%0A%0A%0A%0A%0AN&=5%0A%0A%0A-%0A%0A%0A%0A-%0A%0AE&=6%0A%0A%0A%2F=%0A%0A%0A%0A+%0A%0AI&=0%0A%0A%0A)%0A%0A%0A%0A%0A%2F:%0A%2F%3B&=%5C%0A%0A%0A%7C%0A%0A%0A%0A%0A%22%0A'%3B&@=DEL%0A%0A%0Atrns%0A%0A%0A%0A%0A%0ABKDL&_a:7%3B&=A&=X&=C&=V&=B&_x:1&a:4%3B&=%0A%0A%0ALEFT%0A%0A%0A%0A%0A%0AK&=1%0A%0A%0ADOWN%0A%0A%0A%0A%0A%0AM&=2%0A%0A%0ARIGHT%0A%0A%0A%0A%0A%3C%0A,&=3%0A%0A%0A%0A%0A%0A%0A%0A%3E%0A.&_a:7%3B&=O&_a:4&f:2%3B&=trns%0A%0A%0Atrns%0A%0A%0A%0A%0A%0AENT%20%5BRSFT%5D%3B&@_f:3%3B&=trns%0A%0A%0Atrns%0A%0A%0A%0A%0A%0ALCTL&_a:7%3B&=Z&_x:1&a:4%3B&=trns%0A%0A%0Atrns%0A%0A%0A%0A%0A%0ALALT&=trns%0A%0A%0Atrns%0A%0A%0A%0A%0A%0ALGUI&=trns%0A%0A%0Atrns%0A%0A%0A%0A%0A%0AMO(1)&_x:1&w:2%3B&=trns%0A%0A%0Atrns%0A%0A%0A%0A%0A%0ASPC%20%5BMO(2)%5D&=0%0A%0A%0A%0A%0A%0A%0A%0A%3F%0A%2F%2F&_x:1%3B&=%5B%0A%0A%0A%7B%0A%0A%0A%0A%0A%0A(&=%5D%0A%0A%0A%7D%0A%0A%0A%0A%0A%0A)%3B&@_c=%23ffffff&t=%23121212&w:4&d:true%3B&=L1%0A%0A%0AL2%0ALAYER%20LEGEND%0A%0A%0A%5BHOLD%5D%0ASHIFT%0AL0&_a:5&w:4&d:true%3B&=%0Astaggered%20down%201%20row%0A%0A%0A(pinky%20offset)%0A%0ACols.%20L%201%20%2F&%202,%20R%205%20%2F&%206">Layout</a> (yes, it's <a href="https://en.wikipedia.org/wiki/Colemak">COLEMAK</a>)
</p>

Designs and production files for the top and bottom PCB plates (photo coming soon!) are in the [plates](https://github.com/JRiggles/DELPHI-kbd/blob/main/plates) folder
(NOTE: one plate set covers one *half* of DELPHI - you'll need to use two sets to cover both halves)

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
- [Adafruit QT Py RP2040 microcontroller](https://www.adafruit.com/product/4900) (2x)
  - USB C
  - Raspberry Pi RP2040 chip
  - STEMMA QT connector (a.k.a. QWiic) [used to connect the two halves over I2C]
    - **NOTE**: a [STEMMA QT cable](https://www.adafruit.com/product/5385) is required to connect the halves - 300mm or 400mm length is recommended
      (the cable pictured above is 300mm)
    
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
11. Repeat these steps for the **RIGHT** half of DELPHI, being sure to rename the `CIRCUITPY` drive to `DELPHI_R` at step 3 *(must be exactly this!)*

<hr/>

### TODO
- 3D-printed case?
- Build guide?

<hr/>

**A note regarding hardware and software versions:**

Hardware/software versions will (try to) adhere to [SEMVER](https://semver.org/). It is my intention that hardware and software which share a `MAJOR` version will be compatible with one another (e.g., hardware version 1.2.3 will still be compatible with software version 1.0.0)
