# 파이선 (객체와 변수)

객체라는 것은 하나의 부품이라고 볼 수 있고 우리는 부품을 만든다고 생각 할 수 있다 그렇다면 객체의 특성은 무엇일까?

- 캡슐화

캡슐화라는 것은 함수, 변수 등 연관되어 있는 것들을 묶어서 한곳에 모아두는 것을 뜻한다. 이렇게 캡슐화를 시키면 외부의 영향으로 부터의 오류를 예방할수 있다.

그럼 왜 외부의 영향을 받지 않는것이 중요한가? 객체안에는 많은 양의 데이터가 존재하고 그 데이터는 변수안에 캡슐화 되어있다 그 데이터가 외부로 부터 영향을 받게되면

오류나 예외가 발생 할 수 있다 그래서 외부로 부터 영향을 받지 않는것이 중요하다. 

## 인스턴스 변수의 특성

```
class C:
	def __init__(self, v):
		self.value = v

c1 = C(10)	
print(c1.value)
c1.value = 20
print(c1.value)

```

예문을 보면 생성자의 value 라는 변수에 매개변수 v를 넣어주고 있고 그것을 출력하고 있다.

재미있는 것은 파이선은 인스턴스를 하고 난 후에도 다시한번 메소드가 아닌 인스턴스 된 곳에서 변수의 값을 조정 해줄수 있다는 것이다.

그리하여 결과값은 10, 20 이 차례로 출력 될 것이다.

## set / get 메소드

```
class C:
	def __init__(self, v):
		self.value = v

	def getValue (self):
		return self.value

	def setValue (self, v):
		self.value= v

c1 = C(10)	
print(c1.getvalue())
c1.setValue(20)
print(getValue())
```

우리는 set / get 메소드를 통해서 인스턴스값을 직접 변경하는 것이 아닌 메소드에서 변경하도록 할 수 있다.

이전 예제에서 우리는 메소드 밖에서 인스턴스값을 바꾸어 줬는데 위와 같은 방식으로 메소드 안에서 인스턴스 값을 변경 할 수있다.

그렇다면 우리는 왜 set / get 메소드를 사용해야 할까?

```
class Cal (object):
	def __init__(self,v1, v2):
		self.v1 = v1
		self.v2 = v2

	def add (self):
		return self.v1 + self.v2
	def subtract(self):
		return self.v1 - self.v2


c1 = Cal(10, 10)
print(c1.add())
print(c1.subtract())
c1.v1 = '십'
c1.v2 = 10
print(c1.add())
print(c1.subtract())

```

만약 위와 같은 오류 (문자와 숫자를 더 할 수 없디)를 방지하기 위해 , 이러한 실수는 개발자 혹은 사용자 둘 다 발생 할 수 있다.

이럴때 우리는 set / get 메소드를 통해 문제를 해결해 줄 수 있다.

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

c1 = Cal(10, 10)
print(c1.add())
print(c1.subtract())
c1.v1('십')
c1.v2 = 10
print(c1.add())
print(c1.subtract())
```

위 예문에는 isinstance 라는것을 활용한다 조건문과 isistance(매개변수, int : 매개변수가 int 라면 ture 아니면 false) 를 활용하여 매개변수 v 가 int 이 재정의 한다.
 

## 키워드

캡술화 : 객체의 특성으로 함수, 변수 등 연관되어 있는 것들을 묶어서 한곳에 모아두는 것을 뜻한다.

isistance : 매개변수가 정수인지 확인하는 함수 

get / set 메소드 : instance 변수를 외부가 아닌 메소드에서 설정하기 위한 메소드

## 참고 
[생활코딩](https://opentutorials.org/course/1750/10000)