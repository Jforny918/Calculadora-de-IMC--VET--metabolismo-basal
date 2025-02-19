print ('Cálculo de macronutrientes para hipertrofia e emagrecimento')
print ('='*40)
print ()
peso = float(input('Digite o seu peso: '))
vet = float(input('Digite o seu VET: '))
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