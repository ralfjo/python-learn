with open("file1.txt") as file1:
    list1 = file1.readlines()
    list1 = [int(num.strip()) for num in list1]
    print(list1)
with open("file2.txt") as file2:
    list2 = file2.readlines()
    list2 = [int(num.strip()) for num in list2]
    print(list2)
result = [int(num) for num in list1 if num in list2]
 
print(result)
