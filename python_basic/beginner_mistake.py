is_correct = True
# def func():
#     if is_correct == True:
#         return True
#     else:
#         return False
    
# better solution
def func():
    return is_correct
print(func())

total = 0
num_lst = [1,2,3,4,5]
# for n in num_lst:
#     total += n

# better solution
total = sum(num_lst)
print(total)

import math

minimum = math.inf
# for n in num_lst:
#     if n < minimum:
#         minimum = n

# better solution
minimum = min(num_lst)
maximum = max(num_lst)
print(minimum)

# total = 0
# for n in num_lst:
#     total += n
# avg = total / len(num_lst)

# better solution
import numpy as np
avg = np.mean(num_lst)
print(avg)

# sort vs sorted
l1 = [4,2,3,7,5]
print(l1.sort())
l2 = [6,4,2,8,3]
l2 = sorted(l2)
print(l2)

# case sensitive
google = 1
Google = 2
print(google)
print(Google)