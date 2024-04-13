#Practica 4

#Ejercicio 3

gametag = {
        "Juan":1500000,
        "Pedro":2000000,
        "Maria":1800000,
        "Luis":2200000,
        "Ana":1900000
    }


def money(pay):
    nums = [50000,20000,10000,5000,2000,1000,500]
    detail = {denom: pay // denom for denom in nums}
    return detail



def total_pay(x):
    pay = sum(x.values())
    return pay

all_money = total_pay(gametag)

print(f"Plata en el banco: {all_money}")
print(f"Billetes y monedas:")
for bill, x in money(all_money).items():
    print(f"{x} billetes de {bill}")
