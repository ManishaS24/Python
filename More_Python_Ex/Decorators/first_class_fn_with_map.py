def square(num):
    return num * num

def cube(num):
    return num * num *num

def my_map(func, arr_list):
    result = []

    for i in arr_list:
        result.append(func(i))
    return result

squares = my_map(square, [1,2,3,4,5])

print(squares)

cubes = my_map(cube, [1,2,3,4,5])

print(cubes)