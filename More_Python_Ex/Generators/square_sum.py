# # using list
# def square_numbers(nums):
#     res = []
#     for i in nums:
#         res.append(i*i)
#     return res
# my_nums = square_numbers([1,2,3,4,5])

# # using list comprehension
# my_nums = [x*x for x in [1,2,3,4,5]]

# print(my_nums)

# # using generators - yeild()

# def square_numbers(nums):
#     for i in nums:
#         yield(i*i)

# my_nums = square_numbers([1,2,3,4,5])

# print(my_nums)

# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

# print(next(my_nums))

# We can use comprehensions 
my_nums = (x*x for x in [1,2,3,4,5])

# print(list(my_nums))

for num in my_nums:
    print(num)
