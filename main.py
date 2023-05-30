# Group15_TripleThreat
# Main Home Screen

from colorama import init
from termcolor import colored

init()

print(colored("Cryptography", "white", "on_red"))
print("")
print(colored("Securing Data. Enter for your choice.", "red", "on_white"))
print("")
print(colored("1 - Text Encryption/Decryption", "red", "on_white"))
print("")
print(colored("2 - Image Encryption/Decryption", "red", "on_white"))


i = int(input())
if i == 1:
    import text_cryp
    # Calling the Text Encryption/Decryption file
elif i == 2:
    import image_interface 
    # Calling the main file for Image Encryption/Decryption file
else:
    print("Invalid Input")