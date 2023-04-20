str_1 = 'some str1\n'
str_2 = 'some str2\n'
str_3 = 'some str3\n'
str_4 = 'some str4\n'

with open('some_file.txt', 'w') as f:
    f.write(str_1)
    f.write(str_2)


with open('some_file.txt', 'a') as f:
    f.write(str_3)
    f.write(str_4)
