import math


class Color(object):
    x = 0.0
    y = 0.0

    def __init__(self, x=0.0, y=0.0):
        """

        :type y: float
        :type x: float
        """
        self.x = x
        self.y = y

    def to_state_json(self):
        """

        :return: type: object
        """
        return {
            "colormode": "xy",
            "on": True,
            "xy": [self.x, self.y],
            "bri": 255
        }


def from_rgb(rgb):
    """

    :param rgb: list
    :return: Color
    """
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    x, y = convert_rgb_to_xy(blue, green, red)
    return Color(x, y)


def convert_rgb_to_xy(blue, green, red):
    """

    :param blue: int
    :param green: int
    :param red: int
    :return:
    """
    red = math.pow((red + 0.055) / (1.0 + 0.055), 2.4) if (red > 0.04045) else (red / 12.92)
    green = math.pow((green + 0.055) / (1.0 + 0.055), 2.4) if (green > 0.04045) else (green / 12.92)
    blue = math.pow((blue + 0.055) / (1.0 + 0.055), 2.4) if (blue > 0.04045) else (blue / 12.92)
    _x = red * 0.664511 + green * 0.154324 + blue * 0.162028
    _y = red * 0.283881 + green * 0.668433 + blue * 0.047685
    _z = red * 0.000088 + green * 0.072310 + blue * 0.986039
    x = _x / (_x + _y + _z)
    y = _y / (_x + _y + _z)
    return x, y


COLOR_RED = from_rgb([255, 0, 0])
COLOR_GREEN = from_rgb([0, 255, 0])
COLOR_BLUE = from_rgb([0, 0, 255])
COLOR_WHITE = from_rgb([255, 255, 255])
