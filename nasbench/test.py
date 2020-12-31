from nasbench import api
import numpy as np

nasbench = api.NASBench('./data/nasbench_full.tfrecord')
all_keys = list(nasbench.hash_iterator())
valid_accs = []
for key in all_keys:
    fixed_stat, computed_stat = nasbench.get_metrics_from_hash(key)
    arch = api.ModelSpec(
        matrix=fixed_stat['module_adjacency'],
        ops=fixed_stat['module_operations'],
    )
    data = nasbench.query(arch)
    if data['validation_accuracy'] < 0.9:
        continue
    valid_accs.append(data['validation_accuracy'])
print("mean={}, std={}, std(n-1)={}".format(np.mean(valid_accs), np.std(valid_accs), np.std(valid_accs, ddof=1)))