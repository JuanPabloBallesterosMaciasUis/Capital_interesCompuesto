# Ejercicio 26 : Con el capital, en cuantos meses se duplica.

print("-------------------------------")
print("--CAPITAL--INTERES-COMPUESTO---")
print("-------------------------------")

# input
c = int(input("Dijite la capital:"))
c1 = c
i = 0

#process
while c1<=c*2:
    c1 = c1 + c1 * 0.05
    i = i + 1

#output

print("Los",c,"de capital,se duplica en",i,"meses, teniendo asi ahora",c1)