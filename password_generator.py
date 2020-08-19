import random
import string
import hashlib
import string
import secrets
import termcolor
def pass_gen(option,length) :
    secretsGenerator = secrets.SystemRandom()
    if length < 5 :
        print("/!\ : Weak password !")
    if option == 'A' :
        if length%2 == 1 :
            length = length//2
            length2 =length
        if length%2 == 0 :
            length = length//2
            length2 = length - 1
        gen_pass = str(secretsGenerator.randint(0,50))
        gen_pass =  gen_pass.encode()
        hash = hashlib.sha1(gen_pass)
        gen_hash = hash.hexdigest()
        a = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(length))
        b = ''.join(secrets.choice(gen_hash)for liste_gen_hash in range(length2))
        end = a + b + '$'
        return end
    if option == 'B' :
        string_pass = ''.join(secrets.choice(string.ascii_uppercase) for i in range(length))
        return string_pass
    if option == 'C' :
        num_pass = ''.join(str(secretsGenerator.randint(0,9))for i in range(length))
        return num_pass
print(termcolor.colored("__________                                 _______" ,'green'))
print(termcolor.colored("\______   \____    ______ ______          /  _____/  ____   ____",'green'))
print(termcolor.colored("|     ___/\__  \  /  ___//  ___/  ______ /   \  ____/ __ \ /    \ ",'green'))
print(termcolor.colored("|    |     / __ \_\___ \ \___ \  /_____/ \    \_\  \  ___/|   |  \ ",'green'))
print(termcolor.colored("|____|    (____  /____  >____  >          \______  /\___  >___|  /",'green'))
print(termcolor.colored("               \/     \/     \/                  \/     \/     \/ ",'green'))
print('By 0xE')
print(termcolor.colored('=================================================================','red'))
print('A : All (number, letter, special)')
print('B : only letter')
print('C : only number')
print(termcolor.colored('=================================================================','red'))
choice_option = input("Choose option :")
choice_length = int(input("Choose password length :"))
choice_option = choice_option.upper()
print(pass_gen(choice_option , choice_length))
