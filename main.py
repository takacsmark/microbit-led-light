LIGHT_TIME = 250000
REPEAT = 4

PINS = [
    DigitalPin.P0,
    DigitalPin.P1,
    DigitalPin.P2,
    DigitalPin.P3,
    DigitalPin.P4,
    DigitalPin.P5,
    DigitalPin.P6,
    DigitalPin.P7,
    DigitalPin.P8,
    DigitalPin.P9
    ]

def flash_led(pin):
    pins.digital_write_pin(PINS[pin], 1)
    control.wait_micros(LIGHT_TIME)
    pins.digital_write_pin(PINS[pin], 0)

def forward():
    for i in range(REPEAT):
        for pin in range(PINS.length):
                flash_led(pin)

def backward():
    for i in range(REPEAT):
        for pin in range(PINS.length -1, -1, -1):
            flash_led(pin)

def back_and_forth():
    for i in range(REPEAT):
        forward()
        for pin in range(PINS.length -2, 0, -1): 
            flash_led(pin)

led.enable(False)

def on_forever():
    forward()
    backward()  
    back_and_forth()
basic.forever(on_forever)