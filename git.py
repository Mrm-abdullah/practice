no = 8801700000001
for y in range(10):
    num = no
    file2 = ''
    for x in range(11):
        num2 = str(num)
        file2 += num2 + '\n'
        num += 1
    print(num)
    num3 = str(num)
    file = open(num3 + '.txt', 'w')
    file.write(file2)
    file.close()
    no = num
