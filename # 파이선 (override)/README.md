# 파이선 (override)

override 는 마치 재정의와 같다 상속받는 클래스에서 부모 클래스가 가진 함수를 자식 클래스에서 재정의 하는것이 바로 'override' 이다.

```
class C1:
	def m(self):
		retrun "parent" 

class C2(C1):
	pass

o = C2()
print(o.m())	
```

위 코드를 보자 위 코드는 C2 라는 자식 클래스에서 C1의 M 이라는 함수를 출력하려 하고 있다. (만약 자식클래스에 아무런 함수가 없을시 pass 를 적어야 오류가 없다.) 

하지만 만약 우리가 child 라는 값을 출력하고 싶다면 부모클래스에서 바꿀수 있지만 그렇게 한다면 부모클래스를 받는 여러 자식 클래스에도 영향을 받을수 있다

그렇기 때문에 자식 클래스에서 그 클래스에 맞게 재정의 해주는것이 바람직 하다.

```
class C1:
	def m(self):
		return "parent" 

class C2(C1):
	def m(self):
		return "child" 

o = C2()
print(o.m())	
```

위와 같은 방식으로 override 가 가능하다.

하지만 만약 우리가 완전한 재정의가 아닌 부모클래스의 기능에 다른 기능을 추가하고 싶으면 어떻게 할 수 있을까?

```
class C1:
	def m(self):
		return "parent" 

class C2(C1):
	def m(self):
		return super().m() + ' child'
		
o = C2()
print(o.m())	
```

위 코드는 부모클래스의 함수를 불러오고 그리고 그곳에 추가하고 싶은 값을 넣어주고 있다. 

return super().m() + 'child' 이 코드를 보자 super().m  자신의 부모 클래스 (super) 의 함수 (.m)를 출력함과 동시 chlid 를 추가해 주고 있다.

## 활용

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
	def info(self):
		return "Cal v1 : %d, v2 : %d" % (self.v1, self.v2)

class CalMultiply(Cal):
	def multiply(self):
		result  = self.v1 *self.v2
		Cal._history.append("add : %d*%d=%d" %(self.v1, self.v2, result))
		return result

	def info(self):
		return "CalMultiply => %s" % super().info()

c0 = Cal(30, 60)
print (c0.info())
c1 = CalMultiply(10, 10)
print (c1.info())


```

위 코드를 보면 override 를 통해서 Cal 클래스를 상속받는 CalMultiply 에서 info 를 override 하고 있다.

```
def info(self):
		return "Cal v1 : %d, v2 : %d" % (self.v1, self.v2)


def info(self):
		return "CalMultiply => %s" % super().info()

* %s 는 %d 와 같이 뒤에오는 super().info() 를 % 에 치환해준다는 뜻이다.
``` 

1번째 코드는 Cal Class 의 코드 2번째는 CalMultiply Class의 코드이다.

## 키워드

상속 : 상속이란 클래스가 어떤 클래스에 기능을 그대로 사용하거나 수정 및 추가 하는것을 뜻한다.

override : 자식 클래스에서 부모 클래스의 기능을 재정의 하는것을 뜻한다.

## 참고 
[생활코딩](https://opentutorials.org/course/1750/10116)
