# Polyalphabet cypher bot 
import telebot
from key_generator import key_generator
import os
# =============================================================================
# Main alphabet
# =============================================================================
alphabet_0 = []
for letter in range(97,123):
    alphabet_0.append(chr(letter))
for letter in range(32,91):
    alphabet_0.append(chr(letter))
# =============================================================================
# Token checking/inputing
# =============================================================================
try:
    bot_input = open("bot_token.tg", 'r').read()
except:
    bot_input = input('Incert Bot Token here: ')
    bot_token_write = open('bot_token.tg','w+')
    bot_token_write.write(bot_input)
    bot_token_write.close()
bot = telebot.TeleBot(bot_input)

# =============================================================================
# Help menu
# =============================================================================
@bot.message_handler(commands=['start', 'help'])
def help_message(message):
    bot.send_message(message.from_user.id, '''
*PolyAlphabet Cipher is used to create ciphers based on several alphabets* 

Before beginning encoding/decoding you have to type `new_key`, to get unique key, that can be used for encoding/decoding. 
You have to save it and use it every time (it can be copied by clicking on it on the phone). Number of keys, that could be created is not limeted. 

*Usage*

`key` - start the program.
`0` - get to main menu.
`new_key` - get new key.

Also can be used commands with same names.
''', parse_mode='Markdown')

@bot.message_handler(commands=['new_key'])
def new_key(message):
    bot.send_message(message.from_user.id, 'Generated unique key: ' + "`" +  key_generator() + "`", parse_mode='Markdown')


# =============================================================================
# Encryption
# =============================================================================   
def encryption_func(message, key_read):
    text = message.text
    i = 1
    encoded = ''
    for letter in text:
        if i % 2 == 0:
            encoded += key_read[0][alphabet_0.index(letter)]
        elif i % 3 == 0:
            encoded += key_read[1][alphabet_0.index(letter)]
        elif i % 5 == 0: 
            encoded += key_read[2][alphabet_0.index(letter)]
        else:
            encoded += key_read[3][alphabet_0.index(letter)]
        i += 1
    bot.send_message(message.from_user.id, 'Encoded: ' + "`" +  encoded + "`", parse_mode='Markdown')

# =============================================================================
# Decryption
# =============================================================================
def decryption_func(message, key_read):
    text = message.text
    i = 1
    decoded = ''
    for letter in text:
        if i % 2 == 0:
            decoded += alphabet_0[key_read[0].index(letter)] 
        elif i % 3 == 0:
            decoded += alphabet_0[key_read[1].index(letter)]
        elif i % 5 == 0: 
            decoded += alphabet_0[key_read[2].index(letter)]
        else:
            decoded += alphabet_0[key_read[3].index(letter)]    
        i += 1
    bot.send_message(message.from_user.id, 'Decoded: ' + "`" +  decoded + "`", parse_mode='Markdown')
# =============================================================================
# Main menu
# =============================================================================
@bot.message_handler(content_types=['text'])
def main(message):
    text = message.text
    if text == 'new_key':       # new key generation using text command
        bot.send_message(message.from_user.id, 'Generated unique key: ' + "`" +  key_generator() + "`", parse_mode='Markdown')
    if text == 'key':
        bot.send_message(message.from_user.id, 'Enter the key', parse_mode='Markdown')
        bot.register_next_step_handler(message, key_choose)
    if text == '0':
        bot.send_message(message.from_user.id, 'You are in the main menu', parse_mode='Markdown')

# =============================================================================
# Key check and find
# =============================================================================
def key_choose(message):
    text = message.text
    for dirpath, dirnames, files in os.walk(os.path.abspath('keys/')):
        try: 
            files.index(text)
            bot.send_message(message.from_user.id, 'Key found')
            key_read = open('keys/' + text, 'r').readlines()
            bot.send_message(message.from_user.id, 'What you wanna to do? (Enter number) \n 1 - Encrypt \n 2 - Decrypt')
            bot.register_next_step_handler(message, message_work_with, key_read)
        except ValueError:
            bot.send_message(message.from_user.id, 'Key with this name doesn\'t exist')
            if text == '0':
                main(message)
            else:
                bot.send_message(message.from_user.id, 'Command is incorrect, please try again, or print 0 to get to main menu')
                bot.register_next_step_handler(message, key_choose)

# =============================================================================
# Text input
# =============================================================================
def message_work_with(message, key_read):
    text = message.text
    if text == '1':
        bot.send_message(message.from_user.id, 'Enter plaintext')
        bot.register_next_step_handler(message, encryption_func, key_read)
    elif text == '2':
        bot.send_message(message.from_user.id, 'Enter ciphertext')
        bot.register_next_step_handler(message, decryption_func, key_read)
    elif text == '0':
        main(message)
    else:
        bot.send_message(message.from_user.id, 'Command is incorrect, please try again, or print 0 to get to main menu')
        bot.register_next_step_handler(message, message_work_with, key_read)
bot.polling(none_stop=True, interval=0)
