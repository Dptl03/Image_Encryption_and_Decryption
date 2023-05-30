# Group15_TripleThreat
# Image Encryption

import imageio
import numpy as np

def Encryption():

    print("Enter the path of image")        
    #Taking the image from the user
    img = input()
    img = imageio.imread(img)
    #imread: reads the image from the specified file and returns in a numpy array with metadata

    l = img.shape[0]                        
    #judging the number of rows and columns in the image
    w = img.shape[1]
    n = max(l, w)

    #checking if the image is square or not
    if n % 2:
        n = n + 1

    # Making the picture to have square dimensions
    img2 = np.zeros((n, n, 3))
    img2[:l, :w, :] += img
    # Image is ready for encyption

    # Generating the key for encrytion
    Mod = 256 # Judging the colour composition
    k = 23  # Key for Encryption

    d = np.random.randint(256, size=(int(n / 2), int(n / 2)))  
    # Arbitrary Matrix, should be saved as Key also
    u = int(n / 2)

    def identity(a):  
        # a is the dimension of the matrix required
        id = []
        k = 0
        for i in range(0, a):
            temp = []
            for j in range(0, a):
                if (j == k):
                    temp.append(1)
                else:
                    temp.append(0)
            id.append(temp)
            k = k + 1
        return id

    #Generating an involutory matrix for key
    I = identity(u)                     
    a = np.mod(-d, Mod)

    b = (k * ((I - a) % Mod))
    b = b%Mod

    k = (k**127)
    k = k%Mod

    c = (I + a) % Mod
    c = (c * k) % Mod

    A1 = np.concatenate((a, b), axis=1)
    A2 = np.concatenate((c, d), axis=1)
    A = np.concatenate((A1, A2), axis=0)

    Test = np.matmul(A % Mod, A % Mod) % Mod  
    # making sure that A is an involutory matrix, A*A = I

    # Saving key as an image
    key = np.zeros((n + 1, n))
    key[:n, :n] += A
    # Adding the dimension of the original image within the key
    # Elements of the matrix should be below 256
    key[-1][0] = int(l / Mod)
    key[-1][1] = l % Mod
    key[-1][2] = int(w / Mod)
    key[-1][3] = w % Mod

    imageio.imwrite("Key.png", key)

# ENCRYPTION:
    #    We are using np.matmul function.
    #    Our algorithm is correct as shown in below code.
    #    But was time complex ( with the complexity of O(n^3).
    #    Hence, was running slow.

    # def multiply_mat(a,b):
    #     n=len(a)
    #     m=len(b[0])
    #     ans=zeroes(n,m)
    #     for i in range(0,n):
    #          for j in range(0,m):
    #             for k in range(0,len(b)):
    #                 ans[i][j] += a[i][k] * b[k][j]
    #     return ans

    # Apply the algorithm to R-G-B components separately

    enc_color1 = (np.matmul(A % Mod, img2[:, :, 0] % Mod))
    enc_color1 =  enc_color1 % Mod

    enc_color2 = (np.matmul(A % Mod, img2[:, :, 1] % Mod))
    enc_color2 = enc_color2 % Mod

    enc_color3 = (np.matmul(A % Mod, img2[:, :, 2] % Mod))
    enc_color3 = enc_color3 % Mod

    # Usage of np.resize is shown below
    # This is not part of main algorithm that includes ALA concepts

    enc_color1_shape = (enc_color1.shape[0], enc_color1.shape[1], 1)
    enc_color2_shape = (enc_color2.shape[0], enc_color2.shape[1], 1)
    enc_color3_shape = (enc_color3.shape[0], enc_color3.shape[1], 1)

    enc_color1 = np.resize(enc_color1,(enc_color1_shape) )
    enc_color2 = np.resize(enc_color2,(enc_color2_shape) )
    enc_color3 = np.resize(enc_color3,( enc_color3_shape) )

    # Enc = A * image  #combining the R-G-B components
    encrypt_full = np.concatenate((enc_color1, enc_color2, enc_color3), axis=2)

    imageio.imwrite('Encrypted.png', encrypt_full)
    print("Image encrypted successfully !!")

Encryption()