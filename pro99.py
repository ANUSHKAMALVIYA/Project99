name = input("Enter your name: ")


width = len(name) * 2 + 1


for i in range(len(name)):
    line = ["*"] * width
    line[i * 2] = name[i]
    print(" ".join(line))
