print("1-прямоугольник, 2-треугольник, 3-круг")
a = input("Выберите фигуру: ")

match a:
    
    case '1':
        print("Введите стороны прямоугольника:")
        b = int(input("a = "))
        c = int(input("b = "))
        a = b*c
        print (a)
        
    case '2':
        print("Введите высоту, основание треугольника:")
        h = int(input("h = "))
        b = int(input("b = "))
        a  = (h*b)/2
        print (a)
    
    case '3':
        print("Введите радиус круга:")
        r = int(input("r = "))
        a = ((3.14 * r ** 2))
        print (a)
    case _:
        print("Такой фигуры нет")