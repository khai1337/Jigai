import os
import webbrowser
from winotify import Notification, audio
from win10toast import ToastNotifier
from colorama import Fore
from time import sleep

os.system("title [Jigai v2.0] ^| By alight")

def logo():
    input(f"""{Fore.CYAN}
 ╦ ╦ ╔═╗ ╔═╗ ╦
 {Fore.LIGHTBLACK_EX}║ ║ ║ ╦ ╠═╣ ║{Fore.RESET}
╚╝ ╩ ╚═╝ ╩ ╩ ╩    v3.0
{Fore.CYAN}[{Fore.RESET}Recommend using it with tools like sherlock.{Fore.CYAN}]{Fore.RESET}

{Fore.CYAN}[{Fore.RESET}1{Fore.CYAN}]{Fore.RESET} Name
{Fore.CYAN}[{Fore.RESET}2{Fore.CYAN}]{Fore.RESET} IP
{Fore.CYAN}[{Fore.RESET}3{Fore.CYAN}]{Fore.RESET} Phone Number
{Fore.CYAN}[{Fore.RESET}4{Fore.CYAN}]{Fore.RESET} Discord
{Fore.CYAN}[{Fore.RESET}5{Fore.CYAN}]{Fore.RESET} Address
{Fore.CYAN}[{Fore.RESET}6{Fore.CYAN}]{Fore.RESET} Credits 
{Fore.CYAN}[{Fore.RESET}7{Fore.CYAN}]{Fore.RESET} Full Dox

{Fore.CYAN}[{Fore.RESET}Press enter to continue{Fore.CYAN}]{Fore.RESET}: """)
logo()

skid = input(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Skid you're doxxing: ")
choice = input(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Choice: ")


def Name():
    surname = input(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} SurName: ")
    firstname = input(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} FirstName: ")
    webbrowser.open(f"https://www.peekyou.com/{surname}_{firstname}")
    webbrowser.open(f"https://www.whitepages.com/name/{surname}-{firstname}")
    print(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Closing in 5 Seconds")
    sleep(5)
    os._exit(0)

if choice == "1":
    Name()

def IP():
    ip = input(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} IP: ")
    webbrowser.open(f"http://whatismyipaddress.com/ip/{ip}")
    sleep(3)
    webbrowser.open(f"https://www.ip-tracker.org/locator/-lookup.php?ip={ip}")
    print(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Closing in 5 Seconds")
    sleep(5)
    os._exit(0)

if choice == "2":
    IP()
 

if choice == "3":
    phoneno = input(
    f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Phone: ")
    phone = input(
        f"""
        \n
        {Fore.CYAN}[{Fore.RESET}1{Fore.CYAN}]{Fore.RESET}  OkCaller
        {Fore.CYAN}[{Fore.RESET}2{Fore.CYAN}]{Fore.RESET}  Facebook
        {Fore.CYAN}[{Fore.RESET}3{Fore.CYAN}]{Fore.RESET}  WhitePages
        {Fore.CYAN}[{Fore.RESET}4{Fore.CYAN}]{Fore.RESET}  AnyWho
        {Fore.CYAN}[{Fore.RESET}5{Fore.CYAN}]{Fore.RESET}  PagesJuanes
        {Fore.CYAN}[{Fore.RESET}6{Fore.CYAN}]{Fore.RESET}  All\n\n  {Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Choice: """)
    if phone == "1":
        webbrowser.open(f"http://www.okcaller.com/{phoneno}")
        print(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Closing in 5 Seconds")
        sleep(5)
        os._exit(0)
    if phone == "2":
        webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={phoneno}")
        print(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Closing in 5 Seconds")
        sleep(5)
        os._exit(0)
    if phone == "3":
        webbrowser.open(f"https://www.whitepages.com/phone/{phoneno}")
        print(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Closing in 5 Seconds")
        sleep(5)
        os._exit(0)
    if phone == "4":
        webbrowser.open(f"https://www.anywho.com/phone/{phoneno}")
        print(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Closing in 5 Seconds")
        sleep(5)
        os._exit(0)
    if phone == "5":
        webbrowser.open(f"https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui={phoneno}")
        print(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Closing in 5 Seconds")
        sleep(5)
        os._exit(0)
    if phone == "6":
        webbrowser.open(f"http://www.okcaller.com/{phoneno}")
        sleep(3)
        webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={phoneno}")
        sleep(3)
        webbrowser.open(f"https://www.whitepages.com/phone/{phoneno}")
        sleep(3)
        webbrowser.open(f"https://www.anywho.com/phone/{phoneno}")
        sleep(3)
        webbrowser.open(f"https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui={phoneno}")
        print(f"\n{Fore.CYAN}[{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Closing in 5 Seconds")
        sleep(5)
        os._exit(0)

def Discord():
    id = input(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Discord ID: ")
    webbrowser.open(f"https://lookup.guru/{id}")
    print(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Closing in 5 Seconds")
    sleep(5)
    os._exit(0)

    
if choice == "4":
    Discord()

def Address():
    latitude = input(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Latitude: ")
    longtitude = input(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Longtitude: ")
    webbrowser.open(f"https://www.google.com/maps/place/{latitude}+{longtitude}/")
    print(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Closing in 5 Seconds")
    sleep(5)
    os._exit(0)

if choice == "5":
    Address()

def credits():
    webbrowser.open("https://github.com/khai2rich")
    webbrowser.open("https://t.me/shriveliong")
    print(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Closing in 5 Seconds")
    sleep(5)
    os._exit(0)

if choice == "6":
    credits()

def Full():
    surname = input(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} SurName: ")
    firstname = input(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} FirstName: ")
    webbrowser.open(f"https://www.peekyou.com/{surname}_{firstname}")

    #Intermission

    ip = input(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} IP: ")
    webbrowser.open(f"http://whatismyipaddress.com/ip/{ip}")

    #Intermission

    phoneno = input(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Phone No: ")
    webbrowser.open(f"http://www.okcaller.com/{phoneno}")
    sleep(3)
    webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={phoneno}")
    sleep(3)
    webbrowser.open(f"https://www.whitepages.com/phone/{phoneno}")
    sleep(3)
    webbrowser.open(f"https://www.anywho.com/phone/{phoneno}")
    sleep(3)
    webbrowser.open(f"https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui={phoneno}")

    #Intermission

    latitude = input(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Latitude: ")
    longtitude = input(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Longtitude: ")
    webbrowser.open(f"https://www.google.com/maps/place/{latitude}+{longtitude}/")
    print(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Pulled a Dox on {skid} - khai runs you")
    sleep(2)
    print(f"\n{Fore.CYAN}> [{Fore.RESET}>>>{Fore.CYAN}]{Fore.RESET} Closing in 5 Seconds")
    sleep(5)
    os._exit(0)

if choice == "7":
    Full()
