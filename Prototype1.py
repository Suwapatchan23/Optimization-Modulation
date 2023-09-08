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

    # Loop check id e_prime = e_mem + 1 then return
    while (e_prime != (e_mem + 1)):
        c = np.mod((c * b_mem), m_mem)
        e_prime += 1
        counter_mod += 1
        counter_multiplication += 1

    counter = [counter_mod, counter_multiplication]
    return int(c), counter


######################## The second Method ########################
def square_and_multiply_algorithm(b_sq_mul, e_sq_mul, m_sq_mul):
    # Convert from Decimal to binary.
    e_binary = bin(e_sq_mul)

    c = b_sq_mul
#    power_of_c = 1

    counter_multiplication = 0
    counter_mod = 0
    counter_sqrt = 0

    for i in range(3, len(e_binary)):
        # Square
        c = c ** 2
        counter_sqrt += 1

        #  Check condition If bit binary = 1
        if (e_binary[i] == "1"):
            #  Then multiply
            c *= b_sq_mul
            counter_multiplication += 1
#
    c = np.mod(c, m_sq_mul)
    counter_mod += 1
    counter = [counter_mod, counter_multiplication, counter_sqrt]
    return int(c), counter


result_memory_eff = memory_efficient_method(b, e, m)
result_memory_square = square_and_multiply_algorithm(b, e, m)

print(
    f"c [from memory_efficient_method] = {result_memory_eff[0]} The number of operations : {result_memory_eff[1][0] + result_memory_eff[1][1]} | Modulation : {result_memory_eff[1][0]} | Multiplications : {result_memory_eff[1][1]}")
print(
    f"c [from square_and_multiply_algorithm] = {result_memory_square[0]} The number of operations : {result_memory_square[1][0] + result_memory_square[1][1] + result_memory_square[1][2]} | Modulation : {result_memory_square[1][0]} | Multiplications : {result_memory_square[1][1]} | Square : {result_memory_square[1][2]}")
