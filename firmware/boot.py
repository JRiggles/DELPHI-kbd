from kmk.bootcfg import bootcfg

try:
    bootcfg(
        midi=False,
        mouse=False,
        usb_id=('JRiggles', 'D.E.L.P.H.I Kbd')
    )
except Exception as err:
    print(f'D.E.L.P.H.I boot error: {err}')
else:
    print('BOOT OK')
