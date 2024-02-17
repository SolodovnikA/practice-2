slvr=96
gld=slvr/16
total=int(input('Введите общую стоимость часов: '))
slvr_price=48
slvr_total=slvr*slvr_price
gld_price=(total-slvr_total)/gld
print(round(gld_price))