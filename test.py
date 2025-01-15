import machine
import neopixel
import time

pin = machine.Pin(2)

np = neopixel.NeoPixel(pin, 5)

def demo(np):
    n = np.n

#     # cycle
#     for i in range(4 * n):
#         for j in range(n):
#             np[j] = (0, 0, 0)
#         np[i % n] = (255, 255, 255)
#         np.write()
#         time.sleep_ms(500)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (200, 100, 150)
            if (i / n) % 2 == 0:
              np[i % n] = (0, 0, 0)
            else:
                x=n -1 - (i % n)
                np[x] = (0, 0, 0)
            np.write()
            time.sleep_ms(100)

#     # fade in/out
#     for i in range(0, 4 * 256, 8):
#         for j in range(n):
#             if (i // 256) % 2 == 0:
#                 val = i & 0xff
#             else:
#                 val = 255 - (i & 0xff)
#             np[j] = (val, 0, 0)
#         np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
demo(np)