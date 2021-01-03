# Polyalphabetic encoding/decoding
Polyalphabetic encoding/decoding for Telegram, using PyTelegramBotApi

This bot can be used to encode and decode polyalphabetic ciphers in English (other languages will be added latter) for Telegram. 

### Installation and run
Using console:
```
git clone https://github.com/Antcating/polyalphabetic_cipher_bot.git
cd polyalphabetic_cipher_bot
python3 poly_main.py
```

### Config

#### Initial Config
On the first run of the bot you will be asked to input Bot Token of your bot, that you can get from [@BotFather](t.me/BotFather). The token will be saved to config file and after that you won't be asked to input it again. Initial configuration is over. 
Addiction information about Bot API and etc. can be found on the main page of the [PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI). 

#### In-bot config 

Before beginning encoding/decoding you have to type *new_key*, to get unique key, that can be used for encoding/decoding. 
You have to save it and use it every time (it can be copied by clicking on it on the phone). Number of keys, that could be created is not limited. 

Usage

*key* - start the program.\
*0* - get to main menu.\
*new_key* - get new key.\

Also can be used commands with same names.

For each user can be created own config. 
All configs are saving, so after reboot the settings will not be reset.

### Additional information 

Repository contains simple bash file to restart bot, if will be some problems, so that you can run it and forget about it. Bot will automatically run in the background.

### Related projects and thanks 
- [PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) – telegram bot interaction.