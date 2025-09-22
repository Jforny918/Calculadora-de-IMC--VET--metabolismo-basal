print ('Cálculo do metabolismo basal')
print ('='*40)
peso = float(input('Digite o seu peso: '))
altura = float (input('Digite a sua altura: '))
idade = int(input('Digite a sua idade: '))
sexo = input('Digite o seu sexo (M/F): ')
if sexo == 'M':
    mb = 66 + (13.7*peso) + (5*altura) - (6.8*idade)
    print ('O seu metabolismo basal é: {:.2f}'.format(mb))
else:
    mb= 665 + (9.6*peso)+(1.8*altura)-(4.7*idade)
    print ('O seu metabolismo basal é: {:.2f}'.format(mb))
print ('='*40)
print ('Agora vamos calcular o VET (Valor Energético Total)')
print ('='*40)
print ('Escolha o seu nível de atividade física:')
print ('1 - Sedentário')
print ('2 - Pouco ativo')
print ('3 - Ativo')
print ('4 - Muito ativo') 
print ()
nível = int (input('Digite o número correspondente ao seu nível de atividade física: '))
if nível == 1:
    vet = mb*1.2
    print ('O seu VET é: {:.2f}'.format(vet))
elif nível == 2:  # elif é a abreviação de else if
    vet = mb*1.56
    print ('O seu VET é {:.2f}'.format(vet))
elif nível == 3:
    vet = mb*1.64
    print ('O seu VET é {:.2f}'.format(vet))
else:
    vet = mb*1.82
    print ('O seu VET é {:.2f}'.format(vet))
print ('='*40) 
print ('AGORA VOCÊ JÁ SABE O SEU VET!')
print ('='*40)

