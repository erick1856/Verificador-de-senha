# Validador de senha

'''
Niveis de segurança e suas descriçoes

Muito Fraca = menos de 8 caracteres
Fraca = mais de 8 caracteres apenas minúsculas ou maiúsculas
Média = 8 caracteres com minúsculas E maiúsculas
Forte = 8 caracteres com minúsculas E maiúsculas E números
Muito Forte = 8 caracteres com minúsculas E maiúsculas E números E caracter especial
'''

def recomeco():
    reset = int(input('Quer recomeçar? [1]Sim [2]Não\n'))
    if reset == 1:
        main()

def main():
    senha = list(input('Digite sua senha:\n'))
    tamanho_senha = len(senha)
    estado = ''
    maiúscula = False
    minúscula = False
    numero = False
    lista_especial = ['!', '@', '#', '$', '%', '&','*', '.', ',', '<', '>', '/', '?']
    caracter_especial = False


    if tamanho_senha < 8:
        estado = 'Muito Fraca'

    elif tamanho_senha >= 8:
        estado = 'Fraca'

    for caracter in senha:
        if caracter.isupper() and estado == 'Fraca':
            maiúscula = True
        if caracter.islower() and estado == 'Fraca':
            minúscula = True
        
    if maiúscula and minúscula:
        estado = 'Média'

    for caracter in senha:
        if caracter.isnumeric():
            numero = True

    if tamanho_senha > 8 and maiúscula and minúscula and numero:
        estado = 'Forte'

    for caracter in senha:
        if caracter in lista_especial:
            caracter_especial = True

        if tamanho_senha > 8 and maiúscula and minúscula and numero and caracter_especial:
            estado = 'Muito Forte'
    print(estado)
    recomeco()

if __name__ == '__main__':
    main()