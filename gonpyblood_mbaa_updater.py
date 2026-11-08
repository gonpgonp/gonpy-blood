with open('MBAA.exe', 'rb+') as f:
    f.seek(0x00064700)
    f.write(b'\xeb\x91\x90\x90\x90\x90\x90')

    f.seek(0x00064e2f)
    f.write(b'\x4d\xf7')

    f.seek(0x00076e7e)
    f.write(b'\x08')