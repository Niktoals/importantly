import os
import argparse
from random import *
from Data import DataBase

def get_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("-w", "--write", dest="key", help="service of service")
    parser.add_argument("-sh", "--show", dest="show", help="service of service")
    parser.add_argument("-d", "--delete", dest="delete", help="service of service")
    options=parser.parse_args()
    return options

def show_key(service):
    try:
        print(f"Your pasasword for '{service}' is /// {db.show_key(service)[0]} ///")
    except:
        print("no such service")
        
def generate():
    ls_of_symbols=input("Input what symbols you want to use:\nsp-special symbols\nul-up letters\nll-lower letters\nd-digits\nFor example format is: sp d\n").split()
    lenn=input('Input length of passwd: ')
    special_symbols='~!@#$%^&*-+=|\<>,.?/'
    up_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters='abcdefghijklmnopqrstuvwxyz'
    digits='0123456789'
    alf=''
    passwd=''
    try:
        for s in ls_of_symbols:
            if s=="sp":
                alf+=special_symbols
            if s=="ul":
                alf+=up_letters
            if s=="ll":
                alf+=lower_letters
            if s=="d":
                alf+=digits
        for _ in range(int(lenn)):
            passwd+=choice(alf)
        print("Your password was generated successfuly")
    except:
        print("Sorry, we can't generate password, check your input data")
    return passwd

def change(service):
    ok=input('Do you want to chage key for this service?\n[y/n]')
    if ok.lower()=='y':
        key=generate()
        try:
            db.change_key(service, key)
            print(f"Your pasasword for '{service}' was changed on /// {key} ///")
        except:
            print("Changing failed")

def write(service):
    try:
        if db.service_exists(service):
            print(f"You have already have password for login '{service}':\n/// {db.show_key(service)[0]} ///")
            change(service)
        else:
            key=generate()
            db.insert_key(service, key)
            print(f"Your pasasword for '{service}' is /// {key} ///")
    except Exception as e:
        print(e)

            
if __name__ == "__main__":
    db=DataBase("data_pswd.db")
    schoice=get_args()
    try:
        if schoice.key != None:
            write(schoice.key)
        if schoice.show != None:
            show_key(schoice.show)
        if schoice.delete != None:
            db.delete_service(schoice.delete)
        print("Well done!")
    except:
        print("Something gone wrong")
        