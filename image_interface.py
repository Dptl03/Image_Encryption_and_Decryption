# Group15_TripleThreat
# Home Screen for Image Encryption/Decryption

print("What do you wish to do?")
print("1 - Image Encryption ")
print("2 - Image Decryption")

j = int(input())
if j == 1:
    import image_encryption  
    # Calling the image Encryption file
elif j == 2:
    import image_decryption  
    # Calling the image Decryption file
else:
    print("Invalid Input")
