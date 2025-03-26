def print_formatted(number):
    largura = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        dec = str(i).rjust(largura)
        octal = oct(i)[2:].rjust(largura)
        hexa = hex(i)[2:].upper().rjust(largura)
        binario = bin(i)[2:].rjust(largura)
        print(f"{dec} {octal} {hexa} {binario}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
