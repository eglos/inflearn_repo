#cabinet = {3:"유재석",100:"김태호"}

#print(cabinet[5]) #5라는 key에 대한 값이 없음
#print("hi")

cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["B-100"] = "조세호"

