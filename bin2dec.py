def main():
    print(bin2dec('100'))
def validate(bin):
        if bin == '':
            return False
        if len(bin) == 1:
            if bin == '1' or bin == '0':
                return True
            else:
                return False
        return validate(bin[0]) and validate(bin[1:])

# def trimZero(bin):
#     if len(bin) == 1:
#         return bin
#     if bin[0] == '1':
#         return bin
#     return trimZero(bin[1:])

def bin2dec(bin):
    if not validate(bin):
        print("The input binary is not valid")
        return False
    # bin = trimZero(bin)
    return calc(bin)

def calc(bin):
    n = int(bin[0])
    if len(bin) == 1:
       return n
    return n * pow(2,len(bin)-1) + calc(bin[1:])

if __name__ == '__main__':
    main()