let LIGHT_TIME = 250000
let REPEAT = 4
let PINS = [DigitalPin.P0, DigitalPin.P1, DigitalPin.P2, DigitalPin.P3, DigitalPin.P4, DigitalPin.P5, DigitalPin.P6, DigitalPin.P7, DigitalPin.P8, DigitalPin.P9]
function repeat(times: any, action: any) {
    for (let i = 0; i < times; i++) {
        action
    }
}

function forward() {
    for (let pin of PINS) {
        pins.digitalWritePin(pin, 1)
        control.waitMicros(LIGHT_TIME)
        pins.digitalWritePin(pin, 0)
    }
}

basic.forever(function on_forever() {
    led.enable(false)
    forward()
})
