
x = float(input("Enter value of X: "))
b = float(input("Enter value of bias: "))
w = float(input("Enter value of weight: "))

net = (w * x) + b
print("****** Output ********")
print(f"net = {net}")

if net < 0:
    out = 0
elif 0 <= net <= 1:
    out = net
else:
    out = 1

print(f"Output = {out}")
