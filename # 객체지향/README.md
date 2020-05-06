# 객체지향

## 객체지향이란 ?

Objeckt Oriented Programming 객체라는 것을 중심으로 프로그래밍하는 기법 이라고 설명 할 수 있다.

그렇다면 그 객체 지향 프로그래밍 이란 무엇인가?

이것을 이해하기 위해선 먼저 모듈라는 개념을 알아야 한다 우리는 저번에 모듈이라는 개념을 배웠다 모듈이란 같은 쓰임세가 비슷한 함수끼리 있는 집합이다.

object 는 즉 객체는 class + instance 이다.

class 라는 것은 마치 카테고리와 같다 포유류 라는 카테고리에 사람, 고양이 등 존재한다 이때 포유류는 class 와 같고 사람, 고양이 등 은 instance 와 같다.

## class

여기서 중요한것은 바로 class 이다 class 또한 모듈처럼 무엇인가 담아주는 박스같은 역할이지만 모듈과는 다르게 함수(로직)뿐만 아니라 변수(데이터)까지도 담아 줄 수 있다

한마디로 class 는 연관된 데이터와 로직의 집합이라고 볼 수 있다.   

## instance

이 instance 는 여러개의 class를 받아서 여러개를 만들수도 있지만 1개의 class 로 여러개의 class 도 만들수 있다.

그렇가면 왜 1개의 class 로 여러개의 instance 를 구축하는냐 그것은 1개의 class 로 구축한 instance 들은 모두 같은 변수와 같은 함수로 이루어져 있지만 그 변수의 데이터값들이 다 다를수 있기 때문이다. 

## 객체의 제작

파이선에는 여러가지 함수와 변수가 있는데 연관있는 함/변수의 집합을 class 라고 한다 그리고 그 class 들을 복제해서 여러개의 instace를 만들어 낸다.

그렇기 때문에 그 instace 들은 같은 함수를 같지만 변수의 데이터가 다르다 그렇기 때문에 각 각 함수가 동작하는것이 다르다.

## 객체의 사용 

우리는 이제 Class 를 만들어 볼 것이다. 우리는 이 객체와 Class 를 통해 Calculater 를 만들어 볼 것이다 

하지만 우리는 calculater 계산기를 만들기 전 이 객체라는 것을 어떻게 사용해야 하는지를 배워 볼 것이다.

```
c1 = Cal(10, 10)
print(c1.add())
print(c1.subtract())

c2 = Cal(30,20)
print(c2.add())
print(c2.subtract())
```

위 코드는 하나의 Class로 두개의 instance 를 만들어내고 있다 두개의 instance 는 같은 class 를 사용하지만 다른 결과값을 가진다 이유를 살펴 보자.

## Class 만들기

```
class Cal (object):
	def __init__(self,v1, v2):
		print(v1, v2)

c1 = Cal(10, 10)
	
```

위 예문은 Cal 이라는 클래스를 생성하고 있다. 

class Cal (objact): 클래스를 만들것이다 Cal 이라는 (objact) 이건 뒤에 항상 넣어 주어야 한다 지금은 그렇게 알아 두자.

그리고 클래스 안쪽에서 함수를 정의 해주고 인스턴스 인자값을 받을수 있게 매개변수를 주고 있다 하지만 특별한 것이 있다

그것은 인스턴스의 입력값과 함수에서 받는 매개변수의 수가 일치 하지 않는다는 것이다.

지금은 그저 입력을 해주는 값들은 매개변수 2번째 부터 적용 된다고 생각하자.

## 생성자 (Constructor)

```
class Cal (object):
	def __init__(self,v1, v2):
		print(v1, v2)

c1 = Cal(10, 10)
	
```

위의 예문을 보자 c1 = Cal(10, 10) 이 부분을 보면 Cal 이라는 클래스를 사용하면서 '생성자' 에 10, 10 이라는 인자값을 주고있다.

그렇다면 이 생성자는 무엇일까??

생성자는 좀 더 쉽게 설명하면 instance 에서 class 를 실행 할 때 자동으로 실행 되도록 약속된 함수 라고 생각하면 된다.

클래스를 생성하면 자동으로 만들어지는 메소드 즉 함수라고 이해 할 수 있다, 하지만 이 생성자를 직접 함수로써 정의해 줄 수 있다 그것이 바로 __init__ 이라는 함수이다.

__init__ initialize 의 약자로 초기화 하다 라는 뜻이다 이 __init__ 으로 함수를 정의 해주면 생성자를 직접 만들 수 있다.

하지만 꼭 기억 해야 할것은 인자값 1 번째는 2번째 매개변수 부터 적용 된다는 것을 알아둬야 한다.   

## 인스턴스 변수와 메소드

```
class Cal (object):
	def __init__(self,v1, v2):
		print(v1, v2)

c1 = Cal(10, 10)
print(c1.add())
print(c1.subtract())

c2 = Cal(30,20)
print(c2.add())
print(c2.subtract())
	
```

이제 우리가 배울 부분은 instance 부분이다 Cal 이라는 class 를 c1,c2 로 각각 instance 시켜 주었다.

그러나 아직 그 인스턴스 밑 부분의 코드들이 무었을 뜻하는지 알 수 없다, 그것들에 대해서 배울것이다.

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

c2 = Cal(30,20)
print(c2.add())
print(c2.subtract())
```

우리는 이제 self 라는 매개 변수에 대해 알 수 있다 위의 def __init__ 은 마치 하나의 변수 저장소 같은 곳이다 .

self 라는 것은 한마디로 v1, v2 를 전역변수로 활용하기 위한 하나의 도구라고 생각하자 이것을 인스턴스 변수라고 한다.


## 키워드

객체 지향 프로그램 : 각각의 객체들을 이용하여 프로그래밍을 하는 것

class : 여러가지 함수와 변수가 있는데 연관있는 함/변수의 집합을 class 라고 한다

instance : class 의 복제로서 instance 의 각각 다른 변수들을 지정함으로 같은 class를 사용하지만 다른 결과와 동작을 하게 만드는것

생성자 : constructor 라고도 하며 class 를 instance 시킬때 자동으로 생성되는 메소드(함수)

인스턴스 변수 : 인스턴스 변수라는 것은 첫번째 매개변수를 통해 2,3.. 매개 변수들을 전역변수로 선언해 주는것 같은 의미를 가진다.

## 참고
[생활코딩](https://opentutorials.org/course/1750/9624)

 



