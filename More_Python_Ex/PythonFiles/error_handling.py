try:
    # f = open("testfile.txt")
    # f = open("test_file.txt")
    # var = bad_var

    f = open("corrupt_file.txt")

    if f.name == 'corrupt_file.txt':
        raise Exception


except FileNotFoundError as e:
    print(e)
    # print('Sorry. This file does not exist!')

except Exception as e:
    # print('Sorry. This file does not exist!')
    # print(e)
    print("Error!!")

else:
    print(f.read())
    f.close()

finally:
    print("Executing the finally block..")
