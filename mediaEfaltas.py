nome = input('Digite o nome do aluno: ')

validNota = False
while validNota == False:
    notaProva1 = input('Digite a nota da prova 1: ')
    try:
        notaProva1 = float(notaProva1)
        if notaProva1 < 0 or notaProva1 > 10:
            print('Nota iválida. Valor deve ser entre 0 e 10.')
        else:
            validNota = True
    except:
        print("Nota inválida. Use apenas números e separe os decimais com '.'.")

validNota = False
while validNota == False:
    notaProva2 = input('Digite a nota da prova 2: ')
    try:
        notaProva2 = float(notaProva2)
        if notaProva2 < 0 or notaProva2 > 10:
            print('Nota iválida. Valor deve ser entre 0 e 10.')
        else:
            validNota = True
    except:
        print("Nota inválida. Use apenas números e separe os decimais com '.'.")

validFaltas = False
while validFaltas == False:
    faltas = input('Digite o total de faltas: ')
    try:
        faltas = float(faltas)
        if faltas < 0 or faltas > 20:
            print('Número de faltas inválido. Valor deve ser entre 0 e 20.')
        else:
            validFaltas = True
    except:
        print("Número de faltas inválido. Use apenas números e separe os decimais com '.'.")


media = (notaProva1+notaProva2)/2
assid = (20-faltas)/20

if media >= 6 and assid >= 0.7:
    resultado = 'Aprovado'

elif media < 6 and assid < 0.7:
    resultado = 'Reprovado por média e faltas'

elif media < 6:
    resultado = 'Reprovado por média'

elif assid < 0.7:
    resultado = 'Reprovado por faltas'

else:
    print('Erro')

print('Nome:',nome)
print('Media:',media)
print('Assiduidade:',str(assid*100)+'%')
print('Resultado:',resultado)
    
