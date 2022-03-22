

"""გვაქვს 1,5,10,20 და 50 თეთრიანი მონეტები. დაწერეთ ფუნქცია, რომელსაც გადაეცემა თანხა (თეთრებში) და აბრუნებს მონეტების მინიმალურ რაოდენობას, რომლითაც
 შეგვიძლია ეს თანხა დავახურდაოთ.
მაგ: ყველაზე მოკლე გზა 70 თეთრის დასაშლელად არის 50+20 თეთრიანი მონეტები, შესაბამისად ფუნქციამ უნდა დააბრუნოს 2."""




list_cupiurs=[50,20,10,5,1]
dic_cupiurs={}
customer_number=int(input("write cent: "))

def cupiurs (customer_number):

    total=0
    for i in list_cupiurs:
        quantity=customer_number//i
        remainder=customer_number%i
        total=total+quantity

        customer_number=remainder

        #add in dictionary
        if quantity !=0:
            dic_cupiurs[i]=quantity
        
        #chek if customer number =0
        if customer_number ==0:
            break

    return dic_cupiurs

finaly=cupiurs(customer_number)
print(finaly)


