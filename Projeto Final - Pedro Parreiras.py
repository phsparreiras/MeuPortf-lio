aprovadosM=0
aprovadosF=0
exameM=0
exameF=0
reprovadosM=0
reprovadosF=0
alunosTotal=0

#Validação inicial.
lançamento = input('Deseja iniciar o lançamento de notas (S/N)? ').upper()
while (lançamento != 'S' and lançamento!='N'):
    print ('Opção Inválida')
    lançamento = input('Informe S-Sim ou N-Não: ').upper()

#Inserindo nome e validando o sexo
while (lançamento == 'S'):
    alunosTotal +=1
    nome = input('Informe nome do aluno: ')

    sexo = input('Informe sexo do aluno (M-Masculino ou F-Feminino): ').upper()
    while (sexo != 'M' and sexo != 'F'):
        print('Opção Inválida')
        sexo = input('Informe M-Masculino ou F-Feminino: ').upper()

#Informando as notas por sexo Masculino.
    if (sexo == 'M'):
        for cont in range(1, 4):
            if cont == 1:
                nota1 = int(input('Informe N1: '))
                while nota1 < 0 or nota1 > 10:
                    nota1 = int(input('N1 inválido, valor deve ser entre 0 e 10: '))
            elif cont == 2:
                nota2 = int(input('Informe N2: '))
                while nota2 < 0 or nota2 > 10:
                    nota2 = int(input('N2 inválido, valor deve ser entre 0 e 10: '))
            else:
                nota3 = int(input('Informe N3: '))
                while nota3 < 0 or nota3 > 10:
                    nota3 = int(input('N3 inválido, valor deve ser entre 0 e 10: '))

        media = (nota1 + nota2 + nota3) / 3
        print(str(media))
        if media >= 7:
            aprovadosM += 1
        elif media >= 4:
            exameM += 1
        else:
            reprovadosM += 1

#Informando as notas por sexo Feminino.
    else:
        for cont in range(1, 4):
            if cont == 1:
                nota1 = int(input('Informe N1: '))
                while nota1 < 0 or nota1 > 10:
                    nota1 = int(input('N1 inválido, valor deve ser entre 0 e 10: '))
            elif cont == 2:
                nota2 = int(input('Informe N2: '))
                while nota2 < 0 or nota2 > 10:
                    nota2 = int(input('N2 inválido, valor deve ser entre 0 e 10: '))
            else:
                nota3 = int(input('Informe N3: '))
                while nota3 < 0 or nota3 > 10:
                    nota3 = int(input('N3 inválido, valor deve ser entre 0 e 10: '))

        media = (nota1 + nota2 + nota3) / 3
        print(str(media))
        if media >= 7:
            aprovadosF += 1
        elif media >= 4:
            exameF += 1
        else:
            reprovadosF += 1

#Fechando o while inicial e mostrando os valores finais.
    lançamento = input('Deseja fazer outro lançamento de notas (S/N)? ').upper()
    while (lançamento != 'S' and lançamento != 'N'):
        print('Opção Inválida')
        lançamento = input('Informe S-Sim ou N-Não: ').upper()

else:
    print('Lancamentos Finalizados')


if (lançamento =='S')
    print('Porcentagem de alunos aprovados: ', ((aprovadosF+aprovadosM)*100)/alunosTotal, '%')
    print('Porcentagem de alunos de exame: ', ((exameF+exameM)*100)/alunosTotal, '%')
    print('Porcentagem de alunos reporvados: ', ((reprovadosF+reprovadosM)*100)/alunosTotal, '%')
    print('Total de alunos do sexo masculino aprovados: ' + str(aprovadosM))
    print('Total de alunos do sexo feminino aprovados: ' + str(aprovadosF))
    print('Total de alunos do sexo masculino de Exame: ' + str(exameM))
    print('Total de alunos do sexo feminino de Exame: ' + str(exameF))
    print('Total de alunos do sexo masculino Reprovados: ' + str(reprovadosM))
    print('Total de alunos do sexo feminino Reprovados: ' + str(reprovadosF))

    print('*****Fim da Aplicação*****')




