import imageio 
import random
import cv2

arry = []
imge = cv2.imread('Ss.jpg')


imgeC = cv2.cvtColor(imge,cv2.COLOR_BGR2RGB)
row , col = imgeC.shape[:2]

for i in range(1000):
     C = random.randint(0,col)
     R = random.randint(-100,row)
     CH= random.choice([1,2])
     M = random.choice([-3,-2,-1,0,1,2,3])
     D = random.randint(5,10)
     arry.append([C,R,CH,M,D])

S_GIF= []
for i in range(row//5):
    imge1 = cv2.imread('Ss.jpg')
    imgeC = cv2.cvtColor(imge1,cv2.COLOR_BGR2RGB)
    for k,j in enumerate(arry): 

        cv2.circle(imgeC,(j[0],j[1]),j[2],(255, 200, 180),-1)
        j[0] = j[0] + j[3]  
        j[1] = j[1] + j[4]
    S_GIF.append(imgeC)
imageio.mimsave('snow.gif',S_GIF)
