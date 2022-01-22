Sbox = [0x5E, 0xF9, 0xFC, 0x00, 0x3F, 0x85, 0xBA, 0x5B, 0x18, 0x37, 0xB2, 0xC6, 0x71, 0xC3, 0x74, 0x9D, 0xA7, 0x94, 0x0D, 0xE1, 0xCA, 0x68, 0x53, 0x2E, 0x49, 0x62, 0xEB, 0x97, 0xA4, 0x0E, 0x2D, 0xD0, 0x16, 0x25, 0xAC, 0x48, 0x63, 0xD1, 0xEA, 0x8F, 0xF7, 0x40, 0x45, 0xB1, 0x9E, 0x34, 0x1B, 0xF2, 0xB9, 0x86, 0x03, 0x7F, 0xD8, 0x7A, 0xDD, 0x3C, 0xE0, 0xCB, 0x52, 0x26, 0x15, 0xAF, 0x8C, 0x69, 0xC2, 0x75, 0x70, 0x1C, 0x33, 0x99, 0xB6, 0xC7, 0x04, 0x3B, 0xBE, 0x5A, 0xFD, 0x5F, 0xF8, 0x81, 0x93, 0xA0, 0x29, 0x4D, 0x66, 0xD4, 0xEF, 0x0A, 0xE5, 0xCE, 0x57, 0xA3, 0x90, 0x2A, 0x09, 0x6C, 0x22, 0x11, 0x88, 0xE4, 0xCF, 0x6D, 0x56, 0xAB, 0x7B, 0xDC, 0xD9, 0xBD, 0x82, 0x38, 0x07, 0x7E, 0xB5, 0x9A, 0x1F, 0xF3, 0x44, 0xF6, 0x41, 0x30, 0x4C, 0x67, 0xEE, 0x12, 0x21, 0x8B, 0xA8,
        0xD5, 0x55, 0x6E, 0xE7, 0x0B, 0x28, 0x92, 0xA1, 0xCC, 0x2B, 0x08, 0x91, 0xED, 0xD6, 0x64, 0x4F, 0xA2, 0xBC, 0x83, 0x06, 0xFA, 0x5D, 0xFF, 0x58, 0x39, 0x72, 0xC5, 0xC0, 0xB4, 0x9B, 0x31, 0x1E, 0x77, 0x01, 0x3E, 0xBB, 0xDF, 0x78, 0xDA, 0x7D, 0x84, 0x50, 0x6B, 0xE2, 0x8E, 0xAD, 0x17, 0x24, 0xC9, 0xAE, 0x8D, 0x14, 0xE8, 0xD3, 0x61, 0x4A, 0x27, 0x47, 0xF0, 0xF5, 0x19, 0x36, 0x9C, 0xB3, 0x42, 0x1D, 0x32, 0xB7, 0x43, 0xF4, 0x46, 0xF1, 0x98, 0xEC, 0xD7, 0x4E, 0xAA, 0x89, 0x23, 0x10, 0x65, 0x8A, 0xA9, 0x20, 0x54, 0x6F, 0xCD, 0xE6, 0x13, 0xDB, 0x7C, 0x79, 0x05, 0x3A, 0x80, 0xBF, 0xDE, 0xE9, 0xD2, 0x4B, 0x2F, 0x0C, 0xA6, 0x95, 0x60, 0x0F, 0x2C, 0xA5, 0x51, 0x6A, 0xC8, 0xE3, 0x96, 0xB0, 0x9F, 0x1A, 0x76, 0xC1, 0x73, 0xC4, 0x35, 0xFE, 0x59, 0x5C, 0xB8, 0x87, 0x3D, 0x02, 0xFB]
Sbox_inv = [0x03, 0xA0, 0xFE, 0x32, 0x48, 0xDB, 0x92, 0x6E, 0x89, 0x5E, 0x57, 0x83, 0xE4, 0x12, 0x1D, 0xE8, 0xCE, 0x61, 0x7B, 0xD7, 0xB2, 0x3C, 0x20, 0xAD, 0x08, 0xBB, 0xF2, 0x2E, 0x43, 0xC0, 0x9E, 0x72, 0xD2, 0x7C, 0x60, 0xCD, 0xAE, 0x21, 0x3B, 0xB7, 0x84, 0x52, 0x5D, 0x88, 0xE9, 0x1E, 0x17, 0xE3, 0x77, 0x9D, 0xC1, 0x44, 0x2D, 0xF7, 0xBC, 0x09, 0x6D, 0x97, 0xDC, 0x49, 0x37, 0xFD, 0xA1, 0x04, 0x29, 0x76, 0xBF, 0xC3, 0x74, 0x2A, 0xC5, 0xB8, 0x23, 0x18, 0xB6, 0xE2, 0x78, 0x53, 0xCA, 0x8E, 0xA8, 0xEB, 0x3A, 0x16, 0xD3, 0x80, 0x66, 0x5A, 0x96, 0xF9, 0x4B, 0x07, 0xFA, 0x94, 0x00, 0x4D, 0xE7, 0xB5, 0x19, 0x24, 0x8D, 0xCF, 0x54, 0x79, 0x15, 0x3F, 0xEC, 0xA9, 0x5F, 0x65, 0x81, 0xD4, 0x42, 0x0C, 0x98, 0xF5, 0x0E, 0x41, 0xF3, 0x9F, 0xA4, 0xDA, 0x35, 0x68, 0xD9, 0xA6, 0x6F,
            0x33, 0xDD, 0x4F, 0x6C, 0x91, 0xA7, 0x05, 0x31, 0xFC, 0x62, 0xCC, 0xD0, 0x7D, 0x3E, 0xB1, 0xAB, 0x27, 0x5C, 0x8A, 0x85, 0x50, 0x11, 0xE6, 0xEF, 0x1B, 0xC7, 0x45, 0x71, 0x9C, 0xBD, 0x0F, 0x2C, 0xF1, 0x51, 0x86, 0x8F, 0x5B, 0x1C, 0xEA, 0xE5, 0x10, 0x7E, 0xD1, 0xCB, 0x67, 0x22, 0xAC, 0xB0, 0x3D, 0xF0, 0x2B, 0x0A, 0xBE, 0x9B, 0x70, 0x46, 0xC2, 0xFB, 0x30, 0x06, 0xA2, 0x90, 0x6B, 0x4A, 0xDE, 0x9A, 0xF4, 0x40, 0x0D, 0xF6, 0x99, 0x0B, 0x47, 0xED, 0xAF, 0x14, 0x39, 0x87, 0xD5, 0x59, 0x64, 0x1F, 0x25, 0xE1, 0xB4, 0x55, 0x7F, 0x8C, 0xC9, 0x34, 0x6A, 0xA5, 0xD8, 0x69, 0x36, 0xDF, 0xA3, 0x38, 0x13, 0xAA, 0xEE, 0x63, 0x58, 0xD6, 0x82, 0xB3, 0xE0, 0x26, 0x1A, 0xC8, 0x8B, 0x7A, 0x56, 0xB9, 0xC6, 0x2F, 0x73, 0xC4, 0xBA, 0x75, 0x28, 0x4E, 0x01, 0x93, 0xFF, 0x02, 0x4C, 0xF8, 0x95]

ROUND_KEY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

ROUND = 17
INT_NUM = 2 * 4
MASTER_KEY_SIZE = 4


def key_add(val, rk, num):  # C에서의 RK+(i*8)를 num 인수에 받아서 처리
    # 호출될 때마다 num값에 따라 rk array index가 바뀜
    val[0] ^= rk[0+8*num]
    val[1] ^= rk[1+8*num]
    val[2] ^= rk[2+8*num]
    val[3] ^= rk[3+8*num]
    val[4] ^= rk[4+8*num]
    val[5] ^= rk[5+8*num]
    val[6] ^= rk[6+8*num]
    val[7] ^= rk[7+8*num]


def convert(X):
    T = [0, 0, 0, 0, 0, 0, 0, 0]
    T[0] |= (((X[0] & (1 << 0)) >> 0) << 0)
    T[0] |= (((X[1] & (1 << 0)) >> 0) << 1)
    T[0] |= (((X[2] & (1 << 0)) >> 0) << 2)
    T[0] |= (((X[3] & (1 << 0)) >> 0) << 3)
    T[0] |= (((X[4] & (1 << 0)) >> 0) << 4)
    T[0] |= (((X[5] & (1 << 0)) >> 0) << 5)
    T[0] |= (((X[6] & (1 << 0)) >> 0) << 6)
    T[0] |= (((X[7] & (1 << 0)) >> 0) << 7)

    T[1] |= (((X[0] & (1 << 1)) >> 1) << 0)
    T[1] |= (((X[1] & (1 << 1)) >> 1) << 1)
    T[1] |= (((X[2] & (1 << 1)) >> 1) << 2)
    T[1] |= (((X[3] & (1 << 1)) >> 1) << 3)
    T[1] |= (((X[4] & (1 << 1)) >> 1) << 4)
    T[1] |= (((X[5] & (1 << 1)) >> 1) << 5)
    T[1] |= (((X[6] & (1 << 1)) >> 1) << 6)
    T[1] |= (((X[7] & (1 << 1)) >> 1) << 7)
            
    T[2] |= (((X[0] & (1 << 2)) >> 2) << 0)
    T[2] |= (((X[1] & (1 << 2)) >> 2) << 1)
    T[2] |= (((X[2] & (1 << 2)) >> 2) << 2)
    T[2] |= (((X[3] & (1 << 2)) >> 2) << 3)
    T[2] |= (((X[4] & (1 << 2)) >> 2) << 4)
    T[2] |= (((X[5] & (1 << 2)) >> 2) << 5)
    T[2] |= (((X[6] & (1 << 2)) >> 2) << 6)
    T[2] |= (((X[7] & (1 << 2)) >> 2) << 7)
    
    T[3] |= (((X[0] & (1 << 3)) >> 3) << 0)
    T[3] |= (((X[1] & (1 << 3)) >> 3) << 1)
    T[3] |= (((X[2] & (1 << 3)) >> 3) << 2)
    T[3] |= (((X[3] & (1 << 3)) >> 3) << 3)
    T[3] |= (((X[4] & (1 << 3)) >> 3) << 4)
    T[3] |= (((X[5] & (1 << 3)) >> 3) << 5)
    T[3] |= (((X[6] & (1 << 3)) >> 3) << 6)
    T[3] |= (((X[7] & (1 << 3)) >> 3) << 7)

    T[4] |= (((X[0] & (1 << 4)) >> 4) << 0)
    T[4] |= (((X[1] & (1 << 4)) >> 4) << 1)
    T[4] |= (((X[2] & (1 << 4)) >> 4) << 2)
    T[4] |= (((X[3] & (1 << 4)) >> 4) << 3)
    T[4] |= (((X[4] & (1 << 4)) >> 4) << 4)
    T[4] |= (((X[5] & (1 << 4)) >> 4) << 5)
    T[4] |= (((X[6] & (1 << 4)) >> 4) << 6)
    T[4] |= (((X[7] & (1 << 4)) >> 4) << 7)

    T[5] |= (((X[0] & (1 << 5)) >> 5) << 0)
    T[5] |= (((X[1] & (1 << 5)) >> 5) << 1)
    T[5] |= (((X[2] & (1 << 5)) >> 5) << 2)
    T[5] |= (((X[3] & (1 << 5)) >> 5) << 3)
    T[5] |= (((X[4] & (1 << 5)) >> 5) << 4)
    T[5] |= (((X[5] & (1 << 5)) >> 5) << 5)
    T[5] |= (((X[6] & (1 << 5)) >> 5) << 6)
    T[5] |= (((X[7] & (1 << 5)) >> 5) << 7)

    T[6] |= (((X[0] & (1 << 6)) >> 6) << 0)
    T[6] |= (((X[1] & (1 << 6)) >> 6) << 1)
    T[6] |= (((X[2] & (1 << 6)) >> 6) << 2)
    T[6] |= (((X[3] & (1 << 6)) >> 6) << 3)
    T[6] |= (((X[4] & (1 << 6)) >> 6) << 4)
    T[6] |= (((X[5] & (1 << 6)) >> 6) << 5)
    T[6] |= (((X[6] & (1 << 6)) >> 6) << 6)
    T[6] |= (((X[7] & (1 << 6)) >> 6) << 7)

    T[7] |= (((X[0] & (1 << 7)) >> 7) << 0)
    T[7] |= (((X[1] & (1 << 7)) >> 7) << 1)
    T[7] |= (((X[2] & (1 << 7)) >> 7) << 2)
    T[7] |= (((X[3] & (1 << 7)) >> 7) << 3)
    T[7] |= (((X[4] & (1 << 7)) >> 7) << 4)
    T[7] |= (((X[5] & (1 << 7)) >> 7) << 5)
    T[7] |= (((X[6] & (1 << 7)) >> 7) << 6)
    T[7] |= (((X[7] & (1 << 7)) >> 7) << 7)

    X[0] = T[0]
    X[1] = T[1]
    X[2] = T[2]
    X[3] = T[3]
    X[4] = T[4]
    X[5] = T[5]
    X[6] = T[6]
    X[7] = T[7]

def sbox_TLU(X):
    convert(X)
    X[0] = Sbox[X[0]]
    X[1] = Sbox[X[1]]
    X[2] = Sbox[X[2]]
    X[3] = Sbox[X[3]]
    X[4] = Sbox[X[4]]
    X[5] = Sbox[X[5]]
    X[6] = Sbox[X[6]]
    X[7] = Sbox[X[7]]
    convert(X)


def inv_sbox_TLU(X):
    convert(X)
    X[0] = Sbox_inv[X[0]]
    X[1] = Sbox_inv[X[1]]
    X[2] = Sbox_inv[X[2]]
    X[3] = Sbox_inv[X[3]]
    X[4] = Sbox_inv[X[4]]
    X[5] = Sbox_inv[X[5]]
    X[6] = Sbox_inv[X[6]]
    X[7] = Sbox_inv[X[7]]
    convert(X)

def pbox(X):
    # & 0XFF를 추가시켜준 이유 : C에서는 8비트로 설정해놓으면 계산하면서 자동으로 8비트 넘으면 잘라버리는데
    # 파이썬은 고려 안해줘서 25a5처럼 16비트로 나옴. 우리는 뒤의 8비트인 a5만 필요함. 그래서 앞의 8비트를 잘랐음.
    X[1] = ((X[1] << 7) | (X[1] >> 1)) & 0XFF
    X[2] = ((X[2] << 4) | (X[2] >> 4)) & 0XFF
    X[3] = ((X[3] << 3) | (X[3] >> 5)) & 0XFF
    X[4] = ((X[4] << 6) | (X[4] >> 2)) & 0XFF
    X[5] = ((X[5] << 5) | (X[5] >> 3)) & 0XFF
    X[6] = ((X[6] << 1) | (X[6] >> 7)) & 0XFF
    X[7] = ((X[7] << 2) | (X[7] >> 6)) & 0XFF


def inv_pbox(X):
    X[1] = ((X[1] << 1) | (X[1] >> 7)) & 0XFF
    X[2] = ((X[2] << 4) | (X[2] >> 4)) & 0XFF
    X[3] = ((X[3] << 5) | (X[3] >> 3)) & 0XFF
    X[4] = ((X[4] << 2) | (X[4] >> 6)) & 0XFF
    X[5] = ((X[5] << 3) | (X[5] >> 5)) & 0XFF
    X[6] = ((X[6] << 7) | (X[6] >> 1)) & 0XFF
    X[7] = ((X[7] << 6) | (X[7] >> 2)) & 0XFF


def ENC_TLU(PLAIN_TEXT, CIPHER_TEXT):
    P = []
    RK = [] 
    
    RK = ROUND_KEY
    
    # P 비트 쪼개기 작업
    P.append(PLAIN_TEXT[0] & 0XFF)
    PLAIN_TEXT[0] = PLAIN_TEXT[0] >> 8
    P.append(PLAIN_TEXT[0] & 0XFF)
    PLAIN_TEXT[0] = PLAIN_TEXT[0] >> 8
    P.append(PLAIN_TEXT[0] & 0XFF)
    PLAIN_TEXT[0] = PLAIN_TEXT[0] >> 8
    P.append(PLAIN_TEXT[0] & 0XFF)

    P.append(PLAIN_TEXT[1] & 0XFF)
    PLAIN_TEXT[1] = PLAIN_TEXT[1] >> 8
    P.append(PLAIN_TEXT[1] & 0XFF)
    PLAIN_TEXT[1] = PLAIN_TEXT[1] >> 8
    P.append(PLAIN_TEXT[1] & 0XFF)
    PLAIN_TEXT[1] = PLAIN_TEXT[1] >> 8
    P.append(PLAIN_TEXT[1] & 0XFF)
    
    key_add(P, RK, 0)
    
    # ROUND 1 
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 1)

    # ROUND 2
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 2)


    # ROUND 3
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 3)

    # ROUND 4         
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 4)

    # ROUND 5
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 5)
    
    # ROUND 6
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 6)

    # ROUND 7
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 7)

    # ROUND 8
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 8)

    # ROUND 9
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 9)

    # ROUND 10
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 10)

    # ROUND 11
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 11)

    # ROUND 12
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 12)

    # ROUND 13
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 13)
    
    # ROUND 14
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 14)
    
    # ROUND 15
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 15)
    
    # ROUND 16
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 16)
    
    # ROUND 17
    sbox_TLU(P)
    pbox(P)
    key_add(P, RK, 17)
    
    return P

def DEC_TLU(CIPHER_TEXT, PLAIN_TEXT):
    C = []
    C = CIPHER_TEXT

    RK = ROUND_KEY


    # ROUND 1
    key_add(C, RK, 17)
    inv_pbox(C)
    inv_sbox_TLU(C)
    
    # ROUND 2
    key_add(C, RK, 16)
    inv_pbox(C)
    inv_sbox_TLU(C)
    
    # ROUND 3
    key_add(C, RK, 15)
    inv_pbox(C)
    inv_sbox_TLU(C)
    
    # ROUND 4
    key_add(C, RK, 14)
    inv_pbox(C)
    inv_sbox_TLU(C)
    
    # ROUND 5
    key_add(C, RK, 13)
    inv_pbox(C)
    inv_sbox_TLU(C)

    # ROUND 6
    key_add(C, RK, 12)
    inv_pbox(C)
    inv_sbox_TLU(C)

    # ROUND 7
    key_add(C, RK, 11)
    inv_pbox(C)
    inv_sbox_TLU(C)

    # ROUND 8
    key_add(C, RK, 10)
    inv_pbox(C)
    inv_sbox_TLU(C)

    # ROUND 9
    key_add(C, RK, 9)
    inv_pbox(C)
    inv_sbox_TLU(C)

    # ROUND 10
    key_add(C, RK, 8)
    inv_pbox(C)
    inv_sbox_TLU(C)

    # ROUND 11
    key_add(C, RK, 7)
    inv_pbox(C)
    inv_sbox_TLU(C)

    # ROUND 12
    key_add(C, RK, 6)
    inv_pbox(C)
    inv_sbox_TLU(C)

    # ROUND 13
    key_add(C, RK, 5)
    inv_pbox(C)
    inv_sbox_TLU(C)

    # ROUND 14
    key_add(C, RK, 4)
    inv_pbox(C)
    inv_sbox_TLU(C)

    # ROUND 15
    key_add(C, RK, 3)
    inv_pbox(C)
    inv_sbox_TLU(C)

    # ROUND 16
    key_add(C, RK, 2)
    inv_pbox(C)
    inv_sbox_TLU(C)

    # ROUND 17
    key_add(C, RK, 1)
    inv_pbox(C)
    inv_sbox_TLU(C)

    key_add(C, RK, 0);

def ROUND_KEY_GEN(MASTER_KEY):
    RCON = 0

    # ROUND_KEY 1
    ROUND_KEY[INT_NUM * 0 + 0] = MASTER_KEY[(INT_NUM * 0 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 0 + 1] = MASTER_KEY[(INT_NUM * 0 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 0 + 2] = MASTER_KEY[(INT_NUM * 0 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 0 + 3] = MASTER_KEY[(INT_NUM * 0 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 0 + 4] = MASTER_KEY[(INT_NUM * 0 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 0 + 5] = MASTER_KEY[(INT_NUM * 0 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 0 + 6] = MASTER_KEY[(INT_NUM * 0 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 0 + 7] = MASTER_KEY[(INT_NUM * 0 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 0] ^= RCON
    RCON += 1

    # ROUND_KEY 2
    ROUND_KEY[INT_NUM * 1 + 0] = MASTER_KEY[(INT_NUM * 1 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 1 + 1] = MASTER_KEY[(INT_NUM * 1 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 1 + 2] = MASTER_KEY[(INT_NUM * 1 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 1 + 3] = MASTER_KEY[(INT_NUM * 1 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 1 + 4] = MASTER_KEY[(INT_NUM * 1 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 1 + 5] = MASTER_KEY[(INT_NUM * 1 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 1 + 6] = MASTER_KEY[(INT_NUM * 1 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 1 + 7] = MASTER_KEY[(INT_NUM * 1 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 1] ^= RCON
    RCON += 1

    # ROUND_KEY 3
    ROUND_KEY[INT_NUM * 2 + 0] = MASTER_KEY[(INT_NUM * 2 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 2 + 1] = MASTER_KEY[(INT_NUM * 2 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 2 + 2] = MASTER_KEY[(INT_NUM * 2 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 2 + 3] = MASTER_KEY[(INT_NUM * 2 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 2 + 4] = MASTER_KEY[(INT_NUM * 2 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 2 + 5] = MASTER_KEY[(INT_NUM * 2 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 2 + 6] = MASTER_KEY[(INT_NUM * 2 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 2 + 7] = MASTER_KEY[(INT_NUM * 2 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 2] ^= RCON
    RCON += 1

    # ROUND_KEY 4
    ROUND_KEY[INT_NUM * 3 + 0] = MASTER_KEY[(INT_NUM * 3 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 3 + 1] = MASTER_KEY[(INT_NUM * 3 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 3 + 2] = MASTER_KEY[(INT_NUM * 3 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 3 + 3] = MASTER_KEY[(INT_NUM * 3 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 3 + 4] = MASTER_KEY[(INT_NUM * 3 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 3 + 5] = MASTER_KEY[(INT_NUM * 3 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 3 + 6] = MASTER_KEY[(INT_NUM * 3 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 3 + 7] = MASTER_KEY[(INT_NUM * 3 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 3] ^= RCON
    RCON += 1

    # ROUND_KEY 5
    ROUND_KEY[INT_NUM * 4 + 0] = MASTER_KEY[(INT_NUM * 4 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 4 + 1] = MASTER_KEY[(INT_NUM * 4 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 4 + 2] = MASTER_KEY[(INT_NUM * 4 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 4 + 3] = MASTER_KEY[(INT_NUM * 4 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 4 + 4] = MASTER_KEY[(INT_NUM * 4 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 4 + 5] = MASTER_KEY[(INT_NUM * 4 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 4 + 6] = MASTER_KEY[(INT_NUM * 4 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 4 + 7] = MASTER_KEY[(INT_NUM * 4 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 4] ^= RCON
    RCON += 1

    # ROUND_KEY 6
    ROUND_KEY[INT_NUM * 5 + 0] = MASTER_KEY[(INT_NUM * 5 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 5 + 1] = MASTER_KEY[(INT_NUM * 5 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 5 + 2] = MASTER_KEY[(INT_NUM * 5 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 5 + 3] = MASTER_KEY[(INT_NUM * 5 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 5 + 4] = MASTER_KEY[(INT_NUM * 5 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 5 + 5] = MASTER_KEY[(INT_NUM * 5 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 5 + 6] = MASTER_KEY[(INT_NUM * 5 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 5 + 7] = MASTER_KEY[(INT_NUM * 5 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 5] ^= RCON
    RCON += 1

    # ROUND_KEY 7
    ROUND_KEY[INT_NUM * 6 + 0] = MASTER_KEY[(INT_NUM * 6 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 6 + 1] = MASTER_KEY[(INT_NUM * 6 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 6 + 2] = MASTER_KEY[(INT_NUM * 6 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 6 + 3] = MASTER_KEY[(INT_NUM * 6 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 6 + 4] = MASTER_KEY[(INT_NUM * 6 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 6 + 5] = MASTER_KEY[(INT_NUM * 6 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 6 + 6] = MASTER_KEY[(INT_NUM * 6 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 6 + 7] = MASTER_KEY[(INT_NUM * 6 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 6] ^= RCON
    RCON += 1

    # ROUND_KEY 8
    ROUND_KEY[INT_NUM * 7 + 0] = MASTER_KEY[(INT_NUM * 7 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 7 + 1] = MASTER_KEY[(INT_NUM * 7 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 7 + 2] = MASTER_KEY[(INT_NUM * 7 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 7 + 3] = MASTER_KEY[(INT_NUM * 7 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 7 + 4] = MASTER_KEY[(INT_NUM * 7 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 7 + 5] = MASTER_KEY[(INT_NUM * 7 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 7 + 6] = MASTER_KEY[(INT_NUM * 7 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 7 + 7] = MASTER_KEY[(INT_NUM * 7 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 7] ^= RCON
    RCON += 1

    # ROUND_KEY 9
    ROUND_KEY[INT_NUM * 8 + 0] = MASTER_KEY[(INT_NUM * 8 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 8 + 1] = MASTER_KEY[(INT_NUM * 8 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 8 + 2] = MASTER_KEY[(INT_NUM * 8 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 8 + 3] = MASTER_KEY[(INT_NUM * 8 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 8 + 4] = MASTER_KEY[(INT_NUM * 8 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 8 + 5] = MASTER_KEY[(INT_NUM * 8 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 8 + 6] = MASTER_KEY[(INT_NUM * 8 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 8 + 7] = MASTER_KEY[(INT_NUM * 8 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 8] ^= RCON
    RCON += 1

    # ROUND_KEY 10
    ROUND_KEY[INT_NUM * 9 + 0] = MASTER_KEY[(INT_NUM * 9 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 9 + 1] = MASTER_KEY[(INT_NUM * 9 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 9 + 2] = MASTER_KEY[(INT_NUM * 9 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 9 + 3] = MASTER_KEY[(INT_NUM * 9 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 9 + 4] = MASTER_KEY[(INT_NUM * 9 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 9 + 5] = MASTER_KEY[(INT_NUM * 9 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 9 + 6] = MASTER_KEY[(INT_NUM * 9 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 9 + 7] = MASTER_KEY[(INT_NUM * 9 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 9] ^= RCON
    RCON += 1

    # ROUND_KEY 11
    ROUND_KEY[INT_NUM * 10 + 0] = MASTER_KEY[(INT_NUM * 10 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 10 + 1] = MASTER_KEY[(INT_NUM * 10 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 10 + 2] = MASTER_KEY[(INT_NUM * 10 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 10 + 3] = MASTER_KEY[(INT_NUM * 10 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 10 + 4] = MASTER_KEY[(INT_NUM * 10 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 10 + 5] = MASTER_KEY[(INT_NUM * 10 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 10 + 6] = MASTER_KEY[(INT_NUM * 10 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 10 + 7] = MASTER_KEY[(INT_NUM * 10 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 10] ^= RCON
    RCON += 1

    # ROUND_KEY 12
    ROUND_KEY[INT_NUM * 11 + 0] = MASTER_KEY[(INT_NUM * 11 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 11 + 1] = MASTER_KEY[(INT_NUM * 11 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 11 + 2] = MASTER_KEY[(INT_NUM * 11 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 11 + 3] = MASTER_KEY[(INT_NUM * 11 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 11 + 4] = MASTER_KEY[(INT_NUM * 11 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 11 + 5] = MASTER_KEY[(INT_NUM * 11 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 11 + 6] = MASTER_KEY[(INT_NUM * 11 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 11 + 7] = MASTER_KEY[(INT_NUM * 11 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 11] ^= RCON
    RCON += 1

    # ROUND_KEY 13
    ROUND_KEY[INT_NUM * 12 + 0] = MASTER_KEY[(INT_NUM * 12 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 12 + 1] = MASTER_KEY[(INT_NUM * 12 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 12 + 2] = MASTER_KEY[(INT_NUM * 12 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 12 + 3] = MASTER_KEY[(INT_NUM * 12 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 12 + 4] = MASTER_KEY[(INT_NUM * 12 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 12 + 5] = MASTER_KEY[(INT_NUM * 12 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 12 + 6] = MASTER_KEY[(INT_NUM * 12 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 12 + 7] = MASTER_KEY[(INT_NUM * 12 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 12] ^= RCON
    RCON += 1

    # ROUND_KEY 14
    ROUND_KEY[INT_NUM * 13 + 0] = MASTER_KEY[(INT_NUM * 13 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 13 + 1] = MASTER_KEY[(INT_NUM * 13 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 13 + 2] = MASTER_KEY[(INT_NUM * 13 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 13 + 3] = MASTER_KEY[(INT_NUM * 13 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 13 + 4] = MASTER_KEY[(INT_NUM * 13 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 13 + 5] = MASTER_KEY[(INT_NUM * 13 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 13 + 6] = MASTER_KEY[(INT_NUM * 13 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 13 + 7] = MASTER_KEY[(INT_NUM * 13 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 13] ^= RCON
    RCON += 1

    # ROUND_KEY 15
    ROUND_KEY[INT_NUM * 14 + 0] = MASTER_KEY[(INT_NUM * 14 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 14 + 1] = MASTER_KEY[(INT_NUM * 14 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 14 + 2] = MASTER_KEY[(INT_NUM * 14 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 14 + 3] = MASTER_KEY[(INT_NUM * 14 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 14 + 4] = MASTER_KEY[(INT_NUM * 14 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 14 + 5] = MASTER_KEY[(INT_NUM * 14 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 14 + 6] = MASTER_KEY[(INT_NUM * 14 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 14 + 7] = MASTER_KEY[(INT_NUM * 14 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 14] ^= RCON
    RCON += 1

    # ROUND_KEY 16
    ROUND_KEY[INT_NUM * 15 + 0] = MASTER_KEY[(INT_NUM * 15 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 15 + 1] = MASTER_KEY[(INT_NUM * 15 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 15 + 2] = MASTER_KEY[(INT_NUM * 15 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 15 + 3] = MASTER_KEY[(INT_NUM * 15 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 15 + 4] = MASTER_KEY[(INT_NUM * 15 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 15 + 5] = MASTER_KEY[(INT_NUM * 15 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 15 + 6] = MASTER_KEY[(INT_NUM * 15 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 15 + 7] = MASTER_KEY[(INT_NUM * 15 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 15] ^= RCON
    RCON += 1

    # ROUND_KEY 17
    ROUND_KEY[INT_NUM * 16 + 0] = MASTER_KEY[(INT_NUM * 16 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 16 + 1] = MASTER_KEY[(INT_NUM * 16 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 16 + 2] = MASTER_KEY[(INT_NUM * 16 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 16 + 3] = MASTER_KEY[(INT_NUM * 16 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 16 + 4] = MASTER_KEY[(INT_NUM * 16 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 16 + 5] = MASTER_KEY[(INT_NUM * 16 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 16 + 6] = MASTER_KEY[(INT_NUM * 16 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 16 + 7] = MASTER_KEY[(INT_NUM * 16 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 16] ^= RCON
    RCON += 1

    # ROUND_KEY 18
    ROUND_KEY[INT_NUM * 17 + 0] = MASTER_KEY[(INT_NUM * 17 + 0) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 17 + 1] = MASTER_KEY[(INT_NUM * 17 + 1) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 17 + 2] = MASTER_KEY[(INT_NUM * 17 + 2) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 17 + 3] = MASTER_KEY[(INT_NUM * 17 + 3) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 17 + 4] = MASTER_KEY[(INT_NUM * 17 + 4) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 17 + 5] = MASTER_KEY[(INT_NUM * 17 + 5) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 17 + 6] = MASTER_KEY[(INT_NUM * 17 + 6) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 17 + 7] = MASTER_KEY[(INT_NUM * 17 + 7) % (MASTER_KEY_SIZE * INT_NUM)]
    ROUND_KEY[INT_NUM * 17] ^= RCON
    RCON += 1