def computeAvg():
    size, summ = 5, 0
    arr = []

    for i in range(size):
        temp = int(input(f"Enter marks in subject {i+1}: "))
        arr.append(temp)
        summ += arr[i]
    
    avg = summ/size
    print("\nAverage marks = ", avg)

def celToFah():
    cel = float(input("\nEnter temperature in Celsius: "))
    fah = ((9/5)*cel) + 32
    print("\nTemperature in Fahrenheit = ", fah)

def perimeter():
    lnt = float(input("\nEnter length of the notice board: "))
    wid = float(input("Enter width of the notice board: "))
    peri = 2*(lnt+wid)
    print("\nPerimeter of the notice board = ", peri)

pick = int(input("Pick ->\n1) Compute Average\n2) Celsius to Fahrenheit\n3) Perimeter of Rectangular Notice Board\n>>> "))
match pick:
    case 1:
        computeAvg()
    case 2:
        celToFah()
    case 3:
        perimeter()
    case _:
        print("INVALID INPUT!")
