class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Person:{self.name},Age:{self.age}"
class Student(Person):
    def __init__(self,name,age,scores):
       super().__init__(name,age)
       self.scores=scores
    def compute_average(self):
        if len(self.scores)==0:
         return 0
        return sum(self.scores)/len(self.scores)
    def display(self):
       print("Name : ",self.name)
       print("Age : ",self.age)
       print("Scores: ",self.scores)
       print("Average: ",f"{self.compute_average():.2f}")
    def __str__(self):
       return f"Student {self.name},Avg {self.compute_average():.2f}"
if __name__=="__main__":
       s1=Student("janani",17,[90,99,88])
       s1.display()
       print(s1)