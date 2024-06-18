class Queue:
    def __init__(self):
        self.arr=[]
    def enqueue(self,element):
        self.arr.append(element)
    def dequeue(self):
        if(len(self.arr)==0):
            return -1
        return self.arr.pop(0)
    
q=Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())

##############      ###############     ##############      ############## 
#######                   ##            #######             ##          ##
####                      ##            ####                ##          ##
##                        ##            ##                  ##          ##
#                   ###############     #                   ##############
