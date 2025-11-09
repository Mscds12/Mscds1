import numpy as np
import math

print("Practical Performed by rahul  rathod")

np.set_printoptions(precision=4)

v2 = np.array([-0.1, 0.4])
v1 = np.array([0.6, -0.3])
b = np.array([0.3, 0.5])

w = np.array([-0.2, 0.4, 0.1])

x = np.array([0, 1])
alpha = 0.25
t = 1

zin = []
print("\nCalculate net input to z layer")
for i in range(2):
    zin_i = b[i] + x[0] * v1[i] + x[1] * v2[i]
    zin.append(round(zin_i, 4))
    print(f"z{i+1} = {zin[i]}")

z = []
print("\nApply activation function to calculate output of hidden layer")
for i in range(2):
    z_i = 1 / (1 + math.exp(-zin[i]))
    z.append(round(z_i, 4))
    print(f"z{i+1} = {z[i]}")

yin = w[0] + z[0] * w[1] + z[1] * w[2]
print("\nCalculate net input to output layer")
print("yin =", round(yin, 4))

y = round(1 / (1 + math.exp(-yin)), 4)
print("Output y =", y)

fyin = y * (1 - y)
dk = round((t - y) * fyin, 4) 
print("\ndk =", dk)

dw1 = round(alpha * dk * z[0], 4)
dw2 = round(alpha * dk * z[1], 4)
dw0 = round(alpha * dk, 4)

print("\nWeight changes at output layer:")
print("dw1 =", dw1)
print("dw2 =", dw2)
print("dw0 =", dw0)

din = [dk * w[1], dk * w[2]]
print("\ndin1 =", round(din[0], 4))
print("din2 =", round(din[1], 4))

fzin = []
d = []
for i in range(2):
    fzin_i = z[i] * (1 - z[i])
    fzin.append(round(fzin_i, 4))
    d_i = din[i] * fzin_i
    d.append(round(d_i, 4))

print("\nError terms at hidden layer:")
print("d1 =", d[0])
print("d2 =", d[1])

dv = [[0, 0], [0, 0], [0, 0]]  

for i in range(2):
    dv[0][i] = round(alpha * d[i] * x[0], 4)
    dv[1][i] = round(alpha * d[i] * x[1], 4)
    dv[2][i] = round(alpha * d[i], 4)

print("\nWeight changes between input and hidden layer:")
print("Δv1 =", dv[0])
print("Δv2 =", dv[1])
print("Δb  =", dv[2])

for i in range(2):
    v1[i] += dv[0][i]
    v2[i] += dv[1][i]
    b[i] += dv[2][i]

w[1] += dw1
w[2] += dw2
w[0] += dw0

print("\nFinal weights after one iteration:")
print("v1 =", v1)
print("v2 =", v2)
print("b  =", b)
print("w  =", w)

