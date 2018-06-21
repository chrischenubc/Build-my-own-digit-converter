def main():
    n = -2
    bin = dec2bin(n)
    print(bin)

def dec2bin(n):
    if n == 0 :
        return '0'
    return div_by_2(n,'')


def div_by_2(n,rep):
    if n <= 0:
        return rep
    if n % 2 == 1:
        return div_by_2(n//2, '1' + rep)
    if n % 2 == 0:
        return div_by_2(n//2, '0' + rep)


if __name__ == '__main__':
    main()