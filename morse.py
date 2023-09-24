txt = ("THE MORSE CODE CONVERTER")
new_str=txt.center(20)
print(new_str)
lst=[]

print("Feel free to use alphanumeric texts but dont use and special characters \nYou can use ',' '.' '?' '/' '-' '()' ':'")
text = input("Enter Your text here: ")

morse_dict={ 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',' ':' '}

upper = text.upper()
print(*upper)

for letter in upper:
    if letter == ' ':
        continue
    else: 
        lst.append(letter)
mlist = []
for char in lst:
    mlist.append(morse_dict[char])
final = " ".join(mlist)
print(final)


    
    



    
    
    
