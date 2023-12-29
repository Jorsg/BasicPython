
file = open("demo.txt", 'w')
file.write("wirte test")
file.close()

file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()

file = open("demo.txt", 'a')
file.write("wirte test other line")
file.close()

