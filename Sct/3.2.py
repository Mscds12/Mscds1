import numpy as np
print("Practical 3(B) performed by rahul Rathod")
np.set_printoptions(precision=20)
x = np.zeros((3,))
weights = np.zeros((3,))
desired = np.zeros((3,))
actual = np.zeros((3,))

for i in range(3):
    x[i] = float(input(f"Initial input x[{i}]: "))

for i in range(3):
    weights[i] = float(input(f"Initial weight[{i}]: "))

for i in range(3):
    desired[i] = float(input(f"Desired output[{i}]: "))

for i in range(3):
    actual[i] = x[i] * weights[i]

print("\nInitial actual:", actual)
print("Desired:", desired)
a = float(input("\nEnter learning rate: "))

iteration = 0
while not np.allclose(desired, actual, atol=1e-6):
    print(f"\n--- Iteration {iteration + 1} ---")
    for i in range(3):
        weights[i] = weights[i] + a * (desired[i] - actual[i])
        actual[i] = x[i] * weights[i]

    print("Updated weights:", weights)
    print("Updated actual:", actual)
    iteration += 1
print("\nFinal output after training:")
print("Corrected weights:", weights)
print("Final actual:", actual)
print("Desired:", desired)

