str=input("Введите строку") #вводим строку
print("длина строки:", len(str)) #с помощью функции len выводим длину строки 
gl=0 #присваиваем переменной значение 
sogl=0 #присваиваем переменной значение 
for i in str: #создаем цикл перебирающий каждый элемент
    if i=="а"or i=="о"or i=="у"or i=="ы"or i=="э"or i=="я"or i=="е"or i=="ё"or i=="ю"or i=="и": #условие для цикла которое отбирает гласные буквы
        gl+=1 #если есть гласная прибавляем в переменную
    else: #если предыдущие условие не выполняется
        sogl+=1 #если есть согласная буква прибавляем в переменную
        print("гласных:", gl) #вывод текста и количество гласных букв 
        print("согласных:", sogl) #вывод текста и количество со гласных букв 