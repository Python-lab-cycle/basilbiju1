class publisher:
    def ___init___(self,pname):
        self.pname=pname
    def display(self):
        print("name",self.pname)
class book(publisher):
    def ___init___(self,pname,bname,title):
        self.pname=pname
        self.bname=bname
        self.title=title
    def display(self):
        print("pname",self.pname)
        print("bname",self.bname)
        print("title",self.title)
class python(book):
    def __init__(self,pname,bname,title,page,price):
        self.pname=pname
        self.bname=bname
        self.title=title
        self.page=page
        self.price=price
    def display(self):
        print("pname",self.pname)
        print("book",self.bname)
        print("title",self.title)
        print("page",self.page)
        print("price",self.price)

n=input("enter publisher")
b=input("enter book")
p=int(input("enter page"))
t=input("enter title")
pr=int(input("enter price"))
obj=python(n,b,p,t,pr)
obj.display()
