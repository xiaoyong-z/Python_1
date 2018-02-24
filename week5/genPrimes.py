def genPrime():
    number = 2
    while True:
        for i in range(number):
            if i == 0 or i == 1:
                continue
            if number % i == 0:
                break
        if i == number - 1:
            yield number
        number += 1
