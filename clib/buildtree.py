import collections


arr = [1, 3, 5, None, 7, 9, 3, 3, 4, 0]

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return f'({self.val})'

def build(arr):
    arr.reverse()
    layers = []
    layer_count = 1
    while arr:
        layer = []
        for _ in range(layer_count):
            if arr:
                layer.append(Node(arr.pop()))
            else:
                break
        layer_count *= 2
        layers.append(layer)
    print(layers)

        
if __name__ == '__main__':
    build(arr)