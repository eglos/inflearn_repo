for i in range(1,51) :
    with open(".\7.입출력\{0}주차.txt".format(i), "w", encoding="utf8") as text_file :
        text_file.write("- {0} 주차 주간보고 -".format(i))
        text_file.write("\n부서 : ")
        text_file.write("\n이름 : ")
        text_file.write("\n업무 요약 : ")
        text_file.close()
