# 키워드 값
# 함수에 자리를 바꿔서 넣어도 출력은 함수에 저장된 형태로 출력

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석",main_lang="파이썬",age=20)
profile(main_lang="자바",age=25,name="김태호")