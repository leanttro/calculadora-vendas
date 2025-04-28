n = float(input("Digite o valor do produto: R$"))
p = int(input("Qual a quantidade de parcelas(até 3x): "))
n1 = n + (n*3/100)
n2 = n1 + (n1*4.20/100)
n3 = n1 + (n1*6.09/100)
n4 = n1 + (n1*7.01/100)

if (p == 0):
    print("Valor final da venda: R${}. \nCom o desconto de 3% para pagamento à vista, o valor fica R$ {}".format(n1,n))
elif (p==1):
    print("Valor final da venda: R${} (com juros de 4,20%),  \nTotal de {} parcela(s).format(n2,p)")
elif (p==2):
    print("Valor final da venda: R${} (com juros de 6,09%) \nTotal de {} parcela(s), sendo {}x de R${:.2f}.".format(n3,p,p,n3/2))
elif (p==3):
    print("Valor final da venda: R${} (com jutos de 7,01%), \nTotal de {} parcelas(s), sendo {}x de R${:.2f}.".format(n4,p,p,n4/3))
else: 
    print("Opção inválida! Digite apenas 0, 1, 2 ou 3.")
