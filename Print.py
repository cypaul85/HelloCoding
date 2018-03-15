try:
    number_input_a = int(input("Input integer> "))
    print("원의 반지름: ", number_input_a)
    print("원의 둘레: ", 2*3.14*number_input_a)
    print("원의 넓이: ", 3.14 * number_input_a * number_input_a)
except Exception as exception:
    print("type(exception): ", type(exception))
    print("exception: ", exception)
    print("Pls input integer number")
else:
    print("No error happened")
finally:
    print("The program was terminated anyhow")

list_number = [52, 273, 32, 72, 100]
try:
    number_input_a = int(input("Input integer> "))
    print("{}th element is {}".format(number_input_a, list_number[number_input_a]))
except ValueError:
    print("Pls input integer number")
except IndexError:
    print("Out of range of index")
