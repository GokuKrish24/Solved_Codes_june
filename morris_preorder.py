class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
arr=[4,2,5,3,-1,7,6,-1,9,-1,-1,8,-1,1]
queue=[]
root=TreeNode(arr[0])
queue.append(root)
i=1
while(len(queue)!=0 and i<len(arr)):
    k=queue.pop(0)
    if(arr[i]!=-1):
        lf=TreeNode(arr[i])
        k.left=lf
        queue.append(lf)
    i+=1
    if(i>=len(arr)):
        break
    if(arr[i]!=-1):
        rf=TreeNode(arr[i])
        k.right=rf
        queue.append(rf)
    i+=1
def morris_inorder(root):
    curr=root
    while(curr!=None):
        if(curr.left==None):
            print(curr.data)
            curr=curr.right
        else:
            prev=curr.left
            while(prev.right!=None and prev.right!=curr):
                prev=prev.right
            if(prev.right==None):
                prev.right=curr
                print(curr.data)
                curr=curr.left

            else:
                prev.right=None
                curr=curr.right
morris_inorder(root)
