let LIGHT_TIME = 250000
let PINS = [DigitalPin.P0, DigitalPin.P1, DigitalPin.P2, DigitalPin.P3, DigitalPin.P13, DigitalPin.P14, DigitalPin.P15, DigitalPin.P16]
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
