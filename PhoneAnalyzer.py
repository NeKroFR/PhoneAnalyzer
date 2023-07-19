import sys, re
from googlesearch import search

def gui():
    banner = """\033[92m
                                                                   
 _____  _                   _____            _                     
|  _  || |_  ___  ___  ___ |  _  | ___  ___ | | _ _  ___  ___  ___ 
|   __||   || . ||   || -_||     ||   || .'|| || | ||- _|| -_||  _|
|__|   |_|_||___||_|_||___||__|__||_|_||__,||_||_  ||___||___||_|  
                                               |___|               
"""
    print(banner)
    number = input("""\033[1;35mEnter the phone number to scan : \033[0m""")
    return number

def is_valid(phone_number):
    """
    verifie that the phone number is valid
    """
    cleaned_number = re.sub(r'\D', '', phone_number)
    if cleaned_number[0] != "0":
        cleaned_number = "0" + cleaned_number[2:]
    if len(cleaned_number) == 10:
            return True
    return False

def format(number):
    """
    Number to a list of diferent formats of this number.
    ---
    EX:
        IN: "0618342214"
        OUT: ['0618342214', '+33618342214', '(+33)6 18 34 22 14', '(06) 18 34 22 14', '06-18-34-22-14']
    """
    n = number.replace(" ", "")
    if n[0] == "+":
        n = "0"+n[3:]
    n_space =""
    space = 0
    for digit in n:
        if space == 2:
            space = 1
            n_space += " "+digit
        else:
            n_space += digit
            space += 1

    numbers = [n, "+33"+n[1:],"(+33)"+n_space[1:],"("+n_space[0:2]+")"+n_space[2:],n_space.replace(" ","-")]
    
    return numbers


def analyse(number):
    number = format(number)
    print(number)
    #need to google dork now

if __name__ == "__main__":
    if len(sys.argv) == 1:
        number = gui()
    else:
        number = "".join(sys.argv[1:])
    if is_valid(number):
        print("\033[92m Valid phone number\033[0m")
        analyse(number)
    else:
        print("\033[0;31mError: invalid phone number\033[0m")
        exit()

# add more formats -> https://sundowndev.github.io/phoneinfoga/resources/formatting/
# phoneinfoga doc: https://sundowndev.github.io/phoneinfoga/resources/additional-resources/
# doc: https://sundowndev.medium.com/phone-number-scanning-osint-recon-tool-6ad8f0cac27b
