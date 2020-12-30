import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

with open("grads_data.txt", "r") as f:
    diff_str = f.readline().rstrip()
    grad_str = f.readline().rstrip()
    label_str = f.readline().rstrip()
    diffs = diff_str.split(' ')
    grads = grad_str.split(' ')
    labels = label_str.split(' ')
diffs = [float(i) for i in diffs]
grads = [float(i) for i in grads]
labels = [float(i) for i in labels]

rel_diffs = [diffs[i]/labels[i] for i in range(len(diffs))]

fig = plt.figure()
plt.xlabel('grads')
plt.ylabel('relative_diffs')
plt.scatter(grads, rel_diffs)
plt.savefig("./rel_diffs.png")
# plt.show()

