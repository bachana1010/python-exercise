# """
# დაწერეთ ეგრეთწოდებული ჯეირანი. დაწერეთ პროგრამა სადაც მომხმარებელს შემოაყვანინებთ მის არჩევანს
# მაგალითად Rock Paper ან Scissors ასევე კომპიუტერმა გაკეთოს თავისი არჩევანი (რანდომის გამოყენებით)
# შემდეგ კი შეამოწმეთ თუ ვინ მოიგებს და დაბეჭდეთ. ყოველი ახალი თამაშის დროს მომხმარებელს კითხეთ სურს თუ არა თამაში კიდევ
# თუ არადა დაასრულეთ პროგრამა

# input:
#     Rock
#     დავუშვათ რომ კომპიუტერმა აირჩია Scissors

# output:
#     you win

# P.S
#     პრინტები დაწერეთ როგორც გინდათ ეს ამოცანა ტესტებზე არ შემოწმდება ამიტომ ეცადეთ უბრალოდ ლამაზად დაბეჭდოთ

#     random.randint(start, stop) start იდან stop შუალედში რანდომ რიცხვს დააბრუნებს

# *********************************** წარმატებები ***********************************
# """
# import random

# win="""
#     *****************
#     *    you are    *
#     *    Winner     *
#     *               *
#     *****************
# """
# loser="""
#     *****************
#     *    you are    *
#     *    loser      *
#     *               *
#     *****************
# """

# draw="""
#     *****************
#     *               *
#     *    draw       *
#     *               *
#     *****************
# """

# end="""
#     *****************
#     *   end  game   *
#     *               *
#     *               *
#     *****************
# """
# while True:

#     choise = ["Rock", "Paper", "Scissors"]

#     choices_random=random.randint(0,2)

#     result=choise[choices_random]



#     customer_choose=input("choose: Rock/Paper/Scissors: ")
# #     customer_choose=customer_choose.title()

# #     if result==customer_choose:
# #         print(draw)


    
# # #Rock


# #     if result=="Rock":
# #         if customer_choose=="Paper":
# #             print("computer choose:",result, "---- your choisc:",customer_choose, loser)
# #         elif customer_choose=="Scissors":
# #             print("computer choose: ",result, " -----your choice:",customer_choose,win)

# # #Paper


# #     if result=="Paper":
# #         if customer_choose=="Rock":
# #              print("computer choose:",result, " ----your choice:", customer_choose,loser)
# #         elif customer_choose=="Scissors":
# #                 print("computer choose:",result, "----your choice:", customer_choose,win)

# # #Scissors

# #     if result=="Scissors":
# #         if customer_choose=="Rock":
# #             print("computer choose:",result, "----your choice:" ,customer_choose, loser)
# #         elif customer_choose=="Paper":
# #             print("computer choose:",result, "----your choice:" ,customer_choose,win)
 
# #     customer_desicion=input("do you want play? yes/no ")

# #     if customer_desicion!="yes":
# #         print(end)

# #         break









# meore amoxsna

import random

choices=("Rock","Scissors", "Paper")

computer_choice_index=random.randint(0,len(choices)-1)

computer_choice=choices[computer_choice_index]

user_choice=input("enter your choice: ")

print(f"comupter choice is {computer_choice} ")
print(f"user choice is {user_choice}")

if computer_choice==user_choice:
    print("tie")
elif computer_choice=="Rock" and user_choice=="Scissors":
    print("user lose")
elif computer_choice=="Scissors" and user_choice=="paper":
    print("user lose")

elif computer_choice=="paper" and user_choice=="Scissors":
    print("user lose")
else:
    print("user won")


#chamovweret erti mxaris mogeba da meore mxare shesabamisad wagbea inqeboda. anu aq cahvmoweret rodis vagebt da danarchen shemtxxvevashi anu vigebt

