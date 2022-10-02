
# 1.
name = input("What is your name: ")
filename = name + ".txt"
out_file = open(filename, 'w',)
out_file.write(name)
out_file.close()


# 2.
name = input("What is your name: ")
filename = name + ".txt"
in_file = open(filename, 'r',)
print(f"You're name is {in_file.read()}")
in_file.close()


# 3.
total = 0
in_file = open("numbers.txt", 'r')
for line in in_file.readlines()[0:2]:
    total += int(line)
in_file.close()
print(total)


# 4.
total = 0
in_file = open("numbers.txt", 'r')
for line in in_file.read().strip():
    total += int(line)
in_file.close()
print(total)
