# DELPHI-kbd
v1.0

## Dual Ergolinear Low-Profile Human Interface ##
DELPHI is a minimal split mechanical keyboard designed to combine ergonomics and an ortholinear layout into a small form factor.
 
*PCB front view*

<img src="/images/front view.png" height="300" alt="PCB render front view">

*PCB rear view*

<img src="/images/rear view.png" height="300"  alt="PCB render rear view">

*Layout (yes, it's [COLEMAK](https://en.wikipedia.org/wiki/Colemak))*

<img src="/images/delphi_kle_layout.png" height="290"  alt="PCB render rear view">

## Features
- Kailh "Choc" low-profile mechanical switches
- Hot-swappable sockets
- Split board (optional, I suppose)
- 40-42 keys (40%)
- Thumb cluster on each half supports a 3&times;1U or a 1&times;1U + 1&times;2U layout
- Outermost 2 columns on each half are staggered down 1U for easier pinky reach
- Wired connection to PC (either half can be connected via USB)
- Wired connection between Left and Right boards
- Dimensions: 4.65" &times; 3.15" [118mm &times; 80mm] (each half)
- Adafruit QT Py RP2040 microcontroller (2x)
  - USB C
  - Raspberry Pi RP2040 chip
  - STEMMA QT connector (a.k.a. QWiic) [used to connect the two halves over I2C]
  - *Running CircuitPython 8.2.9*
- [KMK](https://github.com/KMKfw/kmk_firmware) firmware
  
<hr/>

### TODO
- Bottom plate [in progress]
- Top plate [in progress]
- 3D-printed case?
