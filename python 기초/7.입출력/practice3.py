#파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") # w : write
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close() # file을 open할 경우, 반드시 close()를 해야함

# score_file = open("score.txt","a",encoding="utf8") # a: append
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8") # "r" : read
# print(score_file.readline(), end="") #줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# while True :
#     line = score_file.readline()
#     if not line :
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines()
for line in lines :
    print(line, end="")