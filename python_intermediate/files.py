# file management
file = open("README.txt","r")
print(file.read())
file.close()

# no close any more
with open("README.txt","r") as file:
    print(file.read())

# write - 'w' overwrite, 'a' append
with open("WRITEME.txt","w") as file:
    print(file.write("Thanks"))