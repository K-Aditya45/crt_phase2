def findleftview(root):
    if root == None:
        return []
    result = []
    q = [root]

    while len(q) > 0:
        n = len(q)
        for i in range(n):
            curr = q.pop(0)
            if i == 0:
                result.append(curr.data)
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
    return result