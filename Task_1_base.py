# Input Data
while True:
    def Factorial(n):
        if n == 1:
            return n
        else:
            return n * Factorial(n - 1)
    n = int(input("Please input number of elements \n"))
    print(Factorial(n))
    question = input("Do you want input new number? Y or N \n").upper()
    while not (question == 'Y' or question == 'N'):
        question = input("Please input 'Y' or 'N'. \n").upper()
    if question == "N":
        break
    else:
        continue