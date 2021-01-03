# New keys generator
import uuid
import random


alphabet_1 = []
alphabet_2 = []
alphabet_3 = []
alphabet_4 = []

def key_generator():
    alphabet_key = str(uuid.uuid4())
    key_stor = open('keys/' + alphabet_key, 'w+').close()
    
    i = 0
    while i < 100:
        lettr_1 = chr(random.randint(200,300))
        try:
            while alphabet_1.index(lettr_1) != ValueError: 
                lettr_1 = chr(random.randint(200,300))
        except ValueError:
            alphabet_1.append(lettr_1)
        
        lettr_2 = chr(random.randint(301,401))
        
        try:
            while alphabet_2.index(lettr_2) != ValueError: 
                lettr_2 = chr(random.randint(301,401))
        except ValueError:
            alphabet_2.append(lettr_2)
        
        lettr_3 = chr(random.randint(402,502))
        
        try:
            while alphabet_3.index(lettr_3) != ValueError: 
                lettr_3 = chr(random.randint(402,502))
        except ValueError:
            alphabet_3.append(lettr_3)
        
        lettr_4 = chr(random.randint(503,603))
        
        try:
            while alphabet_4.index(lettr_4) != ValueError: 
                lettr_4 = chr(random.randint(503,603))
        except ValueError:
            alphabet_4.append(lettr_4)
        i += 1
        
    key_stor = open('keys/' + alphabet_key, 'a')
    key_stor.writelines(alphabet_1)
    key_stor.write('\n')
    key_stor.writelines(alphabet_2)
    key_stor.write('\n')
    key_stor.writelines(alphabet_3)
    key_stor.write('\n')
    key_stor.writelines(alphabet_4)
    key_stor.write('\n')
    key_stor.close()
    
    print('Generated unique key: ' + alphabet_key)
    return alphabet_key