# micro:bit v2 内蔵容量タッチ（自己容量方式・商用ハム非依存）
# 電極を P0 に直結（1MΩは付けない）。起動時は電極に触れないこと（自動較正）。
from microbit import *

pin0.set_touch_mode(pin0.CAPACITIVE)

while True:
    t = pin0.is_touched()
    display.show(Image.YES) if t else display.clear()
    print(1 if t else 0)        # シリアルへ → microbit_plot.html で可視化
    sleep(50)
