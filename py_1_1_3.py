def segment(x1, y1, x2, y2 ):

    tg_a = abs(y1/x1)
    tg_b = abs(y2/x2)

    if tg_a > tg_b:
        print("Відрізок ОА утворює більший кут  з віссю ОХ")

    elif tg_a < tg_b:
        print("Відрізок ОB утворює більший кут  з віссю ОХ")

    elif tg_a == tg_b:
      print("Відрізки ОB і ОА утворють однаковий кут  з віссю ОХ")

coordinates = []
coordinates = input("Веддіть координати двох точок - х1, у1, х2, у2\n").split(",")

segment(int(coordinates[0]),int(coordinates[1]),int(coordinates[2]),int(coordinates[3]))