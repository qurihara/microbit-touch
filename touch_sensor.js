// micro:bit v2 タッチ回路 v1
//
// 回路:
//   micro:bit 3V ── 指で触れる ── [人体] ── 指 ── micro:bit P0 ── [固定抵抗 R 例:1MΩ] ── GND
//
// 100ms（商用電源周期の整数倍）の窓で取れるだけサンプリングして平均することで、
// 50Hz / 60Hz のハムを打ち消し、出力を安定させる。
// 値はシリアル(115200bps)に1行1個で出力され、microbit_plot.html で可視化できる。

const WINDOW_MS = 100   // 50/60Hz両方を打ち消す。50Hz東京だけなら20でもOK
basic.forever(function () {
    let sum = 0
    let n = 0
    const start = input.runningTime()
    while (input.runningTime() - start < WINDOW_MS) {
        sum += pins.analogReadPin(AnalogPin.P0)
        n++
    }
    serial.writeLine("" + Math.idiv(sum, n))
})
