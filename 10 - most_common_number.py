"""
დაწერეთ ფუნქცია common_number რომელსაც გადაეცემა ლისტი რომელიც შეიცავს რიცვხბეს
თქვენ უნდა დააბრუნოთ ის რიცხვი რომელიც ყველაზე ხშირად მეორდება


argument:
    [1, 3, 4, 2, 2, 1, 4, 4, 4]
output:
    4


*********************************** წარმატებები ***********************************
"""
def most_common_number(lst):
   
    first_dict={}
    #cast list in dictionary - key,values
    for char in lst:
        if char in first_dict:
            first_dict[char] = first_dict[char] + 1
        else:
            first_dict[char] = 1
   
    finnaly_key=0
    var_values=0

    for key, value in first_dict.items():
        if var_values <value:
            var_values=value
            finnaly_key=key
    return finnaly_key
  
number_list=[1, 3, 4, 2, 2, 1, 4, 4, 4,4,4]

call_function=most_common_number(number_list)
print(call_function)



