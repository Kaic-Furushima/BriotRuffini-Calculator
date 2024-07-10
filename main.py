x = []
x_value = 'a'
f_x = []

x_degree = int(input("Insert x function's degree: "))

for i in range(x_degree):
    f_x.append(int(input(f"Insert value {x_value}: ")))
    x_value = chr(ord(x_value) + 1)

