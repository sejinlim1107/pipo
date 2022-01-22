ROUND_KEY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

ROUND = 13
INT_NUM = 2 * 4
MASTER_KEY_SIZE = 2


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


def sbox(X):
    T = [0, 0, 0]
    # (MSB: x[7], LSB: x[0])
    # Input: x[7], x[6], x[5], x[4], x[3], x[2], x[1], x[0]
    # S5_1

    X[5] ^= (X[7] & X[6]) & 0xFF
    X[4] ^= (X[3] & X[5]) & 0xFF
    X[7] ^= X[4] & 0xFF
    X[6] ^= X[3] & 0xFF
    X[3] ^= (X[4] | X[5]) & 0xFF
    X[5] ^= X[7] & 0xFF
    X[4] ^= (X[5] & X[6]) & 0xFF

    # S3
    X[2] ^= X[1] & X[0] & 0xFF
    X[0] ^= X[2] | X[1] & 0xFF
    X[1] ^= X[2] | X[0] & 0xFF
    X[2] = ~X[2] & 0xFF

    # Extend XOR
    X[7] ^= X[1] & 0xFF
    X[3] ^= X[2] & 0xFF
    X[4] ^= X[0] & 0xFF

    # S5_2
    T[0] = X[7] & 0xFF
    T[1] = X[3] & 0xFF
    T[2] = X[4] & 0xFF
    X[6] ^= (T[0] & X[5]) & 0xFF
    T[0] ^= X[6] & 0xFF
    X[6] ^= (T[2] | T[1]) & 0xFF
    T[1] ^= X[5] & 0xFF
    X[5] ^= (X[6] | T[2]) & 0xFF
    T[2] ^= (T[1] & T[0]) & 0xFF

    # Truncate XOR and bit change
    X[2] ^= T[0] & 0xFF
    T[0] = X[1] ^ T[2] & 0xFF
    X[1] = X[0] ^ T[1] & 0xFF
    X[0] = X[7] & 0xFF
    X[7] = T[0] & 0xFF
    T[1] = X[3] & 0xFF
    X[3] = X[6] & 0xFF
    X[6] = T[1] & 0xFF
    T[2] = X[4] & 0xFF
    X[4] = X[5] & 0xFF
    X[5] = T[2] & 0xFF

    # Output: (MSb) x[7], x[6], x[5], x[4], x[3], x[2], x[1], x[0] (LSb)


def inv_sbox(X):
    # (MSB: x[7], LSB: x[0])
    # Input: x[7], x[6], x[5], x[4], x[3], x[2], x[1], x[0]

    T = [0, 0, 0]

    T[0] = X[7] & 0xFF
    X[7] = X[0] & 0xFF
    X[0] = X[1] & 0xFF
    X[1] = T[0] & 0xFF
    T[0] = X[7] & 0xFF
    T[1] = X[6] & 0xFF
    T[2] = X[5] & 0xFF

    # S52 inv
    X[4] ^= (X[3] | T[2]) & 0xFF
    X[3] ^= (T[2] | T[1]) & 0xFF
    T[1] ^= X[4] & 0xFF
    T[0] ^= X[3] & 0xFF
    T[2] ^= (T[1] & T[0]) & 0xFF
    X[3] ^= (X[4] & X[7]) & 0xFF

    #  Extended XOR
    X[0] ^= T[1] & 0xFF
    X[1] ^= T[2] & 0xFF
    X[2] ^= T[0] & 0xFF
    T[0] = X[3] & 0xFF
    X[3] = X[6] & 0xFF
    X[6] = T[0] & 0xFF
    T[0] = X[5] & 0xFF
    X[5] = X[4] & 0xFF
    X[4] = T[0] & 0xFF

    #  Truncated XOR
    X[7] ^= X[1] & 0xFF
    X[3] ^= X[2] & 0xFF
    X[4] ^= X[0] & 0xFF

    # Inv_S5_1
    X[4] ^= (X[5] & X[6]) & 0xFF
    X[5] ^= X[7] & 0xFF
    X[3] ^= (X[4] | X[5]) & 0xFF
    X[6] ^= X[3] & 0xFF
    X[7] ^= X[4] & 0xFF
    X[4] ^= (X[3] & X[5]) & 0xFF
    X[5] ^= (X[7] & X[6]) & 0xFF

    # Inv_S3
    X[2] = ~X[2] & 0xFF
    X[1] ^= X[2] | X[0] & 0xFF
    X[0] ^= X[2] | X[1] & 0xFF
    X[2] ^= X[1] & X[0] & 0xFF

    # Output: x[7], x[6], x[5], x[4], x[3], x[2], x[1], x[0


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


def ENC(PLAIN_TEXT, CIPHER_TEXT):
    P = []
    RK = [] 
    
    RK = ROUND_KEY
    
    for i in range(2):  # P 비트 쪼개기 작업
        for j in range(4):
            P.append(PLAIN_TEXT[i] & 0XFF)
            PLAIN_TEXT[i] = PLAIN_TEXT[i] >> 8

    key_add(P, RK, 0)

    for i in range(1, ROUND+1):
        sbox(P)
        pbox(P)
        key_add(P, RK, i)

    return P
    

def DEC(CIPHER_TEXT, PLAIN_TEXT):
    C = []
    C = CIPHER_TEXT

    RK = ROUND_KEY


            
    for i in range(ROUND, 0, -1):
        key_add(C, RK, i)
        inv_pbox(C)
        inv_sbox(C)

    key_add(C, RK, 0)


def ROUND_KEY_GEN(MASTER_KEY):
    RCON = 0

    for i in range(0, ROUND+1):
        for j in range(0, INT_NUM):
            ROUND_KEY[INT_NUM * i + j] = MASTER_KEY[(INT_NUM * i + j) % (MASTER_KEY_SIZE * INT_NUM)]
        ROUND_KEY[INT_NUM * i] ^= RCON
        RCON += 1
