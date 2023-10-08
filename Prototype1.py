import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.table import Table

################  Memory Efficient Method #################


def memory_efficient_method(b_mem, e_mem, m_mem):
    cnt_mem = 0
    start = time.time()
    e_prime = 1
    c = 1
    # Create counter for count the number of each operation
    counter_mod = 0
    counter_multiplication = 0
    counter_sqrt = 0
    counter_subtraction = 0

    # Loop check id e_prime = e_mem + 1 then return

    while (e_prime != (e_mem + 1)):
        print(f"e_prime = {e_prime}")
        c = np.mod(((np.mod(c, m_mem)) * np.mod(b_mem, m_mem)), m_mem)
        e_prime += 1
        counter_mod += 3
        counter_multiplication += 1
        cnt_mem += 1
    end = time.time()
    resTime = (end-start) * (10**3)  # time in ms
    counter_all = [counter_mod, counter_multiplication,
                   counter_sqrt, counter_subtraction]
    n_operation = sum(counter_all)

    return int(c), counter_all, n_operation, resTime


######################## Square And Multiply Algorithm ########################
def square_and_multiply_algorithm(b_sq_mul, e_sq_mul, m_sq_mul):

    # Convert from Decimal to binary.
    start = time.time()
    e_binary = bin(e_sq_mul)
    print(f"e_binary = {e_binary}")

    c = b_sq_mul
    #    power_of_c = 1

    counter_multiplication = 0
    counter_mod = 0
    counter_sqrt = 0
    counter_subtraction = 0

    for i in range(3, len(e_binary)):
        print(f"e_binary:  {i}")
        print(f"There are {len(e_binary) - i} left.")
        # Square
        print(f"before square c when c = {c}")
        c = c ** 2

        #  Check condition If bit binary = 1
        if (e_binary[i] == "1"):
            #  Then multiply
            print("before c = c xb_square_mul")
            c *= b_sq_mul
            counter_multiplication += 1
        counter_mod += 1
        print("before new i")
    #
    print("finish for loop")
    c = np.mod(c, m_sq_mul)
    end = time.time()

    resTime = (end-start) * (10**3)  # time in ms
    counter_all = [counter_mod, counter_multiplication,
                   counter_sqrt, counter_subtraction]
    n_operation = sum(counter_all)
    return int(c), counter_all, n_operation, resTime

#################### Exponent Modular ####################


def exponent_modular(b_ex, e_ex, m_ex):
    start = time.time()
    counter_mod = 0
    counter_multiplication = 0
    counter_sqrt = 0
    counter_subtraction = 0

    # Change from e -> (e mod (m-1))
    new_e_ex = np.mod(e_ex, (m_ex - 1))
    counter_subtraction += 1
    counter_mod += 1

    result_arr = memory_efficient_method(b_ex, new_e_ex, m_ex)

    end = time.time()
    resTime = (end - start) * (10**3)  # time in ms
    # Update counter after rern from square_and_multiply_algorithm method.
    counter_mod += result_arr[1][0]
    counter_multiplication += result_arr[1][1]
    counter_sqrt += result_arr[1][2]

    counter_all = [counter_mod, counter_multiplication,
                   counter_sqrt, counter_subtraction]
    n_operation = sum(counter_all)

    return result_arr[0], counter_all, n_operation, resTime

#################### Exponent Modular with Square and Multiply Algorithm #######################


def exponent_modular_with_square(b_sq_mul, e_sq_mul, m_sq_mul):
    # Create counter
    start = time.time()
    counter_mod = 0
    counter_multiplication = 0
    counter_sqrt = 0
    counter_subtraction = 0

    # Change from e -> (e mod (m-1))
    new_e_sq_mul = np.mod(e_sq_mul, (m_sq_mul - 1))
    counter_subtraction += 1
    counter_mod += 1

    result_arr = square_and_multiply_algorithm(
        b_sq_mul, new_e_sq_mul, m_sq_mul)

    end = time.time()
    # Update counter after return from square_and_multiply_algorithm method.
    counter_mod += result_arr[1][0]
    counter_multiplication += result_arr[1][1]
    counter_sqrt += result_arr[1][2]

    resTime = (end - start) * (10**3)  # time in ms
    counter_all = [counter_mod, counter_multiplication,
                   counter_sqrt, counter_subtraction]
    n_operation = sum(counter_all)

    return result_arr[0], counter_all, n_operation, resTime


# input
type1B = 89999857
type1E = [51555977989]
type1M = 152077
# 43157687, 47857727, 50958277, 520586211,
# 55058593, 59058653, 60058721, 6305881, 66058841, 67150091, 69150769, 70150757, 74450777, 78450817, 80450819, 83450819, 85501877, 89001917

type2B = 4007
type2E = [7001, 7573, 8039, 8731, 9013, 9511, 9967, 10177, 10597, 11119]
type2M = 1559


resMemoryEffMethod = []
resSquareAndMulMethod = []
resExponentModularMethod = []
resExponentModularWithSquareMethod = []

w_type = input("what type of input: ")

### TYPE1###
if w_type == "1":
    for i in range(len(type1E)):
        resMemoryEffMethod.append(
            memory_efficient_method(type1B, type1E[i], type1M)[3])
        resSquareAndMulMethod.append(
            square_and_multiply_algorithm(type1B, type1E[i], type1M)[3])
        resExponentModularMethod.append(
            exponent_modular(type1B, type1E[i], type1M)[3])
        resExponentModularWithSquareMethod.append(
            exponent_modular_with_square(type1B, type1E[i], type1M)[3])

    ########################## PLOTTING E GRAPH ###########################
    x_e = type1E

    ########################## PLOTTING LOG(E) GRAPH ###########################
    x_log = np.log(type1E)
    t = type1E

### TYPE2###
elif w_type == "2":
    for i in range(len(type2E)):
        resMemoryEffMethod.append(
            memory_efficient_method(type2B, type2E[i], type2M)[3])
        resSquareAndMulMethod.append(
            square_and_multiply_algorithm(type2B, type2E[i], type2M)[3])
        resExponentModularMethod.append(
            exponent_modular(type2B, type2E[i], type2M)[3])
        resExponentModularWithSquareMethod.append(
            exponent_modular_with_square(type2B, type2E[i], type2M)[3])

    ########################## PLOTTING E GRAPH ###########################
    x_e = type2E

    ########################## PLOTTING LOG(E) GRAPH ###########################
    x_log = np.log(type2E)
    t = type2E


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
########################## PLOTTING E GRAPH ###########################
ax1.set_title(
    "Analysis and Comparison of Modular Exponential methods", fontsize=10)
ax1.set_xlabel("e value", fontsize=10)
if w_type == "1":
    ax1.set_ylabel(
        f"Computation time in ms [ b = {type1B} | m = {type1M} ] ", fontsize=10)
else:
    ax1.set_ylabel(
        f"Computation time in ms [ b = {type2B} | m = {type2M} ] ", fontsize=10)
ax1.plot(x_e, resMemoryEffMethod, label="Memory Efficient Method", marker="o")
ax1.plot(x_e, resSquareAndMulMethod,
         label="Square And Multiply Algorithm", marker="o")
ax1.plot(x_e, resExponentModularMethod,
         label="Exponential And Modular Method", marker="o")
ax1.plot(x_e, resExponentModularWithSquareMethod,
         label="Exponential And Modular With Square Method", marker="o")
for i in range(len(t)):
    ax1.annotate(f"e = {x_e[i]}", (x_e[i], resMemoryEffMethod[i]), fontsize=7)
    ax1.annotate(f"e = {x_e[i]}",
                 (x_e[i], resSquareAndMulMethod[i]), fontsize=7)
    ax1.annotate(f"e = {x_e[i]}",
                 (x_e[i], resExponentModularMethod[i]), fontsize=7)
    ax1.annotate(f"e = {x_e[i]}", (x_e[i],
                 resExponentModularWithSquareMethod[i]), fontsize=7)
ax1.grid()

########################## PLOTTING LOG(E) GRAPH ###########################
ax2.set_xscale("log")
ax2.set_title(
    "Analysis and Comparison of Modular Exponential methods", fontsize=10)
ax2.set_xlabel("e value (log)", fontsize=10)
ax2.plot(x_log, resMemoryEffMethod,
         label="Memory Efficient Method", marker="o")
ax2.plot(x_log, resSquareAndMulMethod,
         label="Square and Multiply Algorithm", marker="o")
ax2.plot(x_log, resExponentModularMethod,
         label="Exponential And Modular Method", marker="o")
ax2.plot(x_log, resExponentModularWithSquareMethod,
         label="Exponential And Modular With Square Method", marker="o")
for i, txt in enumerate(t):
    ax2.annotate(f"log(e) = {round(x_log[i], 2)}",
                 (x_log[i], resMemoryEffMethod[i]), fontsize=7)
    ax2.annotate(f"log(e) = {round(x_log[i], 2)}",
                 (x_log[i], resSquareAndMulMethod[i]), fontsize=7)
    ax2.annotate(f"log(e) = {round(x_log[i], 2)}",
                 (x_log[i], resExponentModularMethod[i]), fontsize=7)
    ax2.annotate(f"log(e) = {round(x_log[i], 2)}", (x_log[i],
                 resExponentModularWithSquareMethod[i]), fontsize=7)
ax2.grid()


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
########################## PLOTTING E GRAPH ###########################
ax1.set_title(
    "Analysis and Comparison of Modular Exponential methods", fontsize=10)
ax1.set_xlabel("e value", fontsize=10)
if w_type == "1":
    ax1.set_ylabel(
        f"Computation time in ms [ b = {type1B} | m = {type1M} ] ", fontsize=10)
else:
    ax1.set_ylabel(
        f"Computation time in ms [ b = {type2B} | m = {type2M} ] ", fontsize=10)
ax1.plot(x_e, resSquareAndMulMethod,
         label="Square And Multiply Algorithm", marker="o", color="orange")
ax1.plot(x_e, resExponentModularWithSquareMethod,
         label="Exponential And Modular With Square Method", marker="o", color="red")
for i in range(len(t)):
    ax1.annotate(f"e = {x_e[i]}",
                 (x_e[i], resSquareAndMulMethod[i]), fontsize=7)
    ax1.annotate(f"e = {x_e[i]}", (x_e[i],
                 resExponentModularWithSquareMethod[i]), fontsize=7)
ax1.grid()

########################## PLOTTING LOG(E) GRAPH ###########################
ax2.set_xscale("log")
ax2.set_title(
    "Analysis and Comparison of Modular Exponential methods", fontsize=10)
ax2.set_xlabel("e value (log)", fontsize=10)
ax2.plot(x_log, resSquareAndMulMethod,
         label="Square and Multiply Algorithm", marker="o", color="orange")
ax2.plot(x_log, resExponentModularWithSquareMethod,
         label="Exponential And Modular With Square Method", marker="o", color="red")
for i, txt in enumerate(t):
    ax2.annotate(f"log(e) = {round(x_log[i], 2)}",
                 (x_log[i], resSquareAndMulMethod[i]), fontsize=7)
    ax2.annotate(f"log(e) = {round(x_log[i], 2)}", (x_log[i],
                 resExponentModularWithSquareMethod[i]), fontsize=7)
ax2.grid()

# print(resMemoryEffMethod)
# print(resSquareAndMulMethod)
# print(resExponentModularMethod)
# print(resExponentModularWithSquareMethod)

plt.legend(fontsize=6)
# plt.show()

############# TODO: Plot the data graph ####################
columns = ('Memory Efficient Method', 'Square and Multiply Algorithm', 'Exponential And Modular Method',
           'Exponential And Modular With Square Method')
rows = [f'e = {type1E[i]}' if w_type ==
        "1" else f"e = {type2E[i]}" for i in (range(len(type1E)))]

# Data for the table
data = [
    ['', columns[0], columns[1], columns[2], columns[3]],
    [rows[0], f"{resMemoryEffMethod[0]:.4f}", f"{resSquareAndMulMethod[0]:.4f}",
        f"{resExponentModularMethod[0]:.4f}", f"{resExponentModularWithSquareMethod[0]:.4f}"],
    [rows[1], f"{resMemoryEffMethod[1]:.4f}", f"{resSquareAndMulMethod[1]:.4f}",
        f"{resExponentModularMethod[1]:.4f}", f"{resExponentModularWithSquareMethod[1]:.4f}"],
    [rows[2], f"{resMemoryEffMethod[2]:.4f}", f"{resSquareAndMulMethod[2]:.4f}",
        f"{resExponentModularMethod[2]:.4f}", f"{resExponentModularWithSquareMethod[2]:.4f}"],
    [rows[3], f"{resMemoryEffMethod[3]:.4f}", f"{resSquareAndMulMethod[3]:.4f}",
        f"{resExponentModularMethod[3]:.4f}", f"{resExponentModularWithSquareMethod[3]:.4f}"],
    [rows[4], f"{resMemoryEffMethod[4]:.4f}", f"{resSquareAndMulMethod[4]:.4f}",
        f"{resExponentModularMethod[4]:.4f}", f"{resExponentModularWithSquareMethod[4]:.4f}"],
    [rows[5], f"{resMemoryEffMethod[5]:.4f}", f"{resSquareAndMulMethod[5]:.4f}",
        f"{resExponentModularMethod[5]:.4f}", f"{resExponentModularWithSquareMethod[5]:.4f}"],
    [rows[6], f"{resMemoryEffMethod[6]:.4f}", f"{resSquareAndMulMethod[6]:.4f}",
        f"{resExponentModularMethod[6]:.4f}", f"{resExponentModularWithSquareMethod[6]:.4f}"],
    [rows[7], f"{resMemoryEffMethod[7]:.4f}", f"{resSquareAndMulMethod[7]:.4f}",
        f"{resExponentModularMethod[7]:.4f}", f"{resExponentModularWithSquareMethod[7]:.4f}"],
    [rows[8], f"{resMemoryEffMethod[8]:.4f}", f"{resSquareAndMulMethod[8]:.4f}",
        f"{resExponentModularMethod[8]:.4f}", f"{resExponentModularWithSquareMethod[8]:.4f}"],
    [rows[9], f"{resMemoryEffMethod[9]:.4f}", f"{resSquareAndMulMethod[9]:.4f}",
        f"{resExponentModularMethod[9]:.4f}", f"{resExponentModularWithSquareMethod[9]:.4f}"],

]


# Create a figure and axis
fig, ax = plt.subplots()

# Create a table
table = ax.table(cellText=data, loc='center', cellLoc='center')

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1, 1.5)  # Adjust the table size
ax.set_title(f"Computataion time in ms | Input type = {w_type}.")

# Remove axis labels and ticks
ax.axis('off')

# Display the table
plt.show()
