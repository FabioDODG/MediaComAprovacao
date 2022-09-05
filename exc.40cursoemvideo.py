import emoji
n1= float(input("Digite a média do primeiro semestre do aluno: "))
n2= float(input("Digite a média do segundo semestre do aluno: "))
n3= float(input("Digite a média do terceiro semestre do aluno: "))
n4= float(input("Digite a média do quarto semestre do aluno: "))
media= (n1+n2+n3+n4)/4
if media <5:
    print(emoji.emojize ("Aluno reprovado.:pensive: " ,language="alias"))
elif media >= 5 and media <=6.9:
    print(emoji.emojize ("Aluno em recuperação. :expressionless: " ,language="alias"))
else:
    print(emoji.emojize("Aluno aprovado!:sunglasses: ", language="alias"))    
   
