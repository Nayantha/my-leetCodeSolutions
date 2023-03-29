import random
import statistics

array = [random.randint(0, 100) for i in range(10)]

print(f"inputted array: {array}")
mean = statistics.mean(array)
print(f"mean for inputted list: {mean}")


array_mean = [int(abs(number - mean)) for number in array]


print(f"closest number to mean: {array[array_mean.index(min(array_mean))]}")
