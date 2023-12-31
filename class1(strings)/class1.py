#print("Hello World")
#print("Pakistan")

# """
# name:str="areeb"
# print(name)
# print(type(name))
# print(id(name))
# print([i for i in dir(name) if "__" not in i])
# """


#name:str = 700
#print(name)

#class2
# name :  str = "Areeb Ahmed"
# Education : str  = "SE"
# age : int = 22
# message : str = f""" name:%s \
# \nEducation:%s \
# \nage:%d """ %(name,Education,age)

# print(message)

# name :  str = "Areeb Ahmed"
# Education : str  = "SE"
# age : int = 22
# message : str = """name:{} \
# \nEducation:{} \
# \nage:{} """ .format(name,Education,age)

# print(message)

# print(ord('A'))

# r = [1,2,3,4,5]
# p = [88,87,90,89,99]
# g = ['A+','A','B','C','D']
# s = list(zip(r,p,g))
# sd = sorted(s,key=lambda x : x[0])
# print(sd)


# def square(nums):
#     return [num ** 2 for num in nums ]

# print(square(list(range(10))))




# from nptyping import NDArray, Shape, UInt64
# import numpy as np
# from typing import Any


# data : NDArray[Shape["20"],Any]  = np.arange(1,21)
# print(data)
# print(data[5:11])
# data[5:11] = 1000
# print(data)



# from nptyping import NDArray, Shape, UInt64
# import numpy as np
# from typing import Any

# data : NDArray[Shape["4"],Any] = np.array([1,5,7,8,10])

# d1 = data[data % 2 == 0]
# print(d1)


# from nptyping import NDArray, Shape, UInt64
# import numpy as np
# from typing import Any

# d1 : NDArray[Shape["Size,Size"],Any] =  np.arange(3*3).reshape(3,3)

# print(d1)

# d2 : NDArray[Shape["Size,Size"],Any] =  np.arange(5*3).reshape(5,3)

# print(d2)




# import pandas as pd 
# import pandera as pa

# a: pd.Series = pd.Series([1,2,3,4,5,6,7,8,9])

# print(a)
  

# import pandas as pd 
# import pandera as pa


# s1 : pd.Series = pd.Series([1,2,3,4,5])
# s2 : pd.Series = pd.Series([10,11,12,13,14])
# s3 : pd.Series = pd.Series(["Ali","Ahmed","Areeb"])

# df : pd.DataFrame = pd.DataFrame({"std_id" : s1,"score" : s2 , "name" : s3})
# print(df)



# import pandas as pd 
# import pandera as pa

# data : list[list[int]] = [[1,2,3],
#                           [4,5,6],
#                           [7,8,9]]

# df : pd.DataFrame = pd.DataFrame(data,columns=['A','B','C'],index=['1','2','3'])    

# print(df)   


import pandas as pd
import pandera as pa
import numpy as np
from nptyping import NDArray, Shape, Int64
total : int = 1000

d: NDArray[Shape[str(total)],Int64] = np.random.randint(80,100,(total,5))
d1 : pd.DataFrame = pd.DataFrame(d,columns=["a","b","c","d","e"])
print(d1)
print(d1["a"])
print(d1.a)