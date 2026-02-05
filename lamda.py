
values=[1,2,3,4,5,6,7,8]
print(list(map(lambda x:x *2,values)))
print(list(filter(lambda x:x %2 ==0,values)))
from functools import reduce
reduce(lambda x,y:x+y,values)


