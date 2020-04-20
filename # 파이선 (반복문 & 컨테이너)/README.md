# 파이선 (반복문 & 컨테이너)

반복문과 컨테이너를 사용하여 예문을 만들어 보자

```
i = 0
members = ['egoing','leezche','graphttie']

while i < len(members):
	print(member[i]) 
	i = i + 1



```

위의 예문을 보면 i 라는 변수를 0으로 선언하고 list member 에는 3개의 index가 있다, 그리고 반복문 while을 통해 반복할 것이다.

while i < len(members): 이 코드에 뜻은 i 가 members 의 원소의 수 만큼 반복한다 그러므로 i < 3

과 같은 뜻이다, 그리고 print(member[i]) 출력을 시키는데 member[i]를 출력 시킬 것이다 그러면 처음은

i = 0 이 됨으로 0번째 원소가 출력된다, 그리고 i + 1 을 통해 차례대로 원소가 출력되도록 하고있다 그리고

i < len(members): 로 인해서 0,1,2 번째 원소가 출력되면 반복문은 종료된 

## for / in

이번엔 while 보다 조금 더 효율적인 반복문 for 를 사용해 볼 것이다

```
i = 0
members = ['egoing','leezche','graphttie']

for member in members :
	print(members)
```

위의 예문을 보자 for 은 while 처럼 반복문을 시작하겠다는 문법이다 그리고 member 는 새로운 컨테이너라고 볼 수 있다

그리고 in 뒤에 오는 members 는 위에서 정의한 members 다.

위 예문을 해석하면 list members 를 반복문이 실행 될 때마다 member 라는 새로운 컨테이너에 넣어주고 

그 컨테이너를 출력한다. 

조금 더 활용을 한 예문을 확인 해보자

```

for item in range(1,5):
	print(item)

```

위 코드를 보자 위 코드에 list 는 없다 하지만 range 라는 문법을 통해 1 ~ 4 까지의 수를 프린트 해준다

지금 상황에선 그냥 range 라는 것이 있다 정도로만 알아 두면 된다.

하지만 항상 for 문이 효율적인것은 아니다 컨테이너를 이용 하는 경우엔 for 문이 훨씬 효율적이지만 그 외 
다른 경우에는 while이 더 효율적일수 있으니 

가장 적합한 방법으로 사용하는 것이 가장 이상적이다.


그럼 로그인 시스템과 반복문을 같이 사용해 보자
```
input_id = input("아이디 입력 : ")
members = ['egoing','megoing']

for member in members :
	if member == input_id:
		print(input_id,"승인")
		import sys
		sys.exit() 
print ("Try again")
```

우리는 보다 혁신적으로 로그인 시스템을 개선하였다. 조건문에서 만들었던 예문과 비교하여 얼마나 효율적으로 변화 하였는지 확인해 보자.
```
input_id = input("아이디 입력 : ")
real_egoing = "egoing"
real_megoing = "megoing"
if real_egoing == input:
	print('Hello', 'egoing')
elif real_megoing = input:
	print ('Hello', 'megoing')
else:
	print('Tra again')
``` 

우선 배열을 통해 하나 하나 사용자의 정보를 index 시키기 매우 편해졌고 반복문을 사용해 쉽게 코드를 더욱 가볍게 만들수 있었다.

## 키워드

컨테이너 : 어떠한 값을 담는 하나의 바구니 라고 생각을 하자 가장 대표적인 컨테이너로는 list 가 있다.

list : index로 문자열, 숫자, boolean이 올 수 있는 하나의 배열.

for / in : 반복문 중 하나로 list 와 같은 배열과 같이 사용하면 휠씬 효율적인 반복문 이다. (for X in Y : X 라는 새로운 변수에 Y list 값을 하나씩 담는다)

## 참고
[생활코딩](https://opentutorials.org/course/1750/9874)




 