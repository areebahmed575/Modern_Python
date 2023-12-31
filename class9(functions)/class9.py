# def sum(*nums)-> int:
#     print(nums,type(nums))
#     total = 0 
#     for  i in nums:
#         total += i
#     return total    

# sum(1,2,3,4,5,6,7,8,9,10)

from typing import Dict,Tuple
def my_function(a:int, b:int, *abc:int, **xyz:int)->None:
    print(a,b, abc, xyz)

my_function(1,2, 7,9,9,9, c=20, d= 30, x=100)