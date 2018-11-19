import sys, os, random
sys.path.insert(0, 'engine2d')
from TheRunTime import *


#initialize highscore
#reset highscore when starting up
f = open("assets/data/highscore.txt", "r+")
hs = int(f.readline())
f.seek(0)
f.truncate()
f.write(str('0'))
f.close()

print('-----------------------------------------------------------------------')
print('launching flappybird')
print('https://github.com/ramremo/Flappybird (ramremo repo)')
print('https://github.com/PopAdi/python-flappy-bird (PopAdi repo)')
print('developed by Rachel Hera')
print('-----------------------------------------------------------------------')

main()