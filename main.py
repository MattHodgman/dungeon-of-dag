import time
import random
import sys

def typewriter_print(text, delay=0.05):
    """
    Print text character by character with a typewriter effect.
    
    :param text: The text to print.
    :param delay: The delay between each character (in seconds).
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Add a newline at the end

def typewriter_input(prompt, delay=0.05):
    """
    Print a prompt character by character, then wait for input.
    
    :param prompt: The prompt text to display.
    :param delay: The delay between each character (in seconds).
    :return: The user's input.
    """
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return input()

def invalid_input(input_value, valid_options):
    """
    Check if the input value is not in the list of valid options.
    
    :param input_value: The input to check.
    :param valid_options: A list of valid options.
    :return: True if input_value is not in valid_options, False otherwise.
    """
    return input_value not in valid_options

def intro():
    typewriter_print('You wake up...')
    time.sleep(2)
    typewriter_print('*drip* *drip*')
    time.sleep(2)
    typewriter_print('You are in a dark room--the cold stone walls barely visible.')
    time.sleep(3)
    typewriter_print('As your eyes adjust to the darkness, you make out an open doorway ahead of you...')
    time.sleep(3)

def sassy_response():
    sass = [
        'What? You didn\'t understand the simple instructions?',
        'Seriously? It\'s not that hard to follow instructions, is it?',
        'Come on, it\'s just a simple yes or no question.',
        'Are you really that confused? It\'s just a simple question.',
        'I can\'t believe you can\'t follow such simple instructions.',
        'It\'s like you\'re trying to make this harder than it is.',
        'Should I get the handbook out for you?'
    ]
    typewriter_print(random.choice(sass))

def leave_room():
    time.sleep(2)
    typewriter_print('You get to your feet. Ouch, your body is so sore. It feels like you\'ve been lying there' \
    'for a thousand years!')
    time.sleep(4)
    typewriter_print('\033[94m{:>70}\033[0m'.format("Wouldn't that be something."))
    time.sleep(1)
    typewriter_print('!!! What was that?!')
    time.sleep(3)
    
    typewriter_print('Welcome to ...')
    print(
        """ 
           _____ _           ______                                             __  ______            
          |_   _| |          |  _  \                                           / _| |  _  \           
            | | | |__   ___  | | | |_   _ _ __   __ _  ___  ___  _ __     ___ | |_  | | | |__ _  __ _ 
            | | | '_ \ / _ \ | | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \   / _ \|  _| | | | / _` |/ _` |
            | | | | | |  __/ | |/ /| |_| | | | | (_| |  __/ (_) | | | | | (_) | |   | |/ / (_| | (_| |
            \_/ |_| |_|\___| |___/  \__,_|_| |_|\__, |\___|\___/|_| |_|  \___/|_|   |___/ \__,_|\__, |
                                                __/ |                                           __/ |
                                                |___/                                           |___/ 
                                                                                            
        """
    )

def main():

    intro()

    decision = None
    while invalid_input(decision, ['yes', 'no']):

        decision = typewriter_input('Do you enter the doorway? (yes/no) ').strip().lower()

        if decision == 'no':
            time.sleep(1)
            typewriter_print('You decide to stay in the room. BORING! You huddle up close to the wall, trying to keep warm.')
            time.sleep(2)
            typewriter_print('You close your eyes... you are so tired...')
            time.sleep(2)
            typewriter_print('You fall asleep and never wake up again.')
            time.sleep(3)
            typewriter_print('\033[91mGAME OVER\033[0m')
            exit()
        if decision == 'yes':
            leave_room()
        else:
            sassy_response()

if __name__ == "__main__":
    main()