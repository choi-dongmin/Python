# 파이선 (조건문)

조건문 영어로는 Conditional Statements 이라고 한다, 말 그대로 조건이 있는 문장이라는 뜻이다.


```
if true:
	print("code 1")
	print("code 2")
```

가장 기본적인 조건문의 예시이다 만약 참 이라면 code 1,2 를 출력해 보아라 라는 의미를 가진 문법이다.

만약 true 의 자리에 false 가 들어간다면 실행이 되지 않을것 이다. 

```
if felse:
	print("code 1")
	print("code 2")
print ("code 3")
```

이렇다면 결과값이 어떨까? 들여쓰기로 칸이 띄어진 code 1, code 2 는 felse 이기 때문에 출력이 되지 않고

오직 code 3 만 조건문의 영향을 받지않기 떄문에 출력 될것이다.

조금 더 심화적인 예문을 보자

```
input = 22
real = 11

if real == input:
	print("Hello")

```

위의 예문을 보자 이번에는 true 와 felse 가 아닌 real 과 input 이 있다 이 둘은 변수이고 그 안에 담긴 값들을 비교하여 참/거짓을 구별 한다.

real == input : 만약 real 과 input 이 같다면 true 아니면 felse 이다 라는 뜻과 일맥상통한다.

이 경우에는 11 == 22 와 같음으로 거짓이 되고 Hello 는 출력이 되지 않는다.

이러한 방법으로 우린 맞았을 경우 Hello 틀렸을 경우 Try again 을 출력 할 수있다.

```
input = 22
real = 11

if real == input:
	print("Hello")

if real != input:
	print("Try again")
```

!= 은 양쪽 항이 같지 않을시에 실행하라는 명령어이다, 그럼으로 위 결과 값은 hello 가 아닌 try again 으로 출력 될 것이다.

하지만 위 코드는 중복된 코드를 반복 하고 있다 그건 불필요한 것임으로 더 발전시켜보자.

```
input = 22
real = 11

if real == input:
	print("Hello")
else:
	print("Try again")
```

이렇게 else 를 써준다면 자신이 쓴 조건문에 부합하지 않을때 else 밑에 오는 구문을 실행시키도록 약속 되어 있다 이렇게 해서 우리는 좀 더 효율적인 코드를 만들수 있다.

그리고 위의 예문 결과값은 else 밑의 구문인 Try again 이 출력된다.

그럼 조금 더 심화 시켜보자 우리가 자주 보는 로그인을 한후 환영 문구가 출력되는
 형태를 배워보자

```
input = 33 
real_me = 11
real_you = "ab"

if real_me == input:
	print("Hello me")
elif real_you == input:
	print ("Hello you")
else:
	print("Try again")

```

우리는 elif를 사용해 반복조건을 사용할수 있다. 위 예문을 보면 만약 real_me == input: 이면 hello me 를 출력한다 그러나 거짓임으로 무시하고 다음을 본다,

elif real_you == input: 이라면 Hello you 가 출력되지만 거짓임으로 그 다음을 실행한다

else: 위 비교연산자가 모두 거짓이었음으로 위 실행 결과는 Try again 을 출력한다.

## 키워드

조건문 : if 를 boolean 을 사용해 조건을 만족 시킬시 그 해당된 코드를 실행시키는것

반복조건문 : elif 로 처음 나온 조건문을 만족 시키시지 못할시 그 다음 elif를 통해 해당된 조건을 다시 확인 하고 만족될 시 출력시키는 것

else : 조건문을 확인하고 그 조건이 충족되지 않으면 else 의 구문을 바로 출력시킨다.(elif 와 다른것은 else 에는 조건이 없다는 것이다.)  


## 참고
[생활코딩](https://opentutorials.org/course/1750/9620)




