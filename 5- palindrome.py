"""
დაწერეთ ფუნქცია სახელად is_palindrome რომელსაც გადაეცემა ერთი არგუმენტი ამ შემთხვევაში ტექსტი ანუ სტრინგი
და ნახავს არის თუ არა ის პალინდრომი. პალინდრომია სტრინგი თუ ის ორივე მხრიდან ერთნაირად იკითხება
ანუ თუ მას შევატრიალებთ მივიღებთ იგივე სიტყვას მაგალითად madam, level, radar და ასე შემდეგ.
თუ სიტყვა პალინდრომია ფუნქციამ უნდა დააბრუნოს True თუ არადა დააბრუნოს False.
caller ფუნქციაში დაწერეთ რომ მომხმარებელმა შემოიყვანოს სტრინგი და შემდეგ გადაეცით ის is_palindrome ფუნქციას და დაბრუნებული შედეგი დაბეჭდეთ

argument:
    level
output:
    True

argument:
    hello
output:
    False

P.S
    ფუნქციის განსაზღვრება ხდება def ის გამოყენებით
    def function_name(argument):
        return something

    ფუნქციას დაარქვით ზუსტად ის სახელი რაც პირობაშია მოცემული სხვა შემთხვევაში ტესტები არ იმუშავებს

*********************************** წარმატებები ***********************************
"""

#first solution
# define function is_palindrome

def word_opposite(word):
    return word[::-1]


def is_palindrome(customer):
    opposite_word=word_opposite(customer)
    i=0
    chek=""
    while i < len(opposite_word):
        if customer[i] == opposite_word[i]:
            chek=chek+opposite_word[i]
        else:
            return False
        if chek==customer:
            return True
       
        
        i=i+1




# call your function and print some examples
def caller():
    inp=input("write word: ")
    pali=is_palindrome(inp)
    print(pali)

    
 
    
    pass


if __name__ == "__main__":
    caller()


#second solution

# def is_palindrome(customer):
#     empty_string=""

#     for i in customer:
#         empty_string=i + empty_string
#     if empty_string==customer:
#         print("result is : " ,empty_string)
#         return True
#     else:
#         print("result is : " ,empty_string)

#         return False


# inp=input("write word: ")
# pali=is_palindrome(inp)
# print(pali)
