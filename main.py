LIGHT_TIME = 250000

PINS = [
    DigitalPin.P0,
    DigitalPin.P1,
    DigitalPin.P2,
    DigitalPin.P3,
    DigitalPin.P13,
    DigitalPin.P14,
    DigitalPin.P15,
    DigitalPin.P16,
]

def forward():
    for pin in PINS:
        pins.digital_write_pin(pin, 1)
        control.wait_micros(LIGHT_TIME)
        pins.digital_write_pin(pin, 0)

def on_forever():
    led.enable(False)
    forward()
basic.forever(on_forever)
