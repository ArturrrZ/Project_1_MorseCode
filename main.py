#-----------------DATA--------------------
morce_code= {
        "A":	"*-",
        "B":	"-***",
        "C":	"-*-*",
        "D":	"-**",
        "E":	"*",
        "F":	"**-*",
        "G":	"--*",
        "H":	"****",
        "I":	"**",
        "J":	"*---",
        "K":	"-*-",
        "L":	"*-**",
        "M":	"--",
        "N":	"-*",
        "O":	"---",
        "P":	"*--*",
        "Q":	"--*-",
        "R":	"*-*",
        "S":	"***",
        "T":	"-",
        "U":	"**-",
        "V":	"***-",
        "W":	"*--",
        "X":	"-**-",
        "Y":	"-*--",
        "Z":	"--**",
        "1":	"*----",
        "2":	"**---",
        "3":	"***--",
        "4":	"****-",
        "5":	"*****",
        "6":	"-****",
        "7":	"--***",
        "8":	"---**",
        "9":	"----*",
        "0":	"-----",
# Special Characters
#         ' ': '/',  # Space
        '.': '.-.-.-',  # Period (Full Stop)
        ',': '--..--',  # Comma
        '?': '..--..',  # Question Mark
        '!': '-.-.--',  # Exclamation Mark
        '&': '.-...',  # Ampersand
        ':': '---...',  # Colon
        ';': '-.-.-.',  # Semicolon
        '=': '-...-',  # Equals Sign
        '+': '.-.-.',  # Plus Sign
        '-': '-....-',  # Hyphen (Minus Sign)
        '_': '..--.-',  # Underscore
        '"': '.-..-.',  # Quotation Mark
        '$': '...-..-',  # Dollar Sign
        '@': '.--.-.'  # At Sign

}
reverse_morce_code= {
    "*-":     "A",
    "-***":     "B",
    "-*-*":     "C",
    "-**":     "D",
    "*":     "E",
    "**-*":     "F",
    "--*":     "G",
    "****":     "H",
    "**":     "I",
    "*---":     "J",
    "-*-":     "K",
    "*-**":     "L",
    "--":     "M",
    "-*":     "N",
    "---":     "O",
    "*--*":     "P",
    "--*-":     "Q",
    "*-*":     "R",
    "***":     "S",
    "-":     "T",
    "**-":     "U",
    "***-":     "V",
    "*--":     "W",
    "-**-":     "X",
    "-*--":     "Y",
    "--**":     "Z",
    "*----":	"1",
    "**---":	"2",
    "***--":	"3",
    "****-":	"4",
    "*****":	"5",
    "-****":	"6",
    "--***":	"7",
    "---**":	"8",
    "----*":	"9",
    "-----":	"0",
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '-.-.--': '!',
    '.-...':  '&',
    '---...': ':',
    '-.-.-.': ';',
    '-...-':  '=',
    '.-.-.':  '+',
    '-....-': '-',
    '..--.-': '_',
    '.-..-.': '"',
    '...-..-':'$',
    '.--.-.':  '@',
}
#-----------------FUNCTIONS--------------------
def decode():
    text=input("Write a text that you want to convert to Morce Code(International format ITU):\n")
    converted_text=""
    converted_list=[]
    final_text_with_spaces=''
    for each in text:
        try:
            # print(morce_code[each.title()])
            converted_text += morce_code[each.title()]
            converted_list.append(morce_code[each.title()])
            final_text_with_spaces += morce_code[each.title()]  + " "
        except KeyError:

            converted_text += " "
            converted_list.append("")
            final_text_with_spaces += " "

    print(f"Final text is: \n{converted_text}\nAs list:\n{converted_list}")
    print(f"Text with spaces between each letter: {final_text_with_spaces}\nP.S. U can use this str to encode that again.")
    print("----------------------------------")
def endoce():
    morced_text = input('Give me your text in Morce Code Format(*-)\nDo not forget to use spaces:\n')
    requested_text = morced_text.split()
    # print(requested_text)
    und_text = ""
    for each_chunk in requested_text:
        try:
            letter = reverse_morce_code[each_chunk]
            und_text += letter
        except KeyError:
            und_text += " "
    print(f"Here is your answer: {und_text}")
    print("----------------------------------")

#-----------------main--------------------
end= False
print("Welcome to the Mose Code Generator.\nYou are able to decode or encode")
while not end:
    choice=input("Type 1 for encode or 2 for decode: ")
    print("--------------------------------------")
    if choice == "1":
        decode()
    elif choice == "2":
        endoce()
    else:
        print("Give me a proper answer!")
        pass
    finish=input("Do u wish to work with this model one more time?\n'Y' for one more or any character to stop:\n").title()
    if finish =='Y':
        pass
    else:
        print('Bye Bye!\nIt was nice to help you!')
        end=True

