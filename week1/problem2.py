s = 'robobobogibobdbobob'
num = 0
for i in range(len(s) - 2):
    if s[i] == 'b':
        if s[i + 1] == 'o':
            if s[i + 2] == 'b':
                num += 1
print("Number of times bob occurs is: " + str(num))