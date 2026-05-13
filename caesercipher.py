logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
directions = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = (input("Type your message: \n")).lower()
shift = int(input("Type the shift number: "))


def caeser_cipher(original_text, shift_count, encode_or_decode):
    caeser_cipher = " "
    for letter in original_text:


        if letter not in alphabets:
            caeser_cipher += letter
        else:
            if letter in alphabets:                                        # even this below logic can be used for this function
                if encode_or_decode == "encode":                         # if the user wants to decode the message
                    new_position = alphabets.index(letter) + shift_count #here shiftcount *= -1 can also be taken
                else:
                    new_position = alphabets.index(letter) - shift_count # here the sign of the shift count will be changed to positve
                new_position %= len(alphabets)
                caeser_cipher += alphabets[new_position]
    print(f"here the {encode_or_decode}d result is : \n{caeser_cipher}")
caeser_cipher(original_text = text, shift_count = shift, encode_or_decode = directions)

should_repeat = True

while should_repeat:
        user_choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if user_choice == "yes":
            
            directions = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
            text = (input("Type your message: \n")).lower()
            shift = int(input("Type the shift number: "))
            caeser_cipher(original_text = text, shift_count = shift, encode_or_decode = directions)
        else:
            should_repeat = False
            print("Hope you enjoyed the cipher. See you later!")





