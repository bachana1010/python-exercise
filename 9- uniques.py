"""
დაწერეთ ფუნქცია flatten_only_unique რომელსაც გადაეცემა ლისტი რომელიც შეიცავს ტაპლებს
თქვენ უნდა დააბრუნოთ ლისტი რომელიც შეიცავს ტაპლებიდან ამოღებულ უნიკალურ რიცხვებს


argument:
    [(1,3,4), (1,1,1), (4,5,5)]
output:
    [1, 3, 4, 5]

P.S
    ფუნქცია გამოიძახება შეგიძლიათ caller ფუნქციიდან
    ფუნქციას დაარქვით ზუსტად ის სახელი რაც პირობაშია მოცემული და გადაეცით 2 არგუმენტი  სხვა შემთხვევაში ტესტები არ იმუშავებს

*********************************** წარმატებები ***********************************
"""
# define function flatten_only_unique


# call your function and print some examples
def caller():
    lst=[(1,3,4), (1,1,1), (4,5,5)]
    setT=set()

    for tuples_idx in range(len(lst)):
        for item_idx in range(len(lst[tuples_idx])):
            setT.add((lst[item_idx][tuples_idx]))

    print(setT)
    pass


if __name__ == "__main__":
    caller()





