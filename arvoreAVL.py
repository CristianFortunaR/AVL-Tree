class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
        
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        
        if not root:
            return root
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
        
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

    def search(self, root, key, path=""):
        if not root:
            return f"Caminho: {path.strip()} | Elemento {key} não encontrado"
        path += str(root.key) + " "
        if root.key == key:
            return f"Caminho: {path.strip()} | Elemento {key} encontrado"
        elif key < root.key:
            return self.search(root.left, key, path)
        else:
            return self.search(root.right, key, path)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def get_height(self, root):
        return root.height if root else 0

    def get_balance(self, root):
        return self.get_height(root.left) - self.get_height(root.right) if root else 0

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def pre_order(self, root):
        return [] if not root else [root.key] + self.pre_order(root.left) + self.pre_order(root.right)

    def post_order(self, root):
        return [] if not root else self.post_order(root.left) + self.post_order(root.right) + [root.key]

    def in_order(self, root):
        return [] if not root else self.in_order(root.left) + [root.key] + self.in_order(root.right)


def main():
    avl = AVLTree()
    root = None
    
    while True:
        try:
            command = input().strip().split()
            if not command:
                continue
            
            if command[0] == "i":
                root = avl.insert(root, int(command[1]))
                print("Árvore após inserção:", avl.in_order(root))
            elif command[0] == "r":
                root = avl.delete(root, int(command[1]))
                print("Árvore após remoção:", avl.in_order(root))
            elif command[0] == "b":
                print(avl.search(root, int(command[1])))
            elif command[0] == "pre":
                print("Pré-Ordem:", avl.pre_order(root))
            elif command[0] == "pos":
                print("Pós-Ordem:", avl.post_order(root))
            elif command[0] == "em":
                print("Em-Ordem:", avl.in_order(root))
            elif command[0] == "exit":
                break
        except EOFError:
            break

if __name__ == "__main__":
    main()
