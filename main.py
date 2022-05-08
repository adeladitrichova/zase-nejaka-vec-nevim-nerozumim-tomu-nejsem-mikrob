#klient
radio.set_group(28)

answer = 0
alphabet = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

options = 24 #alphabet.count(alphabet)


def on_button_pressed_a():
    global answer
    if answer == 0:
        answer = options - 1
    else:
        answer = (answer-1)%options
        basic.show_string(alphabet[answer])
    basic.clear_screen()

def on_button_pressed_b():
    global answer
    if answer == 0:
        answer = options + 1
    else:
        answer = (answer+1)%options
        basic.show_string(alphabet[answer])
    basic.clear_screen()

def on_logo_is_pressed():
    radio.send_string(alphabet[answer])
    basic.show_string("SENT")

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_logo_up(on_logo_is_pressed)


#server

radio.set_group(28)

receiving = True
answers = []

def on_received_string(receivedString):
    if receiving == True:
        answers.push(receivedString)
        
def on_logo_pressed():
    global receiving
    if receiving == True:
        receiving = False
    else:
        receiving = True

def show_results():
    options = []
    for i in answers:
        if i not in options:
            options.append(i)
    for i in options:
        basic.show_string(i)
        pause(1000)
        basic.show_number(answers.count(i))
        pause(1500)
radio.on_received_string(on_received_string)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
