def rgb(*args):
    return "".join('{:02X}'.format(color) if color >= 0 and color <= 255 else '00' if color < 0 else 'FF' for color in args)