input_string = input()

def Rot13(s):
    res = ''
    for i in s:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            if ord(i)+13 > ord('Z'):
                res += chr(ord(i) - 13)
            else:
                res += chr(ord(i) + 13)
        elif ord(i) >= ord('a') and ord(i) <= ord('z'):
            if ord(i)+13 > ord('z'):
                res += chr(ord(i) - 13)
            else:
                res += chr(ord(i) + 13)
        else:
            res += i
    
    return res

print(Rot13(input_string))