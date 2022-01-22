# 나중에 이거 빼기
import sys
sys.path.insert(0, 'C:/Users/dnjsd/OneDrive/Desktop/PIPO_Python/Python_bitslice_fast')

from random import *
import time
import pipo_bitslice_fast_128
import pipo_bitslice_fast_256


def main():
    TEST_SIZE = 100000

# ==== 128bit ====
    SIZE = 2
    MASTER_KEY_SIZE = 16

# PLAIN_TEXT
    PLAIN_TEXT = [0, 0]
    PLAIN_TEXT[0] = 0x1E270026
    PLAIN_TEXT[1] = 0x098552F6

    # for i in range(0, SIZE):
    #    PLAIN_TEXT[i] = randint(0, 32767) | (randint(0, 32767) << 16)

# CIPHER_TEXT
    CIPHER_TEXT = [0, 0, 0, 0, 0, 0, 0, 0]

# MASTER_KEY
    MASTER_KEY = [0x97, 0x22, 0x15, 0x2E, 0xAD, 0x20, 0x1D,
                  0x7E, 0xD2, 0x28, 0x94, 0x77, 0xDD, 0x16, 0xC4, 0x6D]

    # MASTER_KEY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # for i in range(0, MASTER_KEY_SIZE):  # MASTER_KEY 생성
    #    MASTER_KEY[i] = randint(0, 255)

# working
    key_time = 0
    enc_time = 0
    dec_time = 0
    
    
    start_time = time.time() # 시작 시간
    for i in range(TEST_SIZE):
        pipo_bitslice_fast_128.ROUND_KEY_GEN(MASTER_KEY)
    end_time = time.time() # 종료 시간
    key_time += end_time - start_time
        
    start_time = time.time()  # 시작 시간
    for i in range(TEST_SIZE):
        PLAIN_TEXT = pipo_bitslice_fast_128.ENC(PLAIN_TEXT, CIPHER_TEXT)
    end_time = time.time()  # 종료 시간
    enc_time += end_time - start_time
        
    
    start_time = time.time()  # 시작 시간
    for i in range(TEST_SIZE):
        pipo_bitslice_fast_128.DEC(PLAIN_TEXT, CIPHER_TEXT)
    end_time = time.time()  # 종료 시간
    dec_time += end_time - start_time
        
    print("key_bitslice_fast_128: {} sec".format(key_time/TEST_SIZE))
    print("enc_bitslice_fast_128: {} sec".format(enc_time/TEST_SIZE))
    print("dec_bitslice_fast_128: {} sec".format(dec_time/TEST_SIZE))
    print("")

# ==== 256bit ====
    SIZE = 2
    MASTER_KEY_SIZE = 32


# PLAIN_TEXT
    PLAIN_TEXT = [0, 0]
    PLAIN_TEXT[0] = 0x1E270026
    PLAIN_TEXT[1] = 0x098552F6

    # for i in range(0, SIZE):
    #    PLAIN_TEXT[i] = randint(0, 32767) | (randint(0, 32767) << 16)

# CIPHER_TEXT|
    CIPHER_TEXT = [0, 0, 0, 0, 0, 0, 0, 0]

# MASTER_KEY

    MASTER_KEY = [0x97, 0x22, 0x15, 0x2E, 0xAD, 0x20, 0x1D, 0x7E, 0xD2, 0x28, 0x94, 0x77, 0xDD, 0x16, 0xC4, 0x6D,
                  0x33, 0x56, 0xD1, 0x26, 0x06, 0x12, 0xA7, 0x54, 0xB5, 0x6D, 0xA9, 0x76, 0xA4, 0x3A, 0x9A, 0x00]

    # MASTER_KEY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # for i in range(0, MASTER_KEY_SIZE):
    #    MASTER_KEY[i] = randint(0, 255)

# working
    key_time = 0
    enc_time = 0
    dec_time = 0

    start_time = time.time() # 시작 시간
    for i in range(TEST_SIZE):
        pipo_bitslice_fast_256.ROUND_KEY_GEN(MASTER_KEY)
    end_time = time.time() # 종료 시간
    key_time += end_time - start_time
        
    start_time = time.time()  # 시작 시간
    for i in range(TEST_SIZE):
        PLAIN_TEXT = pipo_bitslice_fast_256.ENC(PLAIN_TEXT, CIPHER_TEXT)
    end_time = time.time()  # 종료 시간
    enc_time += end_time - start_time
        
    
    start_time = time.time()  # 시작 시간
    for i in range(TEST_SIZE):
        pipo_bitslice_fast_256.DEC(PLAIN_TEXT, CIPHER_TEXT)
    end_time = time.time()  # 종료 시간
    dec_time += end_time - start_time

    print("key_bitslice_fast_256: {} sec".format(key_time/TEST_SIZE))
    print("enc_bitslice_fast_256: {} sec".format(enc_time/TEST_SIZE))
    print("dec_bitslice_fast_256: {} sec".format(dec_time/TEST_SIZE))


if __name__ == '__main__':
    main()
