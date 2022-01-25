
import numpy as nd

def smooth(c_pos, pos, motion = [.02, .05, .10, .25, .50, .75, .90, .95, .98, 1]):
    move = 0

    for pct in motion:
        move = c_pos + (pos - c_pos) * pct
        print(move)

def smooth_position(c_pos, pos, motion = [.02, .05, .10, .25, .50, .75, .90, .95, .98, 1]):
    moves = []

    p_x, p_y, p_z = pos
    c_p_x, c_p_y, c_p_z = c_pos

    for pct in motion:
        move_a = c_p_x + (p_x - c_p_x) * pct
        move_b = c_p_y + (p_y - c_p_y) * pct
        move_c = c_p_z + (p_z - c_p_z) * pct
        moves.append((move_a, move_b, move_c))

    return nd.array(moves)

if __name__ == '__main__':
    c_pos = (90, 90, 90)
    pos_1 = (90, 13, 13)
    pos_2 = (90, 90, 90)
    arr_1 = smooth_position(c_pos, pos_1)
    arr_2 = smooth_position(c_pos, pos_2)
    combined = nd.array([arr_1, arr_2])
    print(combined[:,0,2])
