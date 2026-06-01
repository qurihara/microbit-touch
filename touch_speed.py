# micro:bit v2 capacitive touch — 反応速度の実験
from microbit import *

pin0.set_touch_mode(pin0.CAPACITIVE)

# 1) 素のループ速度を起動時に1回だけ測る（display負荷ゼロの基準値）
n = 0
t0 = running_time()
while running_time() - t0 < 1000:
    pin0.is_touched()
    n += 1
print("loop_hz", n)        # 1秒間に何回ポーリングできたか

# 2) 本ループ：エッジ時のみ display と serial を触る
prev = False
edge_t = running_time()
edge_n = 0
while True:
    t = pin0.is_touched()
    edge_n += 1
    if t != prev:
        now = running_time()
        rate = edge_n * 1000 // max(1, now - edge_t)   # 直前区間のポーリング/秒
        display.set_pixel(2, 2, 9 if t else 0)          # 最小コストの視覚表示
        print("P" if t else "R", now, rate)             # 押下/解放のみ送信
        prev = t
        edge_t, edge_n = now, 0
