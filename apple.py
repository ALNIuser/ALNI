number_input = input('Введите количество яблок ')
school_child = input('Введите количество учеников ')
print('Расчет равного количества яблок на каждого ученика')
print('Яблок в корзине', number_input)
print('Школьников', school_child, 'человек')
number_apple = int(number_input) // int(school_child)
if int(number_apple) < int(school_child):
    print('Количество яблок меньше количества учеников')
print("Каждый ученик получит по", number_apple, 'яблоку')
print('В корзине останется ', int(number_input) % int(school_child))
