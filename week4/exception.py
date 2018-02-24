def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        except Exception:
            print("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)


def fancy_divide2(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)


try:
    # raise Exception("5")
    try:
        raise Exception("5")
    # except ZeroDivisionError:
    #     print('nothing')
    finally:
        # a = 1/0
        print('finally')
except Exception as e:
    print('yes', e)

fancy_divide2([0, 2, 4], 0)

# NOTICE : the exception variable is only one and it can be covered by the later exception if it's not triggered immediately. At the last the program
# it will check if there is any exception not triggered . If so , it will trigger an error.
