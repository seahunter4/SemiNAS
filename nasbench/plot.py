import matplotlib.pyplot as plt

with open("grads_data.txt", "r") as f:
    diff_str = f.readline().rstrip()
    grad_str = f.readline().rstrip()
    diffs = diff_str.split(' ')
    grads = grad_str.split(' ')
diffs = [float(i) for i in diffs]
grads = [float(i) for i in grads]

fig = plt.figure()
plt.xlabel('grads')
plt.ylabel('diffs')
plt.plot(grads,diffs)
plt.savefig("./grads_diffs.png")
plt.show()

