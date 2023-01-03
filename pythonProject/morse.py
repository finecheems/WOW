# coding=utf-8
MORSE_0= {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
        '.': '.-.-.-', '/': '-..-.',  '?': '..--..',
        '@': '.--.-.', ',': '--..--', '\"': '.-..-.',
        '!': '-.-.--', ':':'---...',  '=':'-...-',
        '\'':'.----.', '-':'-....-',  '_':'..--.-',
        '(':'-.--.',   ')':'-.--.-',  '+':'.-.-.'
        }
morse_1= {v: k for k, v in MORSE_0.items()}
def translation_0(x): #英转码
    for items in x:
        if items == ' ':
            print(" ",end='') 
        M=''
        if items==' ':
            continue
        M =MORSE_0[items.upper()]
        print(M,end=' ')
def translation_1(y):#码转英
    y+=' '
    d=''
    l=[]
    for thing in y:
        if thing !=' ':
           d+=thing
           continue
        else:
            if d!=' ':
                l.append(d)
                d=''
                continue  
    return l
def main():
    return input("\n翻译开始,请输入解密电码or加密信息以进入相应系统\n")
while True:
    keyboard_input= main()
    if keyboard_input == "加密信息":
        keya=input('输入信息:')
        translation_0(keya)
    elif keyboard_input == "解密电码":
        keyb=input('输入电码:')
        i=translation_1(keyb)
        for n in i:
             if n =='':
                print(' ',end="")
                continue
             else:
                print(morse_1[n],end="")
    else:
        print("格式错误，程序结束")
        break
    

