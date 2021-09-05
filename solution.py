def preorderTraversal(root):
    values = []
    now = root 

    while now:
        if now.left:
            temp = now.left
            while temp.right and temp.right != now:
                temp = temp.now
            
            if temp.right == now:
                temp.right = None
                now = now.right
            else:
                values.append(now.val)
                temp.right = now
                now = now.left

        else:
            values.append(now.val)
            now = now.right
    
    return values
            
def inorderTraversal(root):
    values = []
    now = root 

    while now:
        if now.left:
            temp = now.left
            while temp.right and temp.right != now:
                temp = temp.now
            
            if temp.right == now:
                values.append(now.val)
                temp.right = None
                now = now.right
            else:
                temp.right = now
                now = now.left

        else:
            values.append(now.val)
            now = now.right
    
    return values
            
def postorderTraversal(root):
    values = []
    now = root 

    while now:
        if now.left:
            temp = now.left
            while temp.right and temp.right != now:
                temp = temp.now
            
            if temp.right == now:
                temp.right = None
                now = now.right
            else:
                values.append(now.val)
                temp.right = now
                now = now.left

        else:
            values.append(now.val)
            now = now.right
    
    values.reverse()
    return values
            