# МАКСИМАЛЬНОЕ КОЛИЧЕСТВО ПОДРЯД ИДУЩИХ ПАР СИМВОЛОВ
f = open('24_open_kim2022.txt').readline()

# ИДЕЯ В ТОМ, ЧТОБЫ ВСЕ CB ИЛИ ЖЕ AB ЗАМЕНИТЬ НА ЧТО-ТО ОДНО -> replace('CB', 'AB')
# ДЕЛАЕМ ВСЕ ПАРЫ ОДНОРОДНЫМИ 
file = f.replace('CB', 'AB')
for i in range(100000):    # ПОДСЧЕТ КОЛИЧСТВА ИДУЩИХ !ПОДРЯД! СИМВОЛОВ AB
    if i*'AB' in file:
        print(i)