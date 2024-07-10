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

function_dividers = getDividers(f_x)
print(function_dividers)

