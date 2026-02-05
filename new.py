number=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print("orginal list: ",number)
number.sort()
print("sorted list: ",number)
number.append(1)
print("after appending 1: ",number)
number.remove(5)
print("after removing 5: ",number)
number.pop()
print("after poping : ",number)
number.reverse()
print("after reversing: ",number)
number.clear()
print("after clearing: ",number)


inventory=["apple","bannana","carrots","dates"]
print("current inventory")
inventory.append("eggs")
print("after appending egg",inventory)
inventory.remove("bannana")
print("after removing bannana",inventory)

