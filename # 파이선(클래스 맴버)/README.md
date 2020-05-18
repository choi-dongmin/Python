# 파이선(클래스 맴버)


## 클래스 메소드(class method)

```
class Cs:
	@staticmethod
	def static_method():
		print('staic method')

	@classmethod	
	def clas_ method(cls):
		print('class method')

	def instance_method(self):
		print('instance method')

i = Cs()
Cs.static_method()
Cs.class_method()
i.instance_method()
```
파이선에는 2가지의 class member 가 존재한다 staitc method 와 class method 그리고 class method 에는 instance method 처럼 매개변수 처음에는 cls 가 있어야 한다.

cls 의 뜻은 method 자신이 속한 class 를 뜻하며 그것을 instatnce 의 self 처럼 받아준다고 이해하자.

또한 만약 class method 를 호출하고 싶다면 우리는 Cs.static_method() 와 같은 식으로 class 를 통해서 method 를 호출 시켜야한다.


## 클래스 변수 (class variale)
```
class Cs:
	count = 0
	def __init__ (self):
		Cs.count = Cs.count + 1

	@classmethod
	def getCount(cls):
		return cs.count

i1 = Cs()
i2 = Cs()
i3 = Cs()
print(Cs.getCount())
```

위 예문은 instance 를 한 만큼 결과값을 출력하는 시스템이다 작동하는 원리를 보자 i1,2,3 이 instance 가 되면 생성자를 통해 Cs.count = Cs.count + 1 를 실행한다.

그렇다면 Cs.count 는 무엇일까? 바로 class 안쪽에 method 밖에 존재하는 count = 0 이것이 바로 클래스 변수이다  

만약 클래스 변수를 메소드에서 쓰려고 한다면 Cs.count 와 같이 클래스를 통해서 쓸수 있다.

## 클래스 맴버의 활용

```
class Cal (object):
	_history = []

	def __init__(self,v1, v2):
		self.v1 = v1
		self.v2 = v2

	def add (self):
		result = self.v1 + self.v2
		Cal._history.append("add : %d+%d=%d" %(self.v1, self.v2, result))
		return result
	
	def subtract(self):
		result = self.v1 - self.v2
		Cal._history.append("add : %d-%d=%d" %(self.v1, self.v2, result))
		return result

	def setV1 (self, v):
		if isinstance (v, int) :
			self.v1 = v1

	def getV1 (self):
		return self.v1
	
	@classmethod
	def history(cls):
		for item in Cal._history:
			print(item)

class CalMultiply(Cal):
	def multiply(self):
		result  = self.v1 *self.v2
		Cal._history.append("add : %d*%d=%d" %(self.v1, self.v2, result))
		return result



c1 = CalMultiply(10, 10)
print(c1.multiply())
print(c1.add())
print(c1.subtract())
Cal.history()

```
위의 코드를 살펴보자 우선 CalMultiply Class 를 인스턴스화 시키고 CalMultiply Class 는 Cal Class 를 상속받고 있다.

자식 클래스에 인자값을 주어도 부모클래스에 지정한 생성자가 있음으로 그곳으로 인자값이 들어가며 들어간 값들은 함수에 따라 작동을 하게 된다.

그리고 history 라는 함수를 만들어 주었고 그 함수는 자신이 속한 Class 를 받고있다 이 history 함수는 어떻게 각 함수들이 작동하는지에 대한 결과값을 보여준다.

history 는 list Cal._history Cal class 의 _history 를 for/in 으로 반복하고 있다.

하지만 이 history 함수는 클래스 맴버이기 때문에 @classmethod 와 인자값을 cls 를 받아주 있다.

```
* Cal._history.append("add : %d*%d=%d" %(self.v1, self.v2, result)

위 코드는 Class Cal 의 _history 란 배열에 append 한다 즉 배열안에 추가한다는 뜻이다

그리고 %d %() 란 ()안에 매개변수의 값을 % 로 치환해준다. 

```

## 키워드 

클래스 맴버 : 클래스의 속한 맴버로 호출 할 때는 해당 class 를 통해서 호출 해야한다. ex ) for item in Cal._history:

상속 : 클래스가 다른 클래스의 기능을 받아와 수정 혹은 기능을 추가 하는것을 말한다.


## 참고 

[생활코딩](https://opentutorials.org/course/1750/10018)

