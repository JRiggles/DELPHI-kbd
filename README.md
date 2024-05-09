<p align="center">
    <img src="/images/DELPHI logo white.svg" height="92" alt="DELPHI_KBD logo in white">
</p>

Hardware v1.0.2, Software v1.1.1 &copy; 2022-24[^1] ![Static Badge](https://img.shields.io/badge/%20-0E1116?style=flat-square&logo=opensourcehardware&logoColor=fff)

[^1]: Hardware/software versions will (try to) adhere to [SEMVER](https://semver.org/). It is my intention that hardware and software which share a `MAJOR` version will be compatible with one another (e.g., hardware version 1.2.3 will still be compatible with software version 1.0.0)

## Dual Ergolinear Low-Profile Human Interface ##
DELPHI is a minimal split mechanical keyboard designed to combine ergonomics and an ortholinear layout into a small form factor.

<p align="center">
    <img src="/images/IMG_3758.jpg" height="600" alt="Photo of assembled keyboard with PCB plates and the 'LP' version of the 'Edge Case'">
    <br/>
    <br/>
</p>

<p align="center">
    <img src="/images/delphi_kle_layout.png" height="830"  alt="Keyboard Layout Editor layout">
    <br/>
    <a href="http://www.keyboard-layout-editor.com/##@_name=D.E.L.P.H.I.%20FULL&author=John%20Riggles&pcb:false&plate:false&css=*%20%7B%20%0A%20%20%20%20font-family%2F:%20monospace%2F%3B%20font-weight%2F:%20600%2F%3B%20%7D%3B&@_a:7&f:4&w:2&d:true%3B&=LAYER%200&_c=%231f1f1f&t=%23ffffff&p=CHICKLET&f:3%3B&=W&=F&=P&=G&_x:1%3B&=J&=L&=U&=Y%3B&@=TAB&=Q&=R&=S&_n:true%3B&=T&=D&_x:1%3B&=H&_n:true%3B&=N&=E&=I&_a:5%3B&=%2F:%0A%0A%0A%0A%0A%0A%2F%3B&=%22%0A%0A%0A%0A%0A%0A'%3B&@_a:7%3B&=BKDL&=A&=X&=C&=V&=B&_x:1%3B&=K&=M&_a:5%3B&=%3C%0A%0A%0A%0A%0A%0A,&=%3E%0A%0A%0A%0A%0A%0A.&_a:7%3B&=O&_a:4&f:1&fa@:0&:0&:0&:0&:0&:0&:2&:2%3B%3B&=TAP%2F:%0A%0AHOLD%2F:%0A%0A%0A%0AENT%0ASFT%3B&@=1SH%2F:%0A%0AHOLD%2F:%0A%0A%0A%0ASFT%0ACTL&_a:7&f:3%3B&=Z&_x:1%3B&=LALT&=LGUI&=MO(1)&_x:1&a:4&fa@:1&:0&:1%3B&w:2%3B&=TAP%2F:%0A%0AHOLD%2F:%0A%0A%0A%0ASPACE%0AMO(2)&_a:5&f:3%3B&=%3F%0A%0A%0A%0A%0A%0A%2F%2F&_x:1&a:7&f:3%3B&=(&_f:4%3B&=)%3B&@_y:1&c=%23cccccc&t=%23000000&w:2&d:true%3B&=LAYER%201&_c=%231f1f1f&t=%23ffffff&f:3%3B&=2&=3&=4&=5&_x:1%3B&=6&=7&=8&=9%3B&@=GESC&=1&=&=&_n:true%3B&=&=&_x:1%3B&=&_n:true%3B&=4&=5&=6&=0&_a:5%3B&=%7C%0A%0A%0A%0A%0A%0A%5C%3B&@_a:7%3B&=DEL&=&=&=&=&=&_x:1%3B&=&=1&=2&=3&=.&_f:2&fa@:3%3B%3B&=TRNS%3B&@_f:3%3B&=TRNS&_a:5&fa@:1&:1&:0&:0&:0&:0&:1%3B%3B&=CTL%0ADEL%0A%0A%0A%0A%0AALT&_x:1&a:7&f:3%3B&=TRNS&_f:3%3B&=TRNS&_c=%230069ff&a:5&fa@:1&:1%3B%3B&=%0AMO(1)%0A%0A%0A%0A%0ATRNS&_x:1&c=%231f1f1f&a:7&f:3&w:2%3B&=TRNS&_f:3%3B&=0&_x:1&f:3%3B&=%5B&_f:3%3B&=%5D%3B&@_y:1&c=%23cccccc&t=%23000000&f:4&w:2&d:true%3B&=LAYER%202&_c=%231f1f1f&t=%23ffffff&f:3%3B&=%2F@&=%23&=$&=%25&_x:1%3B&=%5E&=%2F&&=*&=(%3B&@=~&=!&=&=&_n:true%3B&=PGUP&=&_x:1%3B&=&_n:true%3B&=UP&_a:5%3B&=%2F_%0A%0A%0A%0A%0A%0A-&=+%0A%0A%0A%0A%0A%0A%2F=&_a:7%3B&=)&=%7C%3B&@=TRNS&=&=&=HOME&=PGDN&=END&_x:1%3B&=LEFT&=DOWN&=RIGHT&=%2F_&=+&_f:2&fa@:3%3B%3B&=TRNS%3B&@_f:3%3B&=TRNS&=&_x:1%3B&=TRNS&=TRNS&=TRNS&_x:1&c=%230069ff&a:5&fa@:0&:1&:0&:0&:0&:0&:0%3B&w:2%3B&=%0AMO(2)%0A%0A%0A%0A%0ATRNS&_c=%231f1f1f&a:7%3B&=&_x:1%3B&=%7B&=%7D%3B&@_t=%23000000&w:13&d:true%3B&=TRNS%2F:%20Transparent%20key%2F%3B%20Blank%2F:%20No%20operation%20(KC.NO)">Layout</a> (yes, it's <a href="https://en.wikipedia.org/wiki/Colemak">COLEMAK</a>)
</p>

## Features
- "Ergolinear" layout combines an ortholinear (columnar) layout with staggered pinky rows for ergonomics
  - Outermost 2 columns on each half are staggered down 1U for easier reach
- Kailh "Choc" low-profile mechanical switches
- Hot-swappable sockets
- Split board (optional, I suppose)
- 40-42 keys (40%) total [20-21 keys on each half]
- Thumb cluster on each half supports a 3&times;1U or a 1&times;1U + 1&times;2U layout
- Wired connection to PC (either half can be connected via USB)
- Wired connection between Left and Right boards (via Adafruit STEMMA QT)
- Dimensions: 4.65" &times; 3.15" (118mm &times; 80mm) [each half]
- [Adafruit QT Py RP2040 microcontroller](https://www.adafruit.com/product/4900) (2&times;)
  - USB C
  - Raspberry Pi RP2040 chip
  - STEMMA QT connector (a.k.a. Qwiic)
> [!IMPORTANT]
> A [STEMMA QT cable](https://www.adafruit.com/product/5385) (or compatible equivalent, such as a SparkFun Qwiic cable) is required to connect the halves<br/>300mm or 400mm length is recommended. The cable pictured above is 300mm long.
  <br/>

  > DELPHI ***might*** also work with the SAMD21 [Adafruit QT PY](https://www.adafruit.com/product/4600) as long as you solder on the "optional"<sup>*</sup> [2MB SPI Flash IC](https://www.adafruit.com/product/4763), but I haven't been able to get this board to work on Windows 11 (YMMV). 
  >
  > <sup>*</sup>KMK firmware will not fit on this board without the extra Flash memory.

## PCB Renders
<p align="center">
    <img src="/images/DELPHI kbd front.png" height="322" alt="PCB render front view">
    <br/>
    PCB top view
</p>

<p align="center">
    <img src="/images/DELPHI kbd rear.png" height="322"  alt="PCB render rear view">
    <br/>
    PCB bottom view
</p>


## Accessories
### PCB top and bottom [plates](https://github.com/JRiggles/DELPHI-kbd/blob/main/plates) 
> [!NOTE]
>  - One plate set covers one *half* of DELPHI - you'll need to use two sets to cover both halves
>  - The main PCB mounts to bottom plate via qty. 5 M2&times;6mm standoffs ***per-half***
>  - It's recommended that you use at least the bottom plate on each half of DELPHI in order to protect the components and avoid hitting the microcontroller's reset / boot buttons 
 
<p align="center">
    <img src="/images/DELPHI plate front.png" height="322" alt="PCB render front view">
    <br/>
    Plates front view (i.e., left side top and bottom plates) - <a href="https://github.com/JRiggles/DELPHI-kbd/blob/main/images/Plates%20LEFT.jpeg">photo here</a>
</p>

<p align="center">
    <img src="/images/DELPHI plate rear.png" height="322"  alt="PCB render rear view">
    <br/>
    Plates rear view (i.e., right side bottom and top plates) - <a href="https://github.com/JRiggles/DELPHI-kbd/blob/main/images/Plates%20RIGHT.jpeg">photo here</a>
</p>

### 3D printable case: the ["Edge Case"](https://github.com/JRiggles/DELPHI-kbd/blob/main/cases) 
> [!NOTE]
>  - This case assumes you're using at least the bottom PCB plate (in addition to the main PCB)
>  - The STL is for the LEFT side; it will need to be *mirrored* in your slicer of choice to accommodate the RIGHT side

There are two case variants:
  - Edge Case LP (low-profile, lines up with bottom plate and main PCB; pictured above on assembled keyboard)
  - Edge Case HP (high-profile, lines up with bottom plate and top plate)
  > Presupported Lychee Slicer scene files (\*.lys) are included for each case variant
  
## Software
- [CircuitPython 8.2.9](https://circuitpython.org/board/adafruit_qtpy_rp2040/)
- [KMK Firmware](https://github.com/KMKfw/kmk_firmware)

## Software Setup

The setup for DELPHI essentially follows the [Quick Start Guide](http://kmkfw.io/docs/Getting_Started#tldr-quick-start-guide) for KMK, with some changes:

1. Connect the **LEFT** half of DELPHI to your computer via USB
2. Download and install [CircuitPython 8.2.9](https://circuitpython.org/board/adafruit_qtpy_rp2040/) for the Adafruit QT Py RP2040
3. [Rename](https://learn.adafruit.com/welcome-to-circuitpython/renaming-circuitpy) the `CIRCUITPY` USB drive to `DELPHI_L` *(must be exactly this!)*
4. Download and unzip [KMK Firmware](https://github.com/KMKfw/kmk_firmware)
5. Download DELPHI [boot.py](https://github.com/JRiggles/DELPHI-kbd/blob/main/firmware/boot.py)
6. Download DELPHI [main.py](https://github.com/JRiggles/DELPHI-kbd/blob/main/firmware/main.py)
7. Copy the `kmk` folder to the root of the `DELPHI_L` drive
8. Copy `boot.py` to the root of the `DELPHI_L` drive[^2]
9. Copy `main.py` to the root of the `DELPHI_L` drive
10. Eject the `DELPHI_L` USB drive and disconnect it from your computer
11. Repeat these steps for the **RIGHT** half of DELPHI, being sure to rename the `CIRCUITPY` drive to `DELPHI_R` at step 3 *(must be exactly this!)*

[^2]: As of firmware v1.1.0, DELPHI hides the CircuitPython USB drive by default. To mount the drive, hold the corresponding homing key (e.g. "T" on the left half or "N" on the right half) while connecting the board. To disable this feature, simply leave the `boot.py` file empty.

##

### TODO
- [ ] Update to CircuitPython 9.0.4
- [ ] Build guide?
- [x] Test printing the Edge Case LP
- [x] Test printing the Edge Case HP
- [ ] ~~[Peg](https://peg.software/) compatibility? - if I can figure it out...~~

*Apparently Peg doesn't play nicely with KMK's "Stringy Keymaps", inline comments in keymaps, or `hold-tap` keycodes. Support for Peg is on hold until further notice.*
