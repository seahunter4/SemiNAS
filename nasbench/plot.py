import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

with open("grads_data.txt", "r") as f:
    grad_str = f.readline().rstrip()
    label_str = f.readline().rstrip()
    pred_str = f.readline().rstrip()
grads = grad_str.split(' ')
labels = label_str.split(' ')
preds = pred_str.split(' ')
grads = [float(i) for i in grads]
labels = [float(i) for i in labels]
preds = [float(i) for i in preds]
rel_diffs = [abs((labels[i] - preds[i])/preds[i]) for i in range(len(preds))]

fig = plt.figure()
plt.xlabel('grads')
plt.ylabel('relative_diffs')
plt.ylim(-100,100)
plt.scatter(grads, rel_diffs)
plt.savefig("./rel_diffs.png")
# plt.show()

