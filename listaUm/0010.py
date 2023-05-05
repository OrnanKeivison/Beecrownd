produto1 = input().split(" ")
produto2 = input().split(" ")

codgo1, quantidade1, valor1 = produto1
codgo2, quantidade2, valor2 = produto2

total = (int(quantidade1) * float(valor1)) + (int(quantidade2) * float(valor2))

print("VALOR A PAGAR: R$ %0.2f" %total)