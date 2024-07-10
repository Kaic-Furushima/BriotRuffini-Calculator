def calculateBR(f_x, function_dividers):
    roots = {}
    for i in range(len(function_dividers)):
        calculated_values = []
        calculated_values.append(f_x[0])
        print(f"{function_dividers[i]} | ", end="")
        print(f"{calculated_values[0]} | ", end="")
        for j in range(1, len(f_x)):
            calculated_values.append(calculated_values[j - 1] * function_dividers[i] + f_x[j])
            print(f"{calculated_values[j]} | ", end="")
        if(calculated_values[len(calculated_values) - 1] == 0):
            roots[f"{function_dividers[i]}"] = calculated_values
        print("")
    print(roots)


def buildPanel(f_x):
    print("***| ", end='')
    for i in range(len(f_x)):
        print(f"{f_x[i]} | ", end='')

def getDividers(function_values):
    function_dividers = []
    for i in range(len(function_values)):
        if(function_values[len(function_values) - 1] % (i + 1) == 0):
            function_dividers.append(i + 1)
            function_dividers.append(-(i + 1))
    return function_dividers

x = []
x_value = 'a'
f_x = []

x_degree = int(input("Insert x function's degree: "))

for i in range(x_degree + 1):
    f_x.append(int(input(f"Insert value {x_value}: ")))
    x_value = chr(ord(x_value) + 1)

buildPanel(f_x)
print()
calculateBR(f_x, getDividers(f_x))

