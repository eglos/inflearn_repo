#표준입출력
# print("Python","Java",sep=",")
# print("무엇이 더 재미있을까요?")

# print("Python","Java",sep=",",end="?")
# print("무엇이 더 재미있을까요?")

# import sys
# print("Python","Java", file=sys.stdout)
# print("Python","Java", file=sys.stderr)

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject,score in scores.items(): # items() : key, value 구분지어 출력
    #print(subject,score)
    # print(subject.ljust(8),str(score).rjust(4), sep=":") # sep : 문자열 연결 시 구분자 입력

# 은행 순번대기표 
# 001, 002, 003, ...
# for num in range(1,21) :
#     print("대기번호 : " + str(num).zfill(3)) # zfill : 해당 자리수 만큼 출력 시 빈 공간은 0으로 표시

answer = input("아무 값이나 입력하세요 : ") #사용자 입력을 받게 될 때는 문자열 타입으로 받게 됨.
print(type(answer))
print("입력하신 값은 " + answer + " 입니다.")