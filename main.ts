// klient
radio.setGroup(28)
let answer = 0
let alphabet = ["A", "B", "C", "D", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
let options = 24
// alphabet.count(alphabet)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (answer == 0) {
        answer = options - 1
    } else {
        answer = (answer - 1) % options
        basic.showString(alphabet[answer])
    }
    
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (answer == 0) {
        answer = options + 1
    } else {
        answer = (answer + 1) % options
        basic.showString(alphabet[answer])
    }
    
    basic.clearScreen()
})
input.onLogoUp(function on_logo_is_pressed() {
    radio.sendString(alphabet[answer])
})
// server
radio.setGroup(28)
let receiving = true
let answers = []
function show_results() {
    options
}

radio.onReceivedString(function on_received_string(receivedString: string) {
    if (receiving == true) {
        answers.push(receivedString)
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    if (receiving == true) {
        receiving = false
    } else {
        receiving = true
    }
    
})
