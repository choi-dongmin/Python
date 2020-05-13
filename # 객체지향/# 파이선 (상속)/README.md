# 파이선 (상속)

- 상속은 무엇인가??

기존의 객체에 기능을 그대로 받아오면서 새로운 객체에서 필요에 맞게 기능을 추가 하는것을 '상속'이라고 일컫는다.

```
class class1 (object):
	def method1 (self):
		return 'm1'

class class2 (class1):
	def method2 (self):
		return 'm2'

c2 = class2()
print(c2.method1())
print(c2.method2())
``` 

위 예문을 보면 상속을 쉽게 이해 할 수 있다 위 코드에는 두개의 class 가 존재한다 (class1, class2) 

그리고 각각의 클래스에는 method 가 또 한개씩 존재한다 (method1, method2)

호출하는 코드를 보면 class2 를 instance 시키고 있고 method1,2 를 print 하고 있다, 우리는 여기서 이상한것을 알수 있다.

바로 class2 는 method1 을 정의하고 있지 않기 때문이다 그렇다면 이 코드는 오류를 발생 시킬까? 답은 X 이다.

그렇다면 왜 오류가 발생하지 않을까 바로 class2 가 class1 를 상속 받고있기 때문이다 우리는 어떻게 상속 받는지 알 수 있을까?

바로  class class2 (class1): 이 부분이다 python은 class name 뒤에 오는 () 안에 부모클래스의 이름을 넣어줌으로 상속을 받을수 있다.

*java 같은 경우에는 class2 extends class1 이런식으로 처리한다.

그러면 이제 calculater 예제를 통해 상속이라는 것을 활용 해보자

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

class CalMultiply(Cal):
	def multiply(self):
		return self.v1 * self.v2


c1 = CalMultiply(10, 10)
print(c1.multiply())
print(c1.add())
print(c1.subtract())

```

활용한 예제를 보면 class Cal 을 class Calmultiply 에서 상속을 받고 multiply 라는 함수를 추가해 주었다.

instance 하는 곳을 본다면 Cal class 가 아니라 CalMultiply 즉 상속받는 자식 클래스를 instance 를 해주고 있다..

그럼에도 부모클래스가 가진 메소드를 불러오는것이 전혀 오류를 발생시키지 않는다.

우리는 그럼 왜 상속을 사용해야 하는가? 우리는 프로그래밍을 단순히 혼자만 진행하지 않는다

만약 A,B 라는 사람이 있고 A 사람이 만든 코드를 B 사람이 사용하려 할 때 수정 및 코드추가를 하려하면 오류를 발생 시킬수 있다.

그러면 상속을 받는 곳에서 코드를 추가한다면 오류가 발생하더라도 부모클래스는 변화가 없기 때문에 수정하는것이 매우 안전해지며 효율적으로 활용 할 수 있게된다.


## 키워드    

상속 : 기존의 객체에 기능을 그대로 받아오면서 새로운 객체에서 필요에 맞게 기능을 추가 하는것

## 참고
[생활코딩](https://opentutorials.org/course/1750/9968)