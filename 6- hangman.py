"""
დაწერეთ ეგრეთწოდებული ჩამოხრჩობანა (hangman).
პროცესი შემდეგია პროგრამა შემთხვევითობის პრინციპით ირჩევს რაიმე სიტყვას WORDS ლისტიდან (თუ გნებავთ თქვენი ლისტრი გააკეთეთ სასურველი სიტყვებით)
და მომხამრებელს აძლევს საშუალებას რომ გამოიცნოს. მას შემოყავს ასოები რიგ რიგობით და თუ ეს ასო არის სიტყვაში უნდა შეავსოთ ის და აჩვენოთ
თუ არ არის მაშინ მისი სიცოცხლეების რაოდენობა (LIFE_NUMBER) ერთით შემცირდება და როდესაც ყველა სიცოცხლეს დახარჯავს ის წააგებს თამაშს.
ხოლო თუ მანამდე შეძლო მთლიანი სიტყვის გამოცნობა მაშინ მომხმარებელი მოგებულია. წაგების ან მოგების შემდეგ მომხმარებელს კითხეთ სურს თუ არა კიდევ თამაში,
თუ სურს, თავიდან აირჩიეთ სიტყვა და გააგრძელეთ თამაში თუ არადა პროგრამამ დაასრულოს მუშაობა.
გაითვალისწინეთ რომ შემოყვანილი ასო თუ რამდენიმეჯერ მეორდება სიტყვაში ყველა უნდა შეავსოთ.
ასევე მოხმარებელს უნდა შეეძლოს დაინახოს სიტყვის ზომა და გამოცნობილი ასოები ვიზუალურად როგორც მაგალითშია მოცემული.



input:
    დავუშვათ რომ კომპიუტერმა აირჩია disappear
    m
output:
    _________


input:
    დავუშვათ რომ კომპიუტერმა აირჩია disappear
    a
output:
    ___a___a_


P.S
    პრინტები დაწერეთ როგორც გინდათ ეს ამოცანა ტესტებზე არ შემოწმდება ამიტომ ეცადეთ უბრალოდ ლამაზად დაბეჭდოთ

    random.randint(start, stop) start იდან stop შუალედში რანდომ რიცხვს დააბრუნებს
    გაიხსენეთ რას აკეთებდა join() split() მეთოდები
    გამოიყენეთ ფუნქციები და აუცილებლად დაწერეთ კომენტარები
    

*********************************** წარმატებები ***********************************
"""
import random


LIFE_NUMBER = 3


#random sityvebis archeva
def random_word_make(word_random):

   
    return random.choice(word_random)

WORDS = ["aunt", "strange", "broad", "stale", "craven", "disappear", "wistful", "rustic", "bushes", "splendid",
         "aftermath", "shallow", "demonic", "vessel", "tenuous", "hungry", "possible", "wasteful", "finicky", "bounce"
         "scissors", "spectacular", "adamant", "knotty", "chief", "locket", "telling", "harbor", "stick", "dislike"]

random_result=random_word_make(WORDS)

print(random_result)



#random sityvis shesabamisi  fifqebiani stringis sheqmna

def lower_flake_list(flake):
    empty=" "
    i=0
    for i in range(len(flake)):
        empty= empty + "*"
        i=i+1
    return empty

str_flake=lower_flake_list(random_result)
print(str_flake)



# momxmareblis shemoyvanili asos shedareba random_resulttan

def compare_word_letter(rand_word,flake):
    str_flake1=list(flake)
    str_flake1=str_flake1[1:]
    str_word=list(rand_word)
    print("play hangman")
    LIFE_NUMBER = 3
    print("your life is : ", LIFE_NUMBER)
    i=0
    while True  and LIFE_NUMBER > 0:
        i=0
        customer_input=input("write one letter: ")
        customer_input.lower
        if len(customer_input)!=1:
            LIFE_NUMBER-=1
            print("Be careful, enter one letter. you loose life number. your life number: ", LIFE_NUMBER)
        else:

            if rand_word.find(customer_input) != -1:
                print("********congratulation, you are correct***********")
                if customer_input in str_flake1:
                    LIFE_NUMBER-=1
                    print("This letter is repeated. you loose life number. your life number: ", LIFE_NUMBER)

                while i < len(str_word):
                    if str_word[i]==customer_input:
                        str_flake1[i]=customer_input
                        print("".join(str_flake1))
                    i=i+1
            elif rand_word.find(customer_input) == -1 :
                LIFE_NUMBER -= 1
                print(customer_input," is not correct letter.", "your life number:", LIFE_NUMBER)
              

        if LIFE_NUMBER==0:
            print("you loose")
            break

        if "*" not in str_flake1:
            print("you are winner")
            return "".join(str_flake1)
        

compare_word_letter(random_result,str_flake)






