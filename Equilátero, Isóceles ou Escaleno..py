a = int(input('\033[36mDígite o valor da base: '))
b = int(input('Dígite o valor da lateral: '))
c = int(input('Da outra: '))
if a < b + c and b < a + c and c < b + c:
    print('\033[34mÉ possivel foramar um triângulo')
    if a == b and b== c:
        print('\033[31mÉ um triângulo Equilátero!')
    elif a == b or b == c or c == a:
        print('\033[31mÉ um triângulo Isóceles!')
    elif a != b and a != c:
        print('\033[31mÉ um triângulo Escaleno!')
else:
    print('\033[31m Não é possivel formar um triângulo!\033[m')