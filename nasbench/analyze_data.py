import os
import re

if __name__ == "__main__":
    path = "./output/seminas/"
    filename_token = "log0105_"
    search_token = 'Mean test'
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if re.match(token, filename):
                test_accs = list()
                with open (filename, 'r') as f:
                    line = f.readline()
                    if not line:
                        break
                    if re.match(search_token, line):
                        test_acc = float(line.rstrip().split(':')[-1])
                        test_accs.append(test_acc)
                if len(test_accs) == 20:
                    test_accs = test_accs[:10]
                    max_acc = max(test_accs)
                    with open("test_acc.txt", "a") as f:
                        f.write("{} ".format(max_acc))
                        for acc in test_accs:
                            f.write("{} ".format(acc))
                        f.write('\n')




