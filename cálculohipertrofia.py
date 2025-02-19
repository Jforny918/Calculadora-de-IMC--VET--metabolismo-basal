print ('Cálculo de macronutrientes para hipertrofia e emagrecimento')
print ('='*40)
print ()
peso = float(input('Digite o seu peso: '))
vet = float(input('Você já sabe o seu VET (valor energético total)? Se sim, digite-o. Se não, digite 0: '))
print ()
if vet == 0:
    print ('Antes de calcular o VET, precisamos calcular o seu metabolismo basal!')
    print ()
    print ('='*40)
    print ()
    altura = float (input('Digite a sua altura: '))
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite o seu sexo (M/F): ')
    print ()
    if sexo == 'M':
        mb = 66 + (13.7*peso) + (5*altura) - (6.8*idade)
        print ('O seu metabolismo basal é: {:.2f}'.format(mb))
    else:
        mb= 665 + (9.6*peso)+(1.8*altura)-(4.7*idade)
        print ('O seu metabolismo basal é: {:.2f}'.format(mb))
    print ('='*40)
    print ('Agora vamos calcular o VET (Valor Energético Total)')
print ()
print ('Escolha o seu nível de atividade física:')
print ('1 - Sedentário')
print ('2 - Pouco ativo')
print ('3 - Ativo')
print ('4 - Muito ativo')
print ()
nível = int (input('Digite o número correspondente ao seu nível de atividade física: '))
print ()
if nível == 1:
    vet = mb*1.2
    print ('O seu VET é: {:.2f}'.format(vet))
elif nível == 2:
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
print ()
print ('Escolha o seu objetivo:')
print ('1 - Ganhar massa muscular')
print ('2 - Perder gordura')
print ()
objetivo = int(input('Digite o número correspondente ao seu objetivo: '))
print ()
if objetivo == 1:
    proteínas = peso*1.8
    carboidratos = peso*5
    gorduras = 0.25*vet
    print ('Para ganhar massa muscular, você deve consumir: ')
    print ()
    print ('{:.2f} kcal de proteínas'.format(proteínas))
    print ('{:.2f} kcal de carboidratos'.format(carboidratos))
    print ('{:.2f} kcal de gorduras'.format(gorduras))
else:
    proteínas = 0.3*vet
    carboidratos = 0.55*vet
    gorduras = 0.15*vet
    print ('Para perder gordura você deve consumir: ')
    print ('{:.2f} kcal de proteínas'.format(proteínas))
    print ('{:.2f} kcal de carboidratos'.format(carboidratos))
    print ('{:.2f} kcal de gorduras'.format(gorduras))
print ('='*40)