def color_invert(rgb):
    x, y, z = rgb
    return abs(x - 255), abs(y - 255), abs(z - 255),
