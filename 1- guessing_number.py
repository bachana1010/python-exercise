"""
დაწერეთ თამაში, რიცხვის გამოცნობა. სადაც წესები შემდეგია, კომპიუტერი ჩაიფიქრებს რიცხვს შემთხვევითობის პრინციპით 0 დამ 10 მდე
და შემდეგ მომხმარებელმა უნდა გამოიცნოს ჩაფიქრებული რიცხვი, თუმცა მხოლოდ 2 ცდა აქვს. თუ ვერცერთ ცდაზე ვერ გამოიცნო დაბეჭდეთ you lose
ხოლო თუ გამოიცნო დაბეჭდეთ you are wanga რადგან 2 ცდაზე რთულია რიცხვის გამოცნობა ამიტომ მომხმარებელს ცოტათი დავეხმაროთ.
თუ პირველ ცდაზე შემოიყვანა რიცხვი რომელიც ჩაფიქრებულზე ნაკლებია დაბეჭდეთ your choice is lower რათა მივანიშნოთ რომ
ჩაფიქრებული რიცხვი უფრო მეტია და დავეხმაროთ გამოცნობაში ხოლო თუ შემოყვანილი რიცხვი უფრო მეტია ვიდრე ჩაფიქრებული დაბეჭდეთ
your choice is higher

P.S
    პრინტები დაწერეთ როგორც გინდათ ეს ამოცანა ტესტებზე არ შემოწმდება ამიტომ ეცადეთ უბრალოდ ლამაზად დაბეჭდოთ

    random.randint(start, stop) start იდან stop შუალედში რანდომ რიცხვს დააბრუნებს

*********************************** წარმატებები ***********************************
"""
import random

wanga="""
***********************
*   W                 *
*      A              *
*         N           *
*            G        *
*               A     *
***********************
"""

lose="""
***********************
*   l                 *
*      o              *
*         s           *
*            e        *                   
***********************
"""
number_of_trials = 2

number_random=random.randint(0,10)

for idx in range(0, number_of_trials ):
    customer_input_number =int(input("write number: "))
    if customer_input_number == number_random:
        print(wanga)
        break
    elif  idx ==number_of_trials-1:
        print(lose)
        break
    elif customer_input_number >number_random:
        print("your choise is higher")
    elif customer_input_number<number_random:
        print("your choise is lower")
 

    
