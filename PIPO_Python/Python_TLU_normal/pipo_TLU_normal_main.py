from random import *
import time
import pipo_TLU_normal_256
import pipo_TLU_normal_128
import sys
from tkinter import *
from tkinter import filedialog
import binascii
import os
import math


class MyFrame(Frame):
    def __init__(self, master):
        img = PhotoImage(file=fname)
        lbl = Label(image=img)
        lbl.image = img  # 레퍼런스 추가
        lbl.place(x=0, y=0)


def main():
    TEST_SIZE = 1

    # ==== 128bit ====
    SIZE = 2
    MASTER_KEY_SIZE = 16

# PLAIN_TEXT

    #PLAIN_TEXT[0] = 0x1E270026
    #PLAIN_TEXT[1] = 0x098552F6

    # for i in range(0, SIZE):
    #    PLAIN_TEXT[i] = randint(0, 32767) | (randint(0, 32767) << 16)

# CIPHER_TEXT
    CIPHER_TEXT = [0, 0]

# MASTER_KEY
    MASTER_KEY = [0x97, 0x22, 0x15, 0x2E, 0xAD, 0x20, 0x1D,
                  0x7E, 0xD2, 0x28, 0x94, 0x77, 0xDD, 0x16, 0xC4, 0x6D]

    # MASTER_KEY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # for i in range(0, MASTER_KEY_SIZE):  # MASTER_KEY 생성
    #    MASTER_KEY[i] = randint(0, 255)

    root = Tk()

    # 이미지의 경우 보여주도록
    # root.title('이미지 보기')
    # root.geometry('500x400+10+10')
    # myframe = MyFrame(root)

    root.filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

    # 확장자 기억
    fname, ext = os.path.splitext(root.filename)
    fname = root.filename

    # 16진수로 바꿔줌
    with open(root.filename, mode='rb') as f:
        content = f.read()

    hexValue = binascii.hexlify(content).hex()

    # input 길이 구하기
    length = len(hexValue)
    TEST_SIZE = math.ceil(length/16)
    print(TEST_SIZE)
    #pad = length % 64
    # for i in range(pad):
    #    hexValue.append(0)
    # print(inSize)
    # print(hexValue[3398032])

    # 암호화
    # working

    for i in range(TEST_SIZE):
        PLAIN_TEXT = [0, 0]
        PLAIN_TEXT[0] = int(hexValue[16*i:16*(i+1)-1])
        PLAIN_TEXT[1] = int(hexValue[8+16*i:8+16*(i+1)-1])
        pipo_TLU_normal_128.ROUND_KEY_GEN(MASTER_KEY)
        PLAIN_TEXT = pipo_TLU_normal_128.ENC_TLU(PLAIN_TEXT, CIPHER_TEXT)
        # print(i)

    #root.title('이미지 보기')
    # root.geometry('500x400+10+10')
    #myframe = MyFrame(root)
    #binValue = binascii.unhexlify(hexValue)
    # with open('encryption'+ext, 'wb') as file:
    #    file.write(bytes(PLAIN_TEXT))

    for i in range(TEST_SIZE):
        pipo_TLU_normal_128.DEC_TLU(PLAIN_TEXT, CIPHER_TEXT)

    # 복호화해서 저장하는 코드
    #binValue = binascii.unhexlify(PLAIN_TEXT)
    # with open('decryption'+ext, 'wb') as file:
    #    file.write(binValue)


'''
# ==== 256bit ====
    SIZE = 2
    MASTER_KEY_SIZE = 32


# PLAIN_TEXT
    PLAIN_TEXT = [0, 0]
    PLAIN_TEXT[0] = 0x1E270026
    PLAIN_TEXT[1] = 0x098552F6

    # for i in range(0, SIZE):
    #    PLAIN_TEXT[i] = randint(0, 32767) | (randint(0, 32767) << 16)

# CIPHER_TEXT
    CIPHER_TEXT = [0, 0]


# MASTER_KEY
    MASTER_KEY = [0x97, 0x22, 0x15, 0x2E, 0xAD, 0x20, 0x1D, 0x7E, 0xD2, 0x28, 0x94, 0x77, 0xDD, 0x16, 0xC4, 0x6D,
                  0x33, 0x56, 0xD1, 0x26, 0x06, 0x12, 0xA7, 0x54, 0xB5, 0x6D, 0xA9, 0x76, 0xA4, 0x3A, 0x9A, 0x00]

    # MASTER_KEY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # for i in range(0, MASTER_KEY_SIZE):
    #    MASTER_KEY[i] = randint(0, 255)

# working
    for i in range(TEST_SIZE):
        pipo_TLU_normal_256.ROUND_KEY_GEN(MASTER_KEY)

    for i in range(TEST_SIZE):
        PLAIN_TEXT = pipo_TLU_normal_256.ENC_TLU(PLAIN_TEXT, CIPHER_TEXT)

    for i in range(TEST_SIZE):
        pipo_TLU_normal_256.DEC_TLU(PLAIN_TEXT, CIPHER_TEXT)
'''

if __name__ == '__main__':
    main()
