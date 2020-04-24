# 파이선(모듈)

모듈(moudle) 이란 하나의 부품들의 집합이라고 생각하자, 우리가 만약 가구를 만든다고 하면 그 가구를 만드는 공구들이 필요 할 것이다 그 공구들의 집함을 모듈이라고 한다. 

```
import math 
print(math.ceil(2.1))
print(math.floor(2.1))
print(math.sqrt(2.1))

```

자 위의 예문을 보자 math 라는 모듈을 import 하고 있다, 이 math 모듈은 계산을 하기 위한 함수들로 이루어진 모듈이다.

이렇게 언어가 기본적으로 제공하는 모듈을 '내장모듈'이라고 일컫는다

그렇다면 만약 모듈이 없다면 어떤 일이 벌어질까?

```
def a ():
	return (a)
	# 수 많은 코드
	# A 가 만든
def a():
	return(b)
	# 수 많은 코드
	# B 가 만든

print(a())
```

A 라는 사람과 B 라는 사람이 같은 프로젝트를 하고 있는데 의사소통에 문제가 생겨 같은 이름의 함수를 정의했다고 생각하자

그러면 분명히 결과를 출력하는 곳에서 오류가 발생 할 것이다.

이것이 단순히 2개의 함수면 이름을 바꿔줌으로 오류를 해결 할 수 있지만 python 개발자들은 좀 더 효율적으로 이 문제를 개선할수 있도록 하였고 그것이 바로 모듈이다 


```
* module egoing
def a ():
	return (a)
	# 수 많은 코드
	# egoing 이 만든
def b()
	return (b)

```
```
* module megoing 
def a():
	return(b)
	# 수 많은 코드
	# megoing 이 만든
```
```
from eging inmport a
import megoing
print(a())
print(megoing.a())
```

위의 예문은 각각 다른 python 에서 정의를 하고 코드를 작성했고 호출하는 또 다른곳에서 그 python module 을 import 해서 출력하고 있다.   

하지만 또 봐야 할것이 있다 egoing 이라는 모듈에 여러가지 함수가 정리되어 있다 만약 모듈에서 하나의 함수만 import 하고 싶다면 from / import를 써주어야 한다. 

특별한것은 print(egoing.a()) 가 아닌 그냥 a 인데 이것은 모듈로부터 해당 된 하나의 파일을 가져왔기 떄문에 모듈의 이름을 적지 않는다.

또 하나 재미있는 기능이 있는데 바로 호출 하는곳 안에서만 쓸수있게 모듈 이름을 바꿀 수 있다  

```
from eging inmport a
import megoing as me
print(a())
print(me.a())
```

import megoing as me 이런 식으로 immport 다음 as 그리고 변경 할 이름을 적어주면 바꾸어 줄 수 있다.


## 활용 

그러면 우리가 계속 진행해 오고 있는 로그인에 모듈을 적용해 보자.
```
input_id = input("아이디 입력 : ")
members = ['egoing','megoing']

def auth (check)
	for member in members :
		if member == check:
			print(input_id,"승인")
			import sys
			sys.exit()
	print ("Try again")

print(auth(input_id))
```
이 전까지 우리가 해왔던 로그인 프로그램이다, 우리는 여기서 함수를 모듈화 시켜줄 것이다.

```
def auth (check)
	for member in members :
		if member == check:
			print(input_id,"승인")
			import sys
			sys.exit()
	print ("Try again")

```

이 부분만 따로 모듈 시켜주고 다른곳에서 호출을 하겠다. 
## 키워드

import : 수입하다란 뜻으로 모듈을 사용 할 수 있도록 하는 코드이다.  

내장모듈 : 언어가 기본적으로 제공하는 모듈을 뜻한다.

## 참고
[생활코딩](https://opentutorials.org/course/1750/9628)
