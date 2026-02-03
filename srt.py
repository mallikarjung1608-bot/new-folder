total_bill = float(input("enter the total bill amount :"))
num_people = int(input("enter the number of people: "))
share_per_person = total_bill/ num_people
print(f"total bill: ${total_bill:.2f}. each person pays :${share_per_person:.22f}")
print(f"data type of total_bill : {type(total_bill)}")
print(f"data type of num_people :{type(num_people)}")
print(f"data type of share_per_person :{type(share_per_person)}")