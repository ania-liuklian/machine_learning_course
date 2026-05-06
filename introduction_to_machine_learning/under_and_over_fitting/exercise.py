candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
# Write loop to find the ideal tree size from candidate_max_leaf_nodes
from collections import defaultdict
dct = defaultdict()
for max_leaf_nodes in candidate_max_leaf_nodes:
    mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    dct[max_leaf_nodes] = mae
# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
min_mae = min(v for k, v in dct.items())
best_tree_size = 0
for k, v in dct.items():
    if v == min_mae:
        best_tree_size = k


# Check your answer
step_1.check()
