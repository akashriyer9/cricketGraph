import numpy as np
import matplotlib.pyplot as plt
import enum
score = [0,0,0,0,0,0,0]

def gameplay():
    for x in range(0,6):


        over = []
        coin  = np.random.randint(0,29)
        notout = True
        if coin >= 0 and coin < 2:
            over.append("0 runs.dot ball")
            input("")
            score[0] +=1
        elif coin >=2 and coin <11:
            over.append('1 run')
            input("")
            score[1] +=1
        elif coin>=11 and coin <14:
            over.append("2 runs")
            input("")
            score[2] +=1
        elif coin >=14 and coin <17:
            over.append("3 runs")
            input("")
            score[3] +=1
        elif coin >=17 and coin <23:
            over.append("4 runs, great")
            input("")
            score[4] +=1
        elif coin >=23 and coin <24:
            over.append("5 runs")
            input("")
            score[5] +=1
        elif coin >=24 and coin <26:
            over.append("6 runs")
            input("")
            score[6] +=1
        elif coin >=26 and coin <27:
            over.append("CLEAN BOWLED")
            input("")
            score[7] +=1
        elif coin >=27 and coin <28:
            over.append("RUN OUT")
            input("")
            score[7] +=1
        else:
            over.append("CATCH OUT")
            input("")
            score[7] +=1
            print(over)
print(score)
def t20(v = int(input("how many overs"))):
    for v in range(0,v):
        gameplay()

t20()
