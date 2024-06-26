//  constants
let LIGHT_TIME = 250000
let REPEAT = 4
let PINS = [DigitalPin.P0, DigitalPin.P1, DigitalPin.P2, DigitalPin.P3, DigitalPin.P4, DigitalPin.P5, DigitalPin.P6, DigitalPin.P7, DigitalPin.P8, DigitalPin.P9]
//  helpers
function flash_led(pin: number) {
    pins.digitalWritePin(PINS[pin], 1)
    control.waitMicros(LIGHT_TIME)
    pins.digitalWritePin(PINS[pin], 0)
    strip.rotate(1)
    strip.show()
}

function forward() {
    for (let i = 0; i < REPEAT; i++) {
        for (let pin = 0; pin < PINS.length; pin++) {
            flash_led(pin)
        }
    }
}

function backward() {
    for (let i = 0; i < REPEAT; i++) {
        for (let pin = PINS.length - 1; pin > -1; pin += -1) {
            flash_led(pin)
        }
    }
}

function back_and_forth() {
    let pin: number;
    for (let i = 0; i < REPEAT; i++) {
        for (pin = 0; pin < PINS.length; pin++) {
            flash_led(pin)
        }
        for (pin = PINS.length - 2; pin > 0; pin += -1) {
            flash_led(pin)
        }
    }
}

function fill() {
    let pin: number;
    for (let i = 0; i < REPEAT; i++) {
        for (pin = 0; pin < PINS.length; pin++) {
            pins.digitalWritePin(PINS[pin], 1)
            control.waitMicros(LIGHT_TIME)
            strip.rotate(1)
            strip.show()
        }
        for (pin = 0; pin < PINS.length; pin++) {
            pins.digitalWritePin(PINS[pin], 0)
        }
    }
}

function fill_flash() {
    let pin: number;
    for (let i = 0; i < REPEAT; i++) {
        for (pin = 0; pin < PINS.length; pin++) {
            pins.digitalWritePin(PINS[pin], 1)
            control.waitMicros(LIGHT_TIME)
            strip.rotate(1)
            strip.show()
        }
        for (let j = 0; j < REPEAT; j++) {
            for (pin = 0; pin < PINS.length; pin++) {
                pins.digitalWritePin(PINS[pin], 0)
            }
            control.waitMicros(LIGHT_TIME)
            for (pin = 0; pin < PINS.length; pin++) {
                pins.digitalWritePin(PINS[pin], 1)
            }
            control.waitMicros(LIGHT_TIME)
            strip.rotate(1)
            strip.show()
        }
        for (pin = 0; pin < PINS.length; pin++) {
            pins.digitalWritePin(PINS[pin], 0)
        }
    }
}

function half_flash() {
    let pin: number;
    for (let i = 0; i < REPEAT * REPEAT; i++) {
        for (pin = 0; pin < PINS.length; pin++) {
            pin < PINS.length / 2 ? pins.digitalWritePin(PINS[pin], i % 2) : pins.digitalWritePin(PINS[pin], 1 - i % 2)
        }
        control.waitMicros(LIGHT_TIME)
        strip.rotate(1)
        strip.show()
    }
    for (pin = 0; pin < PINS.length; pin++) {
        pins.digitalWritePin(PINS[pin], 0)
    }
}

//  init program
led.enable(false)
let strip = neopixel.create(DigitalPin.P16, 8, NeoPixelMode.RGB)
strip.showRainbow(1, 360)
//  main logic
basic.forever(function on_forever() {
    forward()
    backward()
    back_and_forth()
    fill()
    fill_flash()
    half_flash()
})
