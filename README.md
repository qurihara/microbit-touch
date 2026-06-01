# microbit-touch

micro:bit v2 を使ったタッチ／人体アンテナ実験のためのコードと可視化ツール。

## 構成

| ファイル | 内容 |
|---|---|
| [`touch_sensor.js`](touch_sensor.js) | **(v1)** micro:bit 側の MakeCode (JavaScript)。P0 のアナログ値を商用周期の整数倍で平均し、シリアルに出力する。人体アンテナで拾う商用ハムを利用した抵抗式。 |
| [`touch_capacitive.py`](touch_capacitive.py) | **(v2)** micro:bit 側の MicroPython。v2 内蔵の容量タッチ（自己容量方式）。商用ハムに依存せず、地域・電池駆動でも安定。 |
| [`microbit_plot.html`](microbit_plot.html) | PC 側のライブグラフツール。Web Serial API でシリアルを受信し、数値をリアルタイムに折れ線グラフ表示する。 |

## 回路

```
micro:bit 3V ── 指で触れる ── [人体] ── 指 ── micro:bit P0 ── [固定抵抗 R 例:1MΩ] ── GND
```

P0 は超高インピーダンスのアナログ入力で、人体がアンテナとなって商用電源の
50Hz / 60Hz を拾う。`touch_sensor.js` は 100ms（50Hz=20ms と 60Hz≈16.7ms の
公倍数）の窓で平均することでこのハムを打ち消し、安定した値を出力する。

## v2: 内蔵容量タッチ（MicroPython）

`touch_capacitive.py` は micro:bit v2 内蔵の能動容量センシングを使う。ピン自身を充放電して
時間を測る自己容量方式なので、**周囲の商用ハムに依存せず**、関西（60Hz）でも電池駆動でも安定して
動作する。電極を P0 に直結するだけ（**v1 の 1MΩ は付けない**）。起動時は電極に触れないこと（無接触を
基準に自動較正するため）。

`uflash` で直接書き込める：

```sh
uflash touch_capacitive.py
```

## micro:bit への書き込み

1. [MakeCode エディタ](https://makecode.microbit.org) を開き、JavaScript 表示に切り替える
2. `touch_sensor.js` の内容を貼り付ける
3. `.hex` をダウンロードし、`MICROBIT` ドライブにコピーする

## 可視化ツールの使い方

1. 他のシリアルモニタを閉じる（シリアルポートは 1 つのアプリしか掴めない）
2. `microbit_plot.html` を **Chrome / Edge** で開く（Safari は Web Serial 非対応）
3. 「接続」を押し、`cu.usbmodem...`（DAPLink CDC）を選ぶ
4. micro:bit が出力する数値がリアルタイムにグラフ表示される

### 機能

- カンマ区切りの複数値に自動対応（例 `amp,baseline,touched` → 複数系列を色分け表示）
- Y 軸：自動スケール / 0–1023 固定の切替
- 表示点数の調整、一時停止 / クリア / CSV 保存

インストール不要・単一 HTML ファイル・完全オフライン動作。
