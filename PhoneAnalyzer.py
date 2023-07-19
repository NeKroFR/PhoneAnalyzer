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
    #optimize search requests + patch error
    numbers = format(number)
    results = []
    print("\033[1;35mDigging information from the internet...\033[0m")
    for num in numbers:
        request = search(num)
        for result in request:
            if not result in results:
                results.append(result)
    print("\033[92m"+len(results)+" results found!\033[0m")
    for i in range(len(results)):
        print(i+1,results[i])
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        number = gui()
    else:
        number = "".join(sys.argv[1:])
    if is_valid(number):
        print("\033[92mValid phone number\033[0m")
        analyse(number)
    else:
        print("\033[0;31mError: invalid phone number\033[0m")
        exit()
