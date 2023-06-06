# Шевякина Екатерина 44-22-122 задание 1
import math
import sys


def main(*args):
    try:
        x = float(args[0][0])
        if x <= 1:
            return (1 / x) - 1
        else:
            return 2 * math.sin ** 3 (x / 2)
    except:
        return "Произошла ошибка"

print(main(sys.argv[1:]))