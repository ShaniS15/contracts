# Задание 1: Конвертация криптовалют
btc = int(input('Количество биткоинов:'))
price = int(input('Tекущий курс биткоина в долларах:'))
print(f'Cумма в долларах: {btc * price} \n')


# Задание 2: Вычисление прибыли от продажи криптовалюты
buy_price = int(input('Цена покупки биткоина:'))
sale_price = int(input('Цена продажи биткоина:'))
number_of_bitcoins =int(input('Количество биткоинов:'))
total = (sale_price - buy_price) * number_of_bitcoins
print(f'Прибыль или убыток от продажи: {total} \n')


# Задание 3: Вычисление комиссии биржи
transaction_amount = int(input('Cумма сделки:'))
percent_commission = int(input('Процент комиссии биржи:'))
commission = transaction_amount * percent_commission / 100
print(f'Сумма комиссии: {commission} \n')


# Задание 4: Вычисление средней стоимости криптовалюты
price_1d = int(input('Cтоимость биткоина 1-ый день:'))
price_2d = int(input('Cтоимость биткоина 2-ой день:'))
price_3d = int(input('Cтоимость биткоина 3-ий день:'))
average_price = (price_1d + price_2d + price_3d) / 3
print(f'Cредняя стоимость биткоина: {average_price} \n')