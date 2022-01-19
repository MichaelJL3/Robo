
def smooth(pos, motion = [.02, .03, .05, .15, .25, .25, .15, .05, .03, .02]):
    move = 0

    for pct in motion:
        move += pos * pct
        print(move)

if __name__ == '__main__':
    smooth(90)
