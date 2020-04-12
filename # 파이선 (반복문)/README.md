# 파이선 (반복문)

우리는 이전 if 를 통해 조건문을 배웠다, 조건문이란 조건이 충족할때 포함된 코드를 실행 시키는 것을 의미한다.

그렇다면 반복문은 무엇일까? 말 그대로 반복을 시키는 문법이다 오늘 우리는 반복문을 배워 볼것이다.

```
print("Hello World 0")
print("Hello World 9")
print("Hello World 18")
print("Hello World 27")
print("Hello World 36")
print("Hello World 45")
print("Hello World 54")
print("Hello World 68")
print("Hello World 72")
print("Hello World 81")
``` 

위 코드를 보면 계속해서 9의 배수가 반복되고 있는것을 볼 수 있다 하지만 이렇게 하나하나 입력 하는것이 얼마나 귀찮고 힘든 일인지 조금만 해보아도 알 수 있다

그럴때 우리는 반복문을 사용한다.

while 

대표적인 반복문의 형태중 하나인 while 이다.

```
while false:
	print("Hello World")
print ("After World")
``` 

위와 같은 로직이 있다고 보자 결과값은 After World 일것이다 하지만 while false: 를 while true: 로 바꾸어 준다고 하면 어떻게 될까?

결과는 Hello World 가 시스템을 정지 시킬때 까지 무한히 반복되어 출력 될 것이다.

그럼 우리는 어떻게 원하는 만큼 출력하고 끝낼수 있을까? 우리는 그 몇번 반복했는지 확인해서 그것을 제어 할 수 있다.  

```
i = 0
while i < 3:
	print("Hello World")
	i = i + 1
```
 
위의 로직을 보자 우선 1 = 0 이라고 선언을 해주었다 그 다음 반복을 시작하는데 while i < 3: 이것은 while(반복) 한다 i 가 3 보다 작을때 라고 한것이다.

그럼 	print("Hello World")을 1번 출력하고  i = i + 1 을 실행 시킨다 그 다음 다시 반복 하기 위해 while을 실행시키고 i(1) < 3 이기 때문에 또 코드를 반복한다,

이렇게 i 가 3 보다 작을때 까지 실행을 시킨후 i(3) < 3 이 된다면 실행을 그만둔다.

자 그럼 우리는 이것을 활용해 9의 배수를 출력해보자.

```
i = 0
while i < 9:
	print("Hello World " + (i * 9))
	i = i + 1

``` 

이런 식으로 입력해 준다면 아까 처음에 보았던 9 배수를 출력하는 값과 똑같은 값이 출력이 된다.

```
i = 0
while i < 10:
	print(i)
	i = i + 1
```
위 예제의 결과값은 0 - 9 까지의 숫자이다, 그러나 만약 우리가 결과 값중 4 라는 결과를 제외하고 싶다면 ??

우리는 반복문 안쪽에 조건문을 넣음으로 그 결과를 실행 할 수 있다.

```
i = 0
while i < 10:
	if i != 4:
		print(i)
	i = i + 1
```
위의 코드를 보면 while 안쪽에 if 가 들어감으로 반복과 조건을 같이 사용하고 있다, i < 10 까지 반복한다

그러나 조건은 i 가 4 와 같지 않을 경우(!) 에 i를 출력한다, 만약 i 와 4 가 같다면 if 를 빠져나와 i + 1 을 실행하고

다시 while 로 돌아와 i < 10 까지 반복을 실행한다.

```
i = 0
while i < 10:
	if i == 4:
        break
    print(i)
	i = i + 1
print("After while")
```

그럼 위와 같은 경우에는 어떨까? 이번에는 print(i) 가 if 속하지 않았다 그리고 if 안에는 break 라는 것이 있다 

이 결과는 0,1,2,3 까지 출력하고 그 다음 조건문이 충족하기 때문에 바로 (i == 4) while 시스템을 break 하게 된다.

이 break는 자신이 포함된 시스템을 완전히 정시 시키고 그 다음 코드를 실행시킨다.

## 키워드

while : boolean 을 통해 포함 된 코드를 반복 실행하도록 하는 문법이다

if : boolean 과 조건을 통해 실행을 시키는 문법

break : 자신을 포함하고 있는 로직을 정지 시키는 코드.

## 참고
[생활코딩](https://opentutorials.org/course/1750/9621) 
