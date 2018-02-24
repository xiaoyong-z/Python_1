trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    us_num = int(us_num)
    units = str(us_num % 10)
    tens = str(us_num // 10)
    if us_num <= 10:
        string = trans[str(us_num)]
    elif us_num <= 19:
        string = trans["10"] + ' ' + trans[units]
    else:
        if units == "0":
            string = trans[tens] + ' ' + trans["10"]
        else:
            string = trans[tens] + ' ' + trans["10"] + ' ' + trans[units]
    return string

print(convert_to_mandarin('36'))