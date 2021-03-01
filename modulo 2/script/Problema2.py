import string

ALFAFETO = string.ascii_lowercase
print(ALFAFETO)

plaintext = input('Introduzaca texto a cifrar: ')
print(plaintext)

k = int(input('Introduzca k: '))
print(k)

ciphertext = ''
for l in plaintext:
    
    if l.lower() in ALFAFETO:
        p = ALFAFETO.find(l.lower())
        c = (p + k) % 26
        
        if l.isupper():
            ciphertext += ciphertext.join(ALFAFETO[c].upper())
        else: 
            ciphertext += ciphertext.join(ALFAFETO[c])
    else:
        ciphertext +=  ciphertext.join(l)
print(ciphertext) 
        