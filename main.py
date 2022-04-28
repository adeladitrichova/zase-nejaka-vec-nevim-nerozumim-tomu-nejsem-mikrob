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

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_logo_up(on_logo_is_pressed)

#server

#radio.set_group(28)


#klient
#kdykoliv muze odeslat hlas
#vzdy se zapisuje posledni odpoved a zapisuje se jen jedna odpoved

#server
#prepina stav >prijima< x >neprijima<
#zapisuje se vzdy jedna odpoved od kazdeho
#zobrazi, kolik lidi dalo A, B, C
#vynuluje svoji "pamet" pak proste yk


#A 65
#B 66
#C 67
#D 68
#odpovedi v listu, aby byl neomezemy pocet odpovedi jakoze ykykykykykykykykyk
#provest listu v listu