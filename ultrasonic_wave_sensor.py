import machine  # type: ignore
import time

# 超音波センサーのTRIGピンとECHOピンのピン番号を定義
TRIG = machine.Pin(17, machine.Pin.OUT)
ECHO = machine.Pin(16, machine.Pin.IN)


def distance():
    # 距離をセンチメートルで計算する関数
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()

    while not ECHO.value():
        pass

    start_time = time.ticks_us()

    while ECHO.value():
        pass

    end_time = time.ticks_us()

    duration = time.ticks_diff(end_time, start_time)

    # 距離を計算
    distance_cm = duration * 340 / 2 / 10000  # cm

    # 範囲外の値をチェック
    if distance_cm > 400:
        return None  # センサーの範囲外の場合はNoneを返す

    return distance_cm


# センサーの距離を1回測定して表示する
dist = distance()
if dist is not None:
    print("Distance: %.2f cm" % dist)
    if dist <= 50:
        print("Object detected within 50 cm!")
else:
    print("Out of range or measurement error")
