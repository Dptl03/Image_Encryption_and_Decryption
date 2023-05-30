# Text Encryption and Decryption
import numpy as np       
import sympy               
from sympy import Matrix
# Encryption Function
def encrypt(s, password):
    n = len(s)
    # Generate plain text matrix
    plainText = np.arange(n).reshape(n, 1)
    for i in range(0, n):
        plainText[i][0] = ord(s[i]) - ord('a')

    # Generate key matrix
    key = np.arange(n * n).reshape(n, n)
    for i in range(0, n):
        for j in range(0, n):
            key[i][j] = ord(password[(n * i) + j]) - ord('a')

    # Encrypted matrix
    encryText = key.dot(plainText)

    # Generate encrypted string
    ans = ""
    for i in range(0, n):
        ans += chr((encryText[i][0] % 26) + ord('a'))

    return ans


# Decryption Function
def decrypt(s, password):
    n = len(s)

    # Generate encrypted matrix
    encryText = np.arange(n).reshape(n, 1)
    for i in range(0, n):
        encryText[i][0] = ord(s[i]) - ord('a')

    # Generate key matrix
    key = np.arange(n * n).reshape(n, n)
    for i in range(0, n):
        for j in range(0, n):
            key[i][j] = ord(password[(n * i) + j]) - ord('a')

    # Inverse key matrix to invKey (for generating decryption key)
    def inv_mod(a, m):
        a = a % m
        for x in range(1, m):
            if ((a * x) % m == 1):
                return x
        return 1

    invKey = Matrix(key).inv_mod(26)
    np.invKey = np.array(invKey)
    plainText = invKey * encryText

    # generate plaintext string
    ans = ""
    for i in range(0, n):
        ans += chr((plainText[i] % 26) + ord('a'))

    return ans


# get choice
print("Enter 1 for encryption")
print("Enter 2 for decryption")
a = int(input())

if (a == 1):
    # Encryption BEGINS
    print("Enter string for encryption(lowercase alphabets):")
    s = str(input())                          
    #String to be encrypted
    n = len(s)

    #Key/Password
    print("Password should be " + str(n * n) + " letters long")
    print("Enter password (lowercase alphabets): ")                 
    password = str(input())

    #Password Validation
    if (len(password) != n * n):
        print("Invalid length of string/password.")           
         #Error if password is not n*n letter long
        print("Password should be " + str(n * n) + " letters long")

    else:
        encrypted_string = encrypt(s, password)                
        #Calling the function to perform encryption
        print("The encrypted string is: " + encrypted_string)

if (a == 2):
    # Decryption BEGINS
    print("Enter string for decryption:")                      
    #String to be decrypted
    s = str(input())
    n = len(s)

    #Key/Password
    print("Enter password: ")                                 
    password = str(input())

    #Password Validation
    if (len(password) != n * n):
        print("Invalid length of string. Please try again")      
        #Error if password is not n*n letter long

    else:
        decrypted_string = decrypt(s, password)                 
        #Calling the function to perform decryption
        print("The decrypted string is " + decrypted_string)

# plaintext: ACT
# key: GYBNQKURP