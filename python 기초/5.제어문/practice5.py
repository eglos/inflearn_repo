# 한줄로 끝내는 for문

# 출석번호가 1 2 3 4 앞에 100을 붙이기로 함.
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron Man","Thor","I am groot"]
students = [len(i) for i in students]
print(students)


# 학생 이름 대문자로 변환
students = ["Iron Man","Thor","I am groot"]
students = [i.upper() for i in students]
print(students)