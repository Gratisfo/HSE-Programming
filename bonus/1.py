list = []
while True:
    data = input()
    if not data:
        break
    data = float(data)
    list.append(data)
print('Среднее арифметическое:', sum(list)/len(list))
print('Мнимальное число:', min(list))
print('Максимальное число:', max(list))




  
