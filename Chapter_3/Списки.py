# Списки представляют собой упорядоченные наборы данных

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0])

# В Python также существует специальный синтаксис для обращения к последнему элементу списка - это индекс –1
# print(f'Result: {bicycles[-1].title()}')


# Срезы
# result ['trek', 'cannondale'] - срез начиная со 2го элемента
# print(bicycles[:2])

str_list = ['box', 'car', 'factory', 'worker']
int_list = [1, 2, 3, 4, 5]

# B Объеденить списки можно просто применив оператор сложения.
concat_list = str_list + int_list
# print(concat_list)
# result ['box', 'car', 'factory', 'worker', 1, 2, 3, 4, 5]

# B .append() - позволяет добавлять элементы в конец list
str_list.append('add new item')
print(str_list)
# result ['box', 'car', 'factory', 'worker', 'add new item']
