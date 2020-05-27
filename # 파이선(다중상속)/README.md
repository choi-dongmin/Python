# 파이선(다중상속)

일반적으로 우리가 '상속' 이라고 부르는 것은 하나의 하위 클래스가 하나의 상위 클래스를 받는것을 뜻한다.

A,B,C 클래스가 있고 A -> B 상속 B -> C 이러한 방식으로 하나의 상위클래스 하나의 하위클래스를 일반적으로 상속이라고 일컫는다.

그렇다면 다중상속이란 무엇일까? 바로 하나의 하위클래스가 여러개의 상위클래스를 상속 받는것, 즉 하나의 하위클래스, 하나의 상위클래스가 아니라는 것이다.

```
class C1():
	def c1_m(self):
		print('c1') 

class C2():
	def c2_m(self):
		print('c2')

class C3(C1, C2):
	pass

c = C3()
c.c1_m()


```

위 예문을 보자 C1,2,3 클래스가 있고 C3에서 C1,2 를 상속을 받고 있다 그리고 C3 를 instance 시키고 C1 의 메소드 c1_m 을 호출하고 예외는 발생하지 않는다.

하지만 우리는 이런 경우를 생각해 볼 수 있다 만약 상속받는 상위 클래스의 메소드의 이름이 동일 하다면 어떻게 해야할까?
```
class C1():
	def c1_m(self):
		print('c1') 

	def m(self):
		print('c1_m')

class C2():
	def c2_m(self):
		print('c2')

	def m(self):
		print('c2_m')
class C3(C1, C2):
	pass

c = C3()
c.c1_m()
c.c2_m()
c.m()
```

이런 경우이 m 이라는 메소드는 C3 가 상속받는 2개의 클래스에 모두 m 이라는 메소드가 존재하지만 결과값을 실행하면 오류가 아닌 C1 의 m 이 출력된다.

그 이유는 class C3(C1, C2): 이 곳의 매개변수의 우선순위 때문이다 만약 C2 가 먼저 있다면 C2의 m 이 출력 될 것이다.

만약 C3에 m 이라는 메소드가 있다면 어떻게 될까? 그럼 C3의 m 이 가장 높은 우선순위를 가진다 또한 우리는 그것을 override 라고 일컫는다.


## 활용

```
class Cal (object):
	def __init__(self,v1, v2):
		self.v1 = v1
		self.v2 = v2

	def add (self):
		return self.v1 + self.v2
	def subtract(self):
		return self.v1 - self.v2
	def setV1 (self, v):
		if isinstance (v, int) :
			self.v1 = v1
	def getV1 (self):
		return self.v1

class CalMultiply():
	def multiply(self):
		return self.v1 * self.v2

class CalDivide (Cal, CalMultiply):
	def divide (self):
		return self.v1 / self.v2

c1 = CalDivide (10, 10)
print(c1.multiply())
print(c1.add())
print(c1.subtract())
print(c1.divide())
```

위 예제를 보면 class CalDivide 가 Cal, CalMultiply 2 클래스를 상속받고 있으며 그 상위클래스의 기능과 자신의 기능을 instance 하면서 출력하고 있다.

## 키워드

상속 : 상속이란 상위클래스가 가진 기능들 하위클래스에서 상속을 받아 그 기능을 사용 혹은 수정 하는것을 뜻한다.

다중상속 : 원래 상속이라함은 하위 클래스는 하나의 상위 클래스를 상속 받지만 다중상속은 여러개의 상위 클래스를 상속 받는다. 

override : 오버라이드, 오버라이딩 이란 상속받는 클래스에서 부모클래스와 같은 이름의 메소드를 재정의 해주는것을 일컫는다.

## 참고
[생활코딩](https://opentutorials.org/course/1750/10436)