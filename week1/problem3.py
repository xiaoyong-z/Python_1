s = 'azcbobobegghal'
num = 0
length2 = 0
length = len(s)
st = s[0]
while num + 1 < length:
    if s[num] <= s[num+1]:
        t = s[num] + s[num+1]
        num += 1
        while num + 1 < length and s[num] <= s[num+1]:
            t += s[num+1]
            num += 1
        if len(t) > length2:
            length2 = len(t)
            st = t
    else:
        num += 1
print("Longest substring in alphabetical order is: " + st)