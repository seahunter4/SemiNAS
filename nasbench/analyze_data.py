import os
import re
import numpy as np


if __name__ == "__main__":
    path = "./outputs/seminas/"
    filename_token = "log0105_"
    search_token = 'Mean test'
    max_accs = list()
    first_accs = list()
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if re.match(filename_token, filename):
                print("Processing file {}".format(filename))
                test_accs = list()
                with open (os.path.join(root, filename), 'r') as f:
                    while True:
                        line = f.readline()
                        if not line:
                            break
                        if re.match(search_token, line):
                            test_acc = float(line.rstrip().split(':')[-1])
                            if not test_accs:
                                first_acc = test_acc
                            test_accs.append(test_acc)
                if len(test_accs) == 20:
                    test_accs = test_accs[:10]
                max_acc = max(test_accs)
                max_accs.append(max_acc)
                first_accs.append(first_acc)
                with open("ori_test_acc.txt", "w") as f:
                    f.write("{} {}\n".format(max_acc, first_acc))
                    # for acc in test_accs:
                    #     f.write("{} ".format(acc))
                    # f.write('\n')
                print("Successfully record best test acc:{}, first acc:{}".format(max_acc, first_acc))
    print("Mean best test acc:{}".format(np.mean(max_accs)))
    print("Mean best val test acc:{}".format(np.mean(first_accs)))




