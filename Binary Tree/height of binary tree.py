class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def  heightOfBT(root):
    if(root is None):
        return -1
    
    lside=heightOfBT(root.left)
    rside=heightOfBT(root.right)
    if(lside>rside):
        return lside+1
    else:
        return rside+1
        
def main():
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.left.left.left=Node(7)
    root.left.left.right=Node(8)
    root.left.left.right.left=Node(9)
    print(heightOfBT(root))
main()
