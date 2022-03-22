"""
დაწერეთ ფუნქცია სახელად char_in_word რომელსაც გადაეცემა ორი სტრინგი. პირველი არის სიტყვა ხოლო მეორე ქარაქტერი ანუ ასო.
და მანდ უნდა ნახოს ეს სიტყვა შეიცავს თუ არა მოცემულ ასოს თუ შეიცავს დააბრუნებს True თუ არადა დააბრუნებს False
caller ფუნქციაში დაწერეთ რომ მომხმარებელმა შემოიყვანოს სტრინგი და ასო და შემდეგ გადაეცით ის char_in_word ფუნქციას და დაბრუნებული შედეგი დაბეჭდეთ


argument:
    Python
    p
output:
    True

argument:
    Python
    j
output:
    False

P.S
    გაიხსენეთ in როგორ მუშაობდა სტრინგების შემთხვევაში  5 in [10, 5, 20] არის True
    ასევე შეიძლება გამოგადგეთ ბრძანება find

    ფუნქციის განსაზღვრება ხდება def ის გამოყენებით
    def function_name(argument):
        return something

    ფუნქციას დაარქვით ზუსტად ის სახელი რაც პირობაშია მოცემული სხვა შემთხვევაში ტესტები არ იმუშავებს

*********************************** წარმატებები ***********************************
"""

# define function char_in_word

def char_in_word(customer_t,customer_w):
    if customer_t.find(customer_w)==-1:
        return False
    else:
        return True



# call your function and print some examples
def caller():
    customer_input1=input("write text: ")
    customer_input2=input("write word: ")
    call_function=char_in_word(customer_input1,customer_input2)
    print(call_function)
    pass


if __name__ == "__main__":
    caller()


