class papa:
    def __init__(self,name) -> None:
        self.name=name
    def get_papa_name(self):
        return self.name
class beta(papa):
  
    def __init__(self, name, papa=None, son=None) -> None:
        super().__init__(name)

        if son and papa:
            self.name = son.get_papa_name()
            self.papa = papa
        else:
            self.papa = papa
    

    #!Python does not support Constructor OverLoading
    #  def __init__(self,son,papa) -> None:
    #     self.name=son.get_papa_name()           
    #     self.papa=papa

    def get_name(self):
        return self.name
    def get_papa_name(self):
        return self.papa.get_papa_name()

p0=papa("Buddhisagar bhai")
p1=papa("Jayesh bhai")  
b2=beta(p1,p0)   
b1=beta("Het",p1)
b3=beta("Jiya",p1)


print(b1.get_papa_name())
print(b3.get_papa_name())
print(b2.get_papa_name())
