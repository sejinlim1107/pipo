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
    sbox(P)
    pbox(P)
    key_add(P, RK, 1)

    # ROUND 2
    sbox(P)
    pbox(P)
    key_add(P, RK, 2)


    # ROUND 3
    sbox(P)
    pbox(P)
    key_add(P, RK, 3)

    # ROUND 4         
    sbox(P)
    pbox(P)
    key_add(P, RK, 4)

    # ROUND 5
    sbox(P)
    pbox(P)
    key_add(P, RK, 5)
    
    # ROUND 6
    sbox(P)
    pbox(P)
    key_add(P, RK, 6)

    # ROUND 7
    sbox(P)
    pbox(P)
    key_add(P, RK, 7)

    # ROUND 8
    sbox(P)
    pbox(P)
    key_add(P, RK, 8)

    # ROUND 9
    sbox(P)
    pbox(P)
    key_add(P, RK, 9)

    # ROUND 10
    sbox(P)
    pbox(P)
    key_add(P, RK, 10)

    # ROUND 11
    sbox(P)
    pbox(P)
    key_add(P, RK, 11)

    # ROUND 12
    sbox(P)
    pbox(P)
    key_add(P, RK, 12)

    # ROUND 13
    sbox(P)
    pbox(P)
    key_add(P, RK, 13)
    
    # ROUND 14
    sbox(P)
    pbox(P)
    key_add(P, RK, 14)
    
    # ROUND 15
    sbox(P)
    pbox(P)
    key_add(P, RK, 15)
    
    # ROUND 16
    sbox(P)
    pbox(P)
    key_add(P, RK, 16)
    
    # ROUND 17
    sbox(P)
    pbox(P)
    key_add(P, RK, 17)
    
    return P
    
def DEC(CIPHER_TEXT, PLAIN_TEXT):
    C = []
    C = CIPHER_TEXT

    RK = ROUND_KEY
    
    # ROUND 1
    key_add(C, RK, 17)
    inv_pbox(C)
    inv_sbox(C)
    
    # ROUND 2
    key_add(C, RK, 16)
    inv_pbox(C)
    inv_sbox(C)
    
    # ROUND 3
    key_add(C, RK, 15)
    inv_pbox(C)
    inv_sbox(C)
    
    # ROUND 4
    key_add(C, RK, 14)
    inv_pbox(C)
    inv_sbox(C)
    
    # ROUND 5
    key_add(C, RK, 13)
    inv_pbox(C)
    inv_sbox(C)

    # ROUND 6
    key_add(C, RK, 12)
    inv_pbox(C)
    inv_sbox(C)

    # ROUND 7
    key_add(C, RK, 11)
    inv_pbox(C)
    inv_sbox(C)

    # ROUND 8
    key_add(C, RK, 10)
    inv_pbox(C)
    inv_sbox(C)

    # ROUND 9
    key_add(C, RK, 9)
    inv_pbox(C)
    inv_sbox(C)

    # ROUND 10
    key_add(C, RK, 8)
    inv_pbox(C)
    inv_sbox(C)

    # ROUND 11
    key_add(C, RK, 7)
    inv_pbox(C)
    inv_sbox(C)

    # ROUND 12
    key_add(C, RK, 6)
    inv_pbox(C)
    inv_sbox(C)

    # ROUND 13
    key_add(C, RK, 5)
    inv_pbox(C)
    inv_sbox(C)

    # ROUND 14
    key_add(C, RK, 4)
    inv_pbox(C)
    inv_sbox(C)

    # ROUND 15
    key_add(C, RK, 3)
    inv_pbox(C)
    inv_sbox(C)

    # ROUND 16
    key_add(C, RK, 2)
    inv_pbox(C)
    inv_sbox(C)

    # ROUND 17
    key_add(C, RK, 1)
    inv_pbox(C)
    inv_sbox(C)

    key_add(C, RK, 0)


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