
num_ip = int(input("Enter the number of inputs: "))
print("For", num_ip, "inputs, calculate the net input")

x1 = []
x2 = []
t = []

for i in range(num_ip):
    ele1 = int(input(f"x1[{i+1}]: "))
    ele2 = int(input(f"x2[{i+1}]: "))
    out = int(input(f"Target output y[{i+1}]: "))
    x1.append(ele1)
    x2.append(ele2)
    t.append(out)
w1 = int(input("Enter the weight value of input1: "))
w2 = int(input("Enter the weight value of input2: "))

n = [w1 * i for i in x1]
m = [w2 * i for i in x2]

Yin = []
for i in range(num_ip):
    Yin.append(n[i] + m[i])
print("\nNet input values (Yin):")
print("Yin =", Yin)

Y = []
for i in range(num_ip):
    if Yin[i] >= 1:
        Y.append(1)
    else:
        Y.append(0)
print("Calculated output Y =", Y)
print("Target output T     =", t)

if Y == t:
    print("\n✅ Weight values accepted. The outputs match the targets.")
else:
    print("\n❌ Weights are not suitable. The outputs do not match the targets.")
