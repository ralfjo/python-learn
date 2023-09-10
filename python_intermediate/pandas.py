import pandas as pd

data = pd.read_csv("username.csv")
# print(data)
# print(type(data))
# print(data.to_dict())
# print(type(data['Username']))
# print(data['Username'].to_list())

print(sum(data['Identifier'].to_list()))
print(data['Identifier'].max())

# to access to the column
print(data.Identifier)

# row data
print(data[data.Identifier == 9012])
print(data[data.Identifier == data.Identifier.max()])

