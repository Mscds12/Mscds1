import math

def binary_sigmoid(net):
    return 1 / (1 + math.exp(-net))

def bipolar_sigmoid(net):
    return (2 / (1 + math.exp(-net))) - 1

n = int(input("Enter the number of inputs: "))

x = []
w = []

for i in range(n):
    x_val = float(input(f"Enter value of X{i+1}: "))
    w_val = float(input(f"Enter value of weight W{i+1}: "))
    x.append(x_val)
    w.append(w_val)

b = float(input("Enter value of bias: "))

net = sum([x[i] * w[i] for i in range(n)]) + b
print(f"\nNet input (Yin) = {net}")

binary_out = binary_sigmoid(net)
print(f"Binary Sigmoidal Output = {binary_out:.4f}")

bipolar_out = bipolar_sigmoid(net)
print(f"Bipolar Sigmoidal Output = {bipolar_out:.4f}")
