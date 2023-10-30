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
""" class Person :
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
print(p2.getCount()) """

# cls와 self의 차이

""" class MyClass:
    count = 0

    def __init__(self, num):
        self.count = num

    @classmethod
    def clsMethod(cls):
        cls.count += 1 
        print(f"cls count = {cls.count}")

    def instMethod(self):
        self.count += 1 
        print(f"instance = {self.count}")

MyClass.clsMethod()

obj = MyClass(10)

obj.instMethod()
print(obj.count)

print(MyClass.count)
print(MyClass.count) """

class Champion:
    lv = 1
    movspd = 0
    basicMovSpd = 325
    atkSpd = 0.658
    
    def __init__(self, chmpNam, speed):
        self.hp = 100
        self.chmpNam = chmpNam
        self.level = 1
        self.setSpeed(speed)
        self.setAtkSpd()
        self.setMovSpd()
        
    def setAtkSpd(self):
        self.atkSpd = 0.658*((1.0334)**(Champion.lv - 1) )
    def beAtk(self, dem):
        print("be attack", dem, 1-100.0/(100.0+100))
        self.dem = dem*(100.0/(100.0+100))
        print(self.dem)
        
    def setSpeed(self, sp):
        if (sp == 1):
            self.speed = 50
        else:
            self.speed = 0
            
    def setMovSpd(self):
        print("set Mov Spd")
        self.movspd = (20 + self.speed)*(1.00)*(100)
        
    def printStatus(self):
        print("chmpNam:%s, hp:%f, lv%d, mvSpd:%f, atkSpd:%f") 
        
ashe = Champion("ashe", 474.0)
mipo = Champion("mipo", 520.0)

ashe.printStatus()
mipo.printStatus()

mipo.beAtk(63.0)
mipo.printStatus()