# 파이선 (논리 연산자)

비교 연산자란 쉽게 말해 양쪽 항을 비교해 주어진 값이 참 인지 거짓인지 비교하는 것이다. 

그에 반해 논리 연산자는 비교하여 참 / 거짓을 비교하는것은 맡지만 그것을 and , or 을 통해서 비교를 한다.

1. and 

and 는 양쪽 항의 값이 모두 참 일때만 참 이라는 결과가 나오고, 단 하나라도 거짓 일때는 거짓으로 결과가 나온다.

```
in_id = input("아이디 입력 : ")
in_pw = input("비밀번호 입력 : ")

user_id = "doreme"
user_pw = "123"

if user_id == in_id and user_pw == in_id:
    print("승인")
else:
	print("불가")

```
위 예문을 보면 아이디와 비밀번호를 입력 받고 if user_id == in_id and user_pw == in_id:

이 라인의 논리연산자를 통해 두가지가 모두 참 혹은 거짓을 확인하고 두가지 가 참 이라면 승인

아니라면 불가를 출력한다.

```
True	and		True	= 	True
True	and		False	=	False
False	and		True	= 	False
False	and		False	= 	False

```



2. or

or 은 양쪽 항의 값중 하나라도 참이면 참을 나타내는 논리 연산자 이다 

```
in_id = input("당신의 성함을 입력하세요. : ")
in_nick = input("당신의 별명을 입력하세요 : ")

user_id = "egoing"
user_nick = "igoing"

if user_id == in_id and user_pw == in_id:
    print("승인")
else:
	print("불가")

```
위 예문은 성함, 별명을 입력받고 둘 중 하나라도 그러니까 성함, 별명 중 하나라도 참이라면 승인을 아니라면 불가를 출력한다. 

```

True	or	True	=	True
True	or	False	=	True
False	or	True	=	True
False	or	False	=	False
```

3. not

not 은 참 / 거짓 앞에 붙어서 그것들을 반전 시킨다, not ture = false, not false = ture


## 키워드

비교 연산자 : 비교 연산자는 양쪽 항을 비교해 참 / 거짓으로 결과 값을 나타내주는 연산자 (==, !=)

논리 연산자 : 양쪽 항 을 비교해 and, or, not 을 통해 참 / 거짓을를 나타내주는 연산자 

and : 논리 연산자중 하나로 양쪽 항을 비교해 양 항이 모두 참일시 참을 한쪽이 거짓일시 거짓을 나타낸다.

or : 논리 연산자중 하나로 양쪽 항을 비교해 두개의 항중 하나라도 참이라면 참을 나타낸다.


## 참고
[생활코딩](https://opentutorials.org/course/1750/9619)       

