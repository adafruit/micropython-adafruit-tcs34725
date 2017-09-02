Usage Examples
**************

Connect your sensor in following way:

    * ``3vo`` ↔ ``3V``
    * ``gnd`` ↔ ``gnd``
    * ``sda`` ↔ ``gpio4``
    * ``scl`` ↔ ``gpio5``
    * ``int`` ↔ any other pin (optional)

Now, to make basic measurement::

    import tcs34725
    from machine import I2C, Pin
    i2c = I2C(-1, Pin(5), Pin(4))
    sensor = tcs34725.TCS34725(i2c)
    print(sensor.read())

To perform continuous measurement::

    import time
    sensor.active(True)
    time.sleep_ms(500)
    while True:
        print(sensor.read())
        time.sleep_ms(20)

To change the gain and integration time::

    sensor.gain(16)
    sensor.integration_time(402)

To use the interrupt pin (connected to ``gpio0`` here)::

    def handler(pin):
        print("interrupt!")
        sensor.interrupt(False)

    int_pin = Pin(0, Pin.IN, Pin.PULL_UP)
    int_pin.irq(handler=handler, trigger=Pin.IRQ_FALLING)
    sensor.active(True)
    sensor.threshold(1, 10000, 30000)

