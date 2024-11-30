# List Comprehension
# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "ralfjo"
new_list = [letter for letter in name]
print(new_list)

# Python Sequences
# list, range, string, tuple

# range(1,5) [2,4,6,8]
list = [n * 2 for n in range(1,5)]
print(list)

names = ["Alex", "Beth","Caroline","Dave","Elanor","Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num_string) for num_string in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
result = [num for num in numbers if num % 2 == 0]
print(result)


# 데이터 중첩
# file1.txt와 file2.txt 안을 살펴보세요. 각 파일에는 각각 새 줄에 하나의 숫자가 포함되어 있습니다.
# file1과 file2에 공통으로 있는 숫자를 포함하는 result라는 리스트를 만들 것입니다.
# 예를 들어, file1.txt에 다음이 포함되어 있다면:
# 1 
# 2 
# 3
# 그리고 file2.txt에 다음이 포함되어 있다면:
# 2
# 3
# 4
# result = [2, 3]
# 중요: 출력은 문자열이 아닌 정수의 리스트여야 합니다!
# 반복문 대신 리스트 컴프리헨션을 사용해보세요.
# 1. 리스트 컴프리헨션을 시작하는 키워드 방식을 사용하고 관련 부분을 채워넣으세요.
# 2. 먼저 파일에서 읽어와 파일의 라인을 사용하여 리스트를 만들어야 합니다.
# 3. 이 방법은 매우 유용할 것입니다: https://www.w3schools.com/python/ref_file_readlines.asp 
# 4. 리스트에서 값이 존재하는지 확인할 수 있는 `in` 키워드를 사용할 수 있다는 것을 기억하세요.https://www.w3schools.com/python/ref_keyword_in.asp
# 5. 파이썬에서 문자열을 정수로 변환하는 데 int() 를 사용할 수 있다는 것을 기억하세요.

# with open("file1.txt") as file1:
#     list1 = file1.readlines()

# with open("file2.txt") as file2:
#     list2 = file2.readlines()

# result = [int(num) for num in list1 if num in list2]
 
# print(result)


import random
# Dictionary Comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# names = ["Alex", "Beth","Caroline","Dave","Elanor","Freddie"]
# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split(" ")}
# print(result)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)


# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# weather_f = {day:(temp * 9/5) + 32 for (day,temp) in weather_c.items()}

# print(weather_f)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
 
# weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}
 
# print(weather_f)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}

# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_dict_frame = pandas.DataFrame(student_dict)
# for (key, value) in student_dict_frame.items():
#     print(value)

#Loop through rows of a data frame
for (index, row) in student_dict_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
        
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}