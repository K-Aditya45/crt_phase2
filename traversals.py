class p2:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(o1): #o1=root
    if o1==None:
        return
    inorder(o1.left)
    print(o1.data,end="")
    inorder(o1.right)

o1=p2(10)
o2=p2(20)
o3=p2(30)
o4=p2(40)
o5=p2(50)
o6=p2(60)
o7=p2(70)


o1.left=o2
o1.right=o3
o2.left=o4
o2.right=o5
o3.left=o6
o3.right=o7
inorder(o1)

#levelorder traversal
 def lot(root):
   if root==None:
      return
   result=[]
   q=[root]
   while len(q)>0:
      n=len(q)
      sr=[]
      for i in range(n):
         currnode=q.pop(0)
         sr.append(currnode.data)








         