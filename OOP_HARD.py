import math



class COMPLEX:
    def __init__(self,real,image):
        self._real=real
        self._image=image
        self.module=math.sqrt(((self._real)**2)+((self._image)**2))
        
        
    @property
    def real(self):
        return self._real
    
    @property 
    def image(self):
        return self._image
    
    
    def module(self):
        return self.module


    @classmethod
    def new_complex(cls,real,image):
        return cls(real,image)
    


class PERSON:
     def __init__(self,name,m):
         self.m=m
         self.__name=name
         self.complex_list=[]
         self.mod_list=[]
     @property 
     def name(self):
         return self.__name
     
     def list_complex(self):
         for i in range(0,self.m):
             x=input("nhap vao so phuc thu {} : ".format(i+1))
             self.complex_list.append(x)
         return self.complex_list
     
     def div_process(self):
         for i in range(0,self.m):
             a=list(self.complex_list[i])
             c=0
             b=''
             real=''
             image=''
             for i in range(0,len(a)):
                 if a[i]=='j':
                     c+=1
             if c==0:
                 for i in range(0,len(a)):
                     real=real+str(a[i])
                     image=0
             if c==1:
               for i in range(0,len(a)):
                   if a[i]!='j':
                       b=b+str(a[i])
                       for k in range(0,len(b)):
                           if b[k]=='+' or b[k]=='-':
                               real=b[:k]
                               if real=='':
                                   real=0
                               image=b[k:]
                               if image=='+' or image=='-':
                                   image=b[k:]+'1'
             real=float(real)
             image=float(image)
             self.mod_list.append(COMPLEX.new_complex(real, image).module)
         return self.mod_list
                 
             
     def value_mod(self):
         max_val=max(self.mod_list)
         return max_val
         

while True:
    try:
        n=int(input("nhap vao so luong thanh vien : "))
        if n>=1:
            break
        else:
            print("nhap sai,hay nhap lai.... :")
    except:
        continue


mod_max=[]
list_member=[]

for i in range(0,n):
    name=str(input("nhap vao ten member thu {} : ".format(i+1)))
    m=int(input("nhap vao so luong so phuc cho member thu {} :".format(i+1)))
    person=PERSON(name,m)
    list_member.append(person.name)
    person.list_complex()
    person.div_process()
    mod_max.append(person.value_mod())

max_member=max(mod_max)
print("member {0} co module lon nhat voi gia tri {1} ".format(list_member[mod_max.index(max_member)],max_member))


    