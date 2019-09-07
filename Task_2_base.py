# Data input


while True:
    def Fibonacci(n):
        if n == 0:
            return 0
        elif n in (1, 2):
            return 1
        else:
            return Fibonacci(n - 1) + Fibonacci(n - 2)
    n = int(input("Plesae input number of elements \n"))
    print(Fibonacci(n))
    question = input("Do you want input new number? Y or N \n").upper()
    while not (question == 'Y' or question == 'N'):
        question = input("Please input 'Y' or 'N'. \n").upper()
    if question == "N":
        break
    else:
        continue