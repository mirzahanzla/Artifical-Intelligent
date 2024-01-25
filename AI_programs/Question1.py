class Tree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def generate_tree(depth, current_depth=1, index=[0]):
    if current_depth > depth:
        return None
    
    custom_values = [-3, 7, 2, -1, -7, -3, 8, 4]
    
    value = None if current_depth < depth else custom_values[index[0] % len(custom_values)]
    index[0] += 1
    return Tree(value, generate_tree(depth, current_depth + 1), generate_tree(depth, current_depth + 1))

def find_maximum(node, is_even_depth):
    if node is None:
        return None

    if node.left is None and node.right is None:
        return node.value

    left_max = find_maximum(node.left, not is_even_depth)
    right_max = find_maximum(node.right, not is_even_depth)

    if left_max is not None and right_max is not None:
        if is_even_depth:
            max_leaf_value = max(left_max, right_max)
        else:
            max_leaf_value = min(left_max, right_max)
        node.value = max_leaf_value
        return max_leaf_value

    return left_max or right_max

depth = 4
root = generate_tree(depth)

# Find the maximum leaf value and update the root
find_maximum(root, True)

#Display  root node 
print(f"\nRoot Node value is {root.value}.")
