import sys, re

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
    patterns = [
        r'^\d{10}$',    # 10-digit national format
        r'^\+\d{1,3}\d{4,14}$',     # International format with country code
        r'^\(\d{1,3}\)\d{6,12}$',       # Format with regional access code
        r'^\d{3}[-\s]\d{3}[-\s]\d{4}$'      # Format with spaces or dashes
    ]

    for pattern in patterns:
        if re.match(pattern, cleaned_number):
            return True
    return False



def format(number):
    """
    Number to a list of diferent formats of this number.
    ---
    EX:
        IN: "06 18 34 22 14"
        OUT: ["0618342214", "+33 6 18 34 22 14", "(06) 18 34 22 14", "06 18 34 22 14", "06-18-34-22-14"]
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

    numbers = [n, "+33"+n_space[1:],n_space,"("+n_space[0:2]+")"+n_space[2:],n_space.replace(" ","-")]
    return numbers


def analyse(number):
    number = format(number)
    print(number)

if __name__ == "__main__":
    a = len(sys.argv)
    if a == 1:
        number = gui()
     
    elif a == 2:
        number = sys.argv[1]
    else:
        print("\033[0;31mError: too many arguments\033[0m")
        exit()
    if is_valid(number):
        analyse(number)
    else:
        print("\033[0;31mError: invalid phone number\033[0m")
