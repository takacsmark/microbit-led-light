LIGHT_TIME = 250000
REPEAT = 2

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
    DigitalPin.P9,
]

def repeat(times, action):
    for i in range(times):
        action()

def forward():
    for pin in PINS.reverse():
        pins.digital_write_pin(pin, 1)
        control.wait_micros(LIGHT_TIME)
        pins.digital_write_pin(pin, 0)

def backward():
    for pin in PINS.reverse():
        pins.digital_write_pin(pin, 1)
        control.wait_micros(LIGHT_TIME)
        pins.digital_write_pin(pin, 0)


def on_forever():
    led.enable(False)
    for i in range(2):
        forward()
    
    control.wait_micros(1000000)

basic.forever(on_forever)
