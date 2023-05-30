# Group15_TripleThreat
# Image Decryption

import imageio
import numpy as np

def Decryption():
    Mod = 256
    print("Enter the path of image")                    
    # Input = Cipher Image
    enc=input()
    enc = imageio.imread(enc)
    A = imageio.imread('Key.png')

    # dimensions
    l = A[-1][0] * Mod + A[-1][1]
    w = A[-1][2] * Mod + A[-1][3]
    A = A[0:-1]

    #    We are using python inbuilt function.
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

    # decrypting for R-G-B components separately
    dec_color1_mod = enc[:,:,0] % Mod
    dec_color2_mod=enc[:,:,1] % Mod
    dec_color3_mod=enc[:,:,2] % Mod

    dec_color1 = (np.matmul(A % Mod,dec_color1_mod))
    dec_color1= dec_color1% Mod

    dec_color2 = (np.matmul(A % Mod,dec_color2_mod))
    dec_color2=dec_color2% Mod

    dec_color3 = (np.matmul(A % Mod,dec_color3_mod))
    dec_color3=dec_color3% Mod

    # Usage of np.resize is shown below
    # This is not part of main algorithm that includes ALA concepts

    dec_color1_shape=(dec_color1.shape[0],dec_color1.shape[1],1)
    dec_color2_shape=(dec_color2.shape[0],dec_color2.shape[1],1)
    dec_color3_shape=(dec_color3.shape[0],dec_color3.shape[1],1)

    dec_color1 = np.resize(dec_color1,(dec_color1_shape))
    dec_color2 = np.resize(dec_color2,(dec_color2_shape))
    dec_color3 = np.resize(dec_color3,(dec_color3_shape))

    # combining R-G-B components
    decrypt_full = np.concatenate((dec_color1,dec_color2,dec_color3), axis = 2)

    final = decrypt_full[:l,:w,:]

    imageio.imwrite('Decrypted.png',final)

    print("Image decrypted successfully!!")

Decryption()
