class ListGame:
    def __init__(self,list1,list2):
        self.list1=list1
        self.list2=list2
    def common_member(self,a,b):
        self.a=a
        self.b=b
        l1=set(a)
        l2=set(b)
        if(l1 & l2):
            print("Common element in lists  : ",l1 & l2)
        else:
            print("No common elements")
    def reverseofother(self,a,b):
        self.a=a
        self.b=b
        a.reverse()
        if(b==a):
            print("Are they reverse of each other : YES")
        else:
            print("Are they reverse of each other : NO")
    def equal(self,a,b):
        self.a=a
        self.b=b
        l1=len(a)
        l2=len(b)
        if(l1==l2):
            print("Lists are of equal length and can be multiplied element wise" )
            s=[]
            s=[a[i] * b[i] for i in range(l1)]
            print("Multiplied list is : ",s)
        else:
            print("Lists are not of equal length")

list1=[3,7,2,8]
list2=[8,2,7,3]
print("LIST1 = ",list1)
print("LIST2 = ",list2)
res= ListGame(list1,list2)
res.common_member(list1,list2)
res.equal(list1,list2)
res.reverseofother(list1,list2)
