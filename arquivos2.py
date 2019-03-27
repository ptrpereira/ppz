import random
arq = open('list.txt', 'r')
arqOrd = open('listOrd.txt', 'w')
arr = arq.readlines()
random.shuffle(arr)
arqOrd.writelines(arr)
arq.close()
arqOrd.close()
