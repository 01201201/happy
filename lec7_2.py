""" class Person :
    name = "python"
    age = 23
    number = "010123456789" 
    
p = Person()
print(p.name)
print(p.age)
print(p.number)

p1 = Person()
print(p1.name)
print(p1.age)
print(p1.number) """

#메서드, 셀프

""" class Person :
    name = "python"
    age = 23
    number = "010123456789"
    
    def getIntrodue(self):
        return f"My name is {self.name}"
    
p = Person()
print(p.name)
print(p.age)
print(p.number) """
    
#class 초기화 
    
""" class Person :
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number

  
p = Person("python", 23, "010123456789")
p1 = Person("Hello", 24, "0111111111")
p2 = Person("youngwon", 20, "01033545462")
print(p.name)
print(p1.name)
print(p2.name)

print(p.age)
print(p1.age)
print(p2.age)

print(p.number)
print(p1.number)
print(p2.number) """

# 클래스 변수

""" class Person :
	count = 0

	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.nmuber = number
		Person.count += 1

p = Person("hello", 25, "545131846")
print(p.name)
print(p.count)
p1 = Person("dh", 152, "01064651548")
print(p1.name)
print(p1.count)
p2 = Person("dff", 45, "654064645066")
print(p2.name)
print(p2.count) """

# 클래스 메서드 
class Person :
	count = 0

	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.nmuber = number
		Person.count += 1

	@classmethod
	def getCount(cls) : 
		return cls.count

p = Person("hello", 25, "545131846")
print(p.name)
print(p.getCount())
p1 = Person("dh", 152, "01064651548")
print(p1.name)
print(p1.getCount())
p2 = Person("dff", 45, "654064645066")
print(p2.name)
print(p2.getCount())



 
 