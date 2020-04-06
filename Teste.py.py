salariominimo= float(input("digite o salario minimo:\n"))
ltpreco= salariominimo*0.002
aguaconsumida= float(input("digite a quantidade de agua consumida em litros:\n"))
contadeagua= ltpreco*aguaconsumida
desconto= contadeagua*0.15
contacomdesconto= contadeagua-desconto
print ("O valor da conta de agua é: R$", contadeagua)
print ("O valor a ser pago com 15% de desconto é: R$", contacomdesconto)
