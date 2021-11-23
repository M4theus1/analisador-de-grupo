totidade = 0
mediaidade = 0
idadevelho = 0
nomevelho = ''
totmulheressub20 = 0
for c in range (1, 5):
    print('----- {}a PESSOA -----'.format(c))
    nome = str(input('Digite o seu nome: ')).split()
    idade = int(input('Digite sua idade: '))
    #Agora, calculando o total da idade do grupo e tirando a média
    totidade = totidade + idade
    mediaidade = totidade/4
    sexo = str(input('Informe seu sexo [M/F]: '))
    #Condicional para nome do homem mais velho
    if c == 1 and sexo in 'Mm':
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    #Condicional para total de mulheres com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        totmulheressub20 = totmulheressub20 + 1
print(' ')
print('A média da idade do grupo é de: {}'.format(mediaidade))
print('O nome do homem mais velho é: {}'.format(nomevelho[0]))
print('O total de mulheres com menos de 20 anos é de: {}'.format(totmulheressub20))
