from itertools import product
digit = [str(i) for i in range(1,9)] # делаем список от 1 до 8 и формате str
Znaki = ["+","-",""]
var = []
for i in digit:
    for j in Znaki:
        var.append(i+j) # складываем все возможные комбинации из знаков
count = 0
var2 = []
while count + 3 <= len(var):
    var2.append(var[count:count+3])
    count += 3 #по сколько все возможных комбинаций из знаков всего 3 разделяем их в группу по 3 (список в списке)

var3 = []
x = list(product(range(3),repeat = 8)) # на этом этапе пришлось использовать функцию product, были попытки обойтись бех product, все возможные комбинации
print(var2)
for i in range(len(x)): # бегаем по массиву и подставляем все возможные комбинации которые сделали productom
    var3.append(var2[0][x[i][0]]+var2[1][x[i][1]]+var2[2][x[i][2]]+var2[3][x[i][3]]+var2[4][x[i][4]]+var2[5][x[i][5]]+var2[6][x[i][6]]+var2[7][x[i][7]]+"9")
var4 = []
for i in range(len(var3)):
    if eval(var3[i]) == 100:
        var4.append(var3[i]) # далее сравниваем в элементы массива с суммой 100 если TRUE то добавляем в новый массив , все задача выполнена ! 

for i in var4:
    print(i, " = ", 100)
print("всего комбинаций: ", len(var4))
