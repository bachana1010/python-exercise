"""
დაწერეთ ფუნქცია calculate_grade რომელსაც გადაეცემა ლისტი თითოეული ელემენტი ლისტიდან არის მოსწავლის განმსაძრვრელი dictionary
სადაც წერია სტუდენტის სახელი დავალების ქულები ტესტის ქულები და ლაბის ქულები თითოეულისტVის თვქნე უნდა გამოთვალოს საშუალო ქულა
და ამასთანავე უნდა გაითვალისწინოთ რომ საბოლოო შეფასების ქულა შემდეგი პროპორციით არის გადანაწილებული
10 % არის დავალებებიდან
70 % არის ტესტებიდან
20 % არის ლაბებიდან

საბოლოო ქულის გამოთVლის შემდეგ უნდა შეუსაბამოთ მას ინიციალი შემდეგი პირობით
1. score >= 90 : "A"
2. score >= 80 : "B"
3. score >= 70 : "C"
4. score >= 60 : "D"
5. score >= 50 : "E"
5. score >= 50 : "F"

საბოლოოდ უნდა დააბრუნოთ ლისტი სადაც თითოეული ელემენტი იქნება dictionary
რომელსაც ექნება ორი წყვილი(key value) ერთი იქნება name მეორე საბოლოო ქულის ინიციალი

argument:
    [{"name": "Jack Frost",    "assignment": [80, 50, 40, 20], "test": [75, 75], "lab": [78.20, 77.20]},
     {"name": "James Potter",  "assignment": [82, 56, 44, 30], "test": [90, 80], "lab": [87.90, 78.72]}
     {"name": "Dylan Rhodes",  "assignment": [87, 82, 93, 89], "test": [98, 87], "lab": [92, 94]}
     {"name": "Jessica Stone", "assignment": [67, 55, 77, 21], "test": [40, 50], "lab": [59, 44.56]}
output:
    [{"name": "Jack Frost", score: C},
    {"name": "James Potter", score: B},
    {"name": "Dylan Rhodes", score: A},
    {"name": "Jessica Stone", score: E}]

მაგალითი თუ როგორ გამოითVლება მაგალითად პირველი ადამიანის ქულა
Jack Frost final score = (80+50+40+20)÷4×0,1 + (75+75)÷2×0,7 + (78.2+77.2)÷2×0,2 = 72,79
72,79 > 70 ამიტომ შესაბამისი ინიციალი არის C

*********************************** წარმატებები ***********************************
"""
lst=[{"name": "Jack Frost",    "assignment": [80, 50, 40, 20], "test": [75, 75], "lab": [78.20, 77.20]},
    {"name": "James Potter",  "assignment": [82, 56, 44, 30], "test": [90, 80], "lab": [87.90, 78.72]},
    {"name": "Dylan Rhodes",  "assignment": [87, 82, 93, 89], "test": [98, 87], "lab": [92, 94]},
    {"name": "Jessica Stone", "assignment": [67, 55, 77, 21], "test": [40, 50], "lab": [59, 44.56]}]

jack_frost=lst[0]

james_potter=lst[1]

dylan_rhodes=lst[2]

jessica_Stone=lst[3]



#avarage point

def avarage_point(points):
    sum_point=sum(points)
    sum_point=float(sum_point)
    return sum_point/len(points)

#each others points avarage

def each_student_subject_avarage(student):
    assi=avarage_point(student["assignment"])
    test=avarage_point(student["test"])
    lab=avarage_point(student["lab"])

    return (0.1*assi+ 0.7*test+0.2 *lab)


#a-b-c-d-c score
def A_B_C_D(students_score):
    if students_score <=50:
        return "f"
    elif students_score <=60:
        return 'e'
    elif students_score <=70:
        return "d"
    elif students_score <=80:
        return "c"
    elif students_score <=90:
        return "b"
    elif students_score <=100:
        return "a"
    else: return "overdose"




lst1=[]
dict_jack={"name":"jack", "score":A_B_C_D(each_student_subject_avarage(jack_frost))}
dict_potter={"name":"james potter", "score":A_B_C_D(each_student_subject_avarage(james_potter))}
dict_rhodes={"name":"dylan_rhodes", "score":A_B_C_D(each_student_subject_avarage(dylan_rhodes))}
dict_stone={"name":"jessica stone", "score":A_B_C_D(each_student_subject_avarage(jessica_Stone))}

lst1.append(dict_jack)
lst1.append(dict_potter)
lst1.append(dict_rhodes)
lst1.append(dict_stone)

print(lst1)




