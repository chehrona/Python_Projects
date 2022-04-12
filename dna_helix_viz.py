import random, time, sys
from signal import pause
from typing import final

dnaLetters = ["A", "T", "C", "G"]
pauseTime = 3
def dnaViz():
    print("Press Ctrl-C to quit...\n")
    time.sleep(pauseTime)
    
    i = 0
    while i >= 0:
        ar = [] #Stores pairs of letters AT and GC
        i += 1
        for repeat in range(0, 16):
            letterSelection = random.choice(dnaLetters)
            # print(letterSelection)
            randomLetter = []
            if letterSelection == "A":
                randomLetter.append("A")
                randomLetter.append("T")
            elif letterSelection == "T":
                randomLetter.append("T")
                randomLetter.append("A")
            elif letterSelection == "G":
                randomLetter.append("G")
                randomLetter.append("C")
            else:
                randomLetter.append("C")
                randomLetter.append("G")
            ar.append(randomLetter)

        finalStr = ""
        finalStr = ("    #{}-{}#  \n   #{}---{}# \n  #{}-----{}#\n #{}------{}#\n#{}------{}# \n#{}-----{}#  \n #{}---{}#   \n #{}-{}#     \n  ##       \n" + 
                    " #{}-{}#     \n #{}---{}#   \n#{}-----{}#  \n#{}------{}# \n #{}------{}#\n  #{}-----{}#\n   #{}---{}# \n    #{}-{}#  \n     ##    ").format(ar[0][0], ar[0][1], ar[1][0], ar[1][1], ar[2][0], ar[2][1], ar[3][0], ar[3][1], ar[4][0], ar[4][0], ar[4][1], ar[5][0], ar[5][1], ar[6][0], ar[6][1], 
                        ar[7][0], ar[7][1], ar[8][0], ar[8][1], ar[9][0], ar[9][1], ar[10][0], ar[11][1], ar[12][0], ar[12][1], ar[13][0], ar[13][1], ar[14][0], ar[14][0], ar[14][1], ar[15][0], ar[15][1])
        try:
            print(finalStr) 
            time.sleep(pauseTime)
        except KeyboardInterrupt:
            sys.exit()
    return 
dnaViz()
