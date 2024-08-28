#para a pessoa colocar o numero "input"
num1 = float(input("Digite o primeiro numero:"))
num2= float(input("Digite o segundo numero:"))
num3 = float(input("Digite o terceiro numero:"))

# '{} ,' é para evitar abrir "" 
print("Os numeros lidos são: {} , {} e {} " .format(num1, num2, num3))
def soma(num1,num2,num3):
    soma = num1 + num2 + num3
    print("A soma dos numeros é:", soma)
soma(num1, num2, num3)

def media( num1, num2, num3):
    media = (num1 + num2 + num3)/3
    print("A media dos numeros é: ", media)
media(num1, num2, num3)