def std_weight(height,gender): 
    height_cm = (height)*100
    if gender == "남자" :
        print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(round(height_cm),gender,round(height*height*22,2)))
    else :
        print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(round(height_cm),gender,round(height*height*21,2)))

std_weight(1.75,"남자")