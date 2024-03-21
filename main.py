# constants
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

# helpers
def flash_led(pin):
    pins.digital_write_pin(PINS[pin], 1)
    control.wait_micros(LIGHT_TIME)
    pins.digital_write_pin(PINS[pin], 0)
    strip.rotate(1)
    strip.show()

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
        for pin in range(PINS.length):
                        flash_led(pin)
        for pin in range(PINS.length -2, 0, -1): 
            flash_led(pin)

def fill():
    for i in range(REPEAT):
        for pin in range(PINS.length):
            pins.digital_write_pin(PINS[pin], 1)
            control.wait_micros(LIGHT_TIME)
            strip.rotate(1)
            strip.show() 
        
        for pin in range(PINS.length):
            pins.digital_write_pin(PINS[pin], 0)

def fill_flash():
    for i in range(REPEAT):
        for pin in range(PINS.length):
            pins.digital_write_pin(PINS[pin], 1)
            control.wait_micros(LIGHT_TIME)
            strip.rotate(1)
            strip.show()

        for j in range(REPEAT):
            for pin in range(PINS.length):
                pins.digital_write_pin(PINS[pin], 0)
            
            control.wait_micros(LIGHT_TIME)

            for pin in range(PINS.length):
                pins.digital_write_pin(PINS[pin], 1)

            control.wait_micros(LIGHT_TIME)
            strip.rotate(1)
            strip.show()

        for pin in range(PINS.length):
            pins.digital_write_pin(PINS[pin], 0)

def half_flash():
    for i in range(REPEAT * REPEAT):
        for pin in range(PINS.length):
            pins.digital_write_pin(PINS[pin], i % 2) if pin < PINS.length /2 else pins.digital_write_pin(PINS[pin], 1 - i % 2)
        control.wait_micros(LIGHT_TIME)
        strip.rotate(1)
        strip.show()
    
    for pin in range(PINS.length):
        pins.digital_write_pin(PINS[pin], 0)

# init program
led.enable(False)
strip = neopixel.create(DigitalPin.P16, 8, NeoPixelMode.RGB)
strip.show_rainbow(1, 360)

# main logic
def on_forever():
    forward() 
    backward() 
    back_and_forth()
    fill()
    fill_flash()
    half_flash()
basic.forever(on_forever)