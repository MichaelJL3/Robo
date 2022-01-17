
from pwm_to_angle import convert_pwm_to_angle

def move_1():
    pwm = 300
    height = 0
    b_d = 1
    m_d = -1
    e_d = -1

    w_v = 200
    w_m = 30

    b = pwm + w_m * b_d
    m = pwm + (w_v - height) * m_d
    e = pwm + w_v * e_d

    return (b, m, e)

def move_2():
    pwm = 300
    height = 0
    b_d = 1
    m_d = -1

    w_h = 120
    w_m = 30

    b = pwm + (w_m + w_h) * b_d
    m = pwm - height * m_d
    e = pwm

    return (b, m, e)

def move_n(n):
    pwm = 300
    height = 0
    b_d = 1
    m_d = -1

    w_h = 120
    w_m = 30

    b = pwm + (w_m + w_h * (6-(n-2))/3 - w_h) * b_d
    m = pwm - height * m_d
    e = pwm

    return (b, m, e)

def convert_move(move):
    b, m, e = move
    return (convert_pwm_to_angle(b), convert_pwm_to_angle(m), convert_pwm_to_angle(e))

def gait():
    m1 = move_1()
    m2 = move_2()
    
    st_moves = [m1, m2]
    n_moves = [move_n(i) for i in range(3, 9)]

    return st_moves + n_moves

def move_angles(moves):
    return list(map(lambda m: convert_move(m), moves))

if __name__ == '__main__':
    moves = gait()

    print("pwm moves 1-8")
    for move in moves:
        print(move)

    angles = move_angles(moves)

    print("angle moves 1-8")
    for move_angle in angles:
        print(move_angle)
