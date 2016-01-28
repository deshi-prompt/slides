class: center, middle

# Ardbegにみるかわロボ電装系

.right[@takarakasai]
.right[http://kohya.net]

---

# 今回の目的

2014年度かわさきロボット競技大会の参加機体 Ardbeg (@kyo-46 氏作)の構成をもとに,

- 電装系の大まかな仕組み

- かわさきロボットにおける電装系の構成例(※ 1)

- 電装系内部で使用される信号

を紹介します.

<div align="center">
<img src="./slides/dp_kaw_study/ext/ardbeg.png" width="540" />
</div>

.left[※ 1 : 一部構成を変更しています.]

---

# はじめに

- モータが駆動するまでの大まかな流れ.
  1. 操作者がプロポ(1)のスティック（もしくはスイッチ）を操作します
  1. 操作量がプロポ(1)から無線で受信機(2)に送信されます
  1. 受信機(2)は操作量をモータアンプ(3)に送信します
  1. モータアンプ(3)は受信した操作量にしたがってモータ(4)を駆動します

<div align="center">
(1)<img src="./slides/dp_kaw_study/ext/6k.png" width="180" />
(2)<img src="./slides/dp_kaw_study/ext/r3008sb.png" width="180" />
(3)<img src="./slides/dp_kaw_study/ext/mc402cr.png" width="180" />
(4)<img src="./slides/dp_kaw_study/ext/g_motor380.png" width="180" />
</div>

.center[<strong>=====>>=====>>=====>> 信号の流れ =====>>=====>>=====>></strong>]

---

# はじめに

- モータが駆動するまでの大まかな流れ.
  1. 操作者がプロポ(1)のスティック（もしくはスイッチ）を操作します
  1. 操作量がプロポ(1)から無線で受信機(2)に送信されます
  1. 受信機(2)は操作量をモータアンプ(3)に送信します
  1. モータアンプ(3)は受信した操作量にしたがってモータ(4)を駆動します

<div align="center">
(1)<img src="./slides/dp_kaw_study/ext/6k.png" width="180" />
(2)<img src="./slides/dp_kaw_study/ext/r3008sb.png" width="180" />
(3)<img src="./slides/dp_kaw_study/ext/mc402cr.png" width="180" />
(4)<img src="./slides/dp_kaw_study/ext/g_motor380.png" width="180" />
</div>

.center[<strong> ロボットが駆動!! </strong>]
.center[↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓]
<div align="center">
<img src="./slides/dp_kaw_study/ext/ardbeg.png" width="180" />
</div>

---

class: center, middle

<span class="slide_inflame_small">実際の構成を見てみましょう</span>

---

# Ardbeg電装系

<div align="center">
<img src="./slides/dp_kaw_study/fig/elec_whole.png" width="540" />
</div>

---

# Ardbeg電装系 (内部信号)

<div align="center">
<img src="./slides/dp_kaw_study/fig/elec_whole_marked.svg" width="540" />
</div>

---

class: center, middle

<span class="slide_inflame_middle">PPM?</span>

<span class="slide_inflame_middle">PWM?</span>

---

# What is PPM ?

- PPM
  - Pulse Position Modulation (パルス位置変調) の略語
  - モータアンプに対してプロポの操作量を伝達するために使用されています.
  - 多くの市販されているラジコンで利用されている方式です.
     - 大抵の市販アンプ/受信機は信号レベルで相互互換性があります
  - 操作量を電気信号のHighレベル状態の時間の長さに変換しています.

<div align="center">
<img src="./slides/dp_kaw_study/ext/r3008sb.png" width="240" />
<img src="./slides/dp_kaw_study/fig/ppm_variable.svg" width="300" />
<img src="./slides/dp_kaw_study/ext/mc402cr.png" width="240" />
</div>

.center[<strong>=====>>=====>>=====>> 信号の流れ =====>>=====>>=====>></strong>]

---

class: center, middle

<span class="slide_inflame_small">信号の詳細をを見てみましょう</span>

---

# PPM 信号の詳細

- PPM
  - 信号はおおよそ20[msec]毎に繰り返されます(1)
  - 信号のHigh(5V)の時間がプロポの操作量に応じて1.0～2.0[msec]の間で変化します(2)
     - プロポのスティックがニュートラルポジションでHigh時間は1.5[msec]になります.
     - どちらも,メーカにより少異なりますが、動作に支障がでることはほぼありません.
     - 特殊なモータの場合、受信機との組み合わせによってスペックを生かしきれないことがあります.

<div align="center">
(1)<img src="./slides/dp_kaw_study/fig/ppm_period.svg" width="360" />
(2)<img src="./slides/dp_kaw_study/fig/ppm_edge.svg" width="360" />
</div>

---

# What is PWM ?

- PWM
  - Pulse Width Modulation (パルス幅変調) の略語
  - モータアンプがモータを駆動するため使用されています.
  - 市販されている多くのブラシ付DCモータで利用されている方式です.
  - 操作量を電気信号のHighレベル状態の割合に変換しています.

<div align="center">
<img src="./slides/dp_kaw_study/ext/mc402cr.png" width="240" />
<img src="./slides/dp_kaw_study/fig/pwm_6.6v_0.7.svg" width="300" />
<img src="./slides/dp_kaw_study/ext/g_motor380.png" width="240" />
</div>

.center[<strong>=====>>=====>>=====>> 信号の流れ =====>>=====>>=====>></strong>]

---

class: center, middle

<span class="slide_inflame_small">信号の詳細をを見てみましょう</span>

---

# PWM 信号の詳細

- PWM
  - 信号の周波数はおおよそ100[Hz]～10[KHz]です
     - メーカにより異なります.
  - 信号のHigh(5V)の割合がプロポの操作量に応じて0～100[%]の間で変化します
     - この割合がそのままモータ出力の最大出力に対する割合になります

<div align="center">
<img src="./slides/dp_kaw_study/fig/pwm_6.6v_0.2.svg" width="280" />
<img src="./slides/dp_kaw_study/fig/pwm_6.6v_0.7.svg" width="280" />
<img src="./slides/dp_kaw_study/fig/pwm_6.6v_1.0.svg" width="280" />
<p>左から順に 20[%] 70[%] 100[%]</p>
</div>

---


# 参考資料・画像

- 参考資料

- 参考画像
  - 双葉電子工業, 「MC402CR」 https://www.rc.futaba.co.jp/esc/img/img_04.jpg, 双葉電子工業HP
  - 双葉電子工業, 「r3008sb」 https://www.rc.futaba.co.jp/reciever/air04/img/r3008sb.jpg, 双葉電子工業HP
  - 双葉電子工業, 「T6K」 https://www.rc.futaba.co.jp/propo/air/img/6k/img_01.jpg, 双葉電子工業HP
  - オーム社, 「ロボコンマガジン」 http://www.ohmsha.co.jp/robocon/assets_c/2014/08/%E5%86%99%E7%9C%9F%203-thumb-300x168-3676.jpg, オーム社HP
  - 田宮模型, 「タミヤギヤードモータ K380」 http://www.tamiya.com/japan/robocon/robo_parts/g_motor/g_motor380.jpg, 田宮模型HP
  - 田宮模型, 「LiFeバッテリ」 http://tamiya.com/japan/products/55102lfbattery/55102_thmb.jpg, 田宮模型HP


