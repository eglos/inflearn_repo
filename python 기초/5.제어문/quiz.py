# 난수

from random import *
cnt = 0 #총 탑승 승객 수
for i in range(1,51): #1에서 50까지의 승객
    time = randrange(5,51) #5분에서 50분 소요 시간
    if 5 <= time <= 15 :
        print("[O] {0}번쨰 손님 (소요시간  : {1}분".format(i,time))
        cnt += 1
    else: #매칭 실패한 경우
        print("[ ] {0}번쨰 손님 (소요시간  : {1}분".format(i,time))

print("총 탑승 승객 : {0} 분".format(cnt))