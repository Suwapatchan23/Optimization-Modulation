import numpy as np


# from b^e mod m
b = int(input("b = "))
e = int(input("e = "))
m = int(input("m = "))

# Create empty result array
result_memory_eff = []
result_memory_square = []

################  The First Method #################


def memory_efficient_method(b_mem, e_mem, m_mem):
    e_prime = 1
    c = 1
    # Create counter for count the number of each operation
    counter_mod = 0
    counter_multiplication = 0
    counter_sqrt = 0
    counter_subtraction = 0

    # Loop check id e_prime = e_mem + 1 then return
    while (e_prime != (e_mem + 1)):
        c = np.mod(((np.mod(c, m_mem))* np.mod(b_mem, m_mem)), m_mem)
        e_prime += 1
        counter_mod += 3
        counter_multiplication += 1

    return int(c), [counter_mod, counter_multiplication, counter_sqrt, counter_subtraction]


######################## The second Method ########################
def square_and_multiply_algorithm(b_sq_mul, e_sq_mul, m_sq_mul):
    # Convert from Decimal to binary.
    e_binary = bin(e_sq_mul)

    c = b_sq_mul
#    power_of_c = 1

    counter_multiplication = 0
    counter_mod = 0
    counter_sqrt = 0
    counter_subtraction = 0

    for i in range(3, len(e_binary)):
        # Square
        c = c ** 2
        counter_sqrt += 1

        #  Check condition If bit binary = 1
        if (e_binary[i] == "1"):
            #  Then multiply
            c *= b_sq_mul
            counter_multiplication += 1
        counter_mod += 1
#
    c = np.mod(c, m_sq_mul)
    
    return int(c), [counter_mod, counter_multiplication, counter_sqrt, counter_subtraction]


#################### New Method ####################### 
def new_method(b_sq_mul, e_sq_mul, m_sq_mul):
    # Create counter 
    counter_mod = 0
    counter_multiplication = 0
    counter_sqrt = 0
    counter_subtraction = 0
    
    # Create empty array to get the result
    result_arr = []

    # Change from e -> (e mod (m-1))
    new_e_sq_mul = np.mod(e_sq_mul, (m_sq_mul-1))
    counter_subtraction += 1
    counter_mod += 1

    result_arr = square_and_multiply_algorithm(b_sq_mul, new_e_sq_mul, m_sq_mul)

    # Update counter after return from square_and_multiply_algorithm method.
    counter_mod += result_arr[1][0]
    counter_multiplication += result_arr[1][1]
    counter_sqrt += result_arr[1][2]

    return result_arr[0], [counter_mod, counter_multiplication, counter_sqrt, counter_subtraction]


result_memory_eff = memory_efficient_method(b, e, m)
result_memory_square = square_and_multiply_algorithm(b, e, m)
result_new_method = new_method(b, e, m)

print(f"c [from memory_efficient_method] = {result_memory_eff[0]} The number of operations : {result_memory_eff[1][0] + result_memory_eff[1][1] + result_memory_eff[1][2] + result_memory_eff[1][3]} | Modulation : {result_memory_eff[1][0]} | Multiplications : {result_memory_eff[1][1]} | Square : {result_memory_eff[1][2]} | Subtraction : {result_memory_eff[1][3]}")
print(f"c [from square_and_multiply_algorithm] = {result_memory_square[0]} The number of operations : {result_memory_square[1][0] + result_memory_square[1][1] + result_memory_square[1][2] + result_memory_square[1][3]} | Modulation : {result_memory_square[1][0]} | Multiplications : {result_memory_square[1][1]} | Square : {result_memory_square[1][2]} | Subtraction : {result_memory_square[1][3]}")
print(f"c [from new_method] = {result_new_method[0]} The number of operations : {result_new_method[1][0] + result_new_method[1][1] + result_new_method[1][2] + result_new_method[1][3]} | Modulation : {result_new_method[1][0]} | Multiplications : {result_new_method[1][1]} | Square : {result_new_method[1][2]} | Subtraction : {result_new_method[1][3]}")
