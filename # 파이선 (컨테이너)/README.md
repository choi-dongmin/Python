# 파이선 (컨테이너)

컨테이너란 무엇인가를 담을 수 있는 박스라고 생각하자, 우리는 이러한 형태를 변수에서 볼 수 있었다 

name = 'Egoing' 이러한 형태의 변수가 있다고 생각하자 그러면 name 이라는 곳에 Egoing 이라는 문자열이 들어 가게 된다.

그럼 생각해 보자 하나의 상자 안에 하나가 아닌 복수의 것을 담지 못 할까? 바로 그럴때 컨테이너를 사용 할 수 있다.

## List

파이선에서 컨테이너는 List 가 있다 만약 우리가 'me' 'you' 'we' 이 세가지를 한 List 에 담고 싶다면 어떻해야 할까?

['me', 'you', 'we'] 이렇게 대괄호로 묶어준다면 그것은 하나하나 객체의 타입이 '문자열' 이 었지만 [] 로 묶이는 순간 [] 는 데이터 타입이 List 로 변화된다.

'' 는 문자열을 뜻하는 기호처럼 [] 는 List 를 뜻하는 기호라고 생각하자.

자 그럼 이제 우리는 이 List를 변수와 같이 담아보도록 하자.

```
us = ['me', 'you', 'we'] 

print(us[0])

```

위와 같이 List를 us 라는 곳에 담았다 그리고 print 로 출력하고 있다, 그러나 특별한 점이 있다 [0] 이라는 것이 us 뒤에 위치하고 있다는 것이다.

이  각각의 원소의 위치 번호를 Index 라고 한다(처음부터 0,1,2...) .

조금 더 심화 시켜보자.

```
us = ['me', 'you', 'we'] 
print(us[0])
me = ['Programmer', 'seoul', 25, false]
me[1] = 'suwon'
print(me)

``` 

위의 로직을 보자 me 라는 새로운 List 가 생겼고 그곳에 원소들은 'Programmer', 'seoul', 25, false 가 있다.

(단순히 문자열 뿐아니라 숫자, Blooean 까지 List 로 담을수 있다.)

그리고 만약 List 에서 수정하고 싶은것이 있다면 me[1] = 'suwon' 이와 같이 수정 할 수 


## 키워드

List : 파이선의 컨테이너로 []를 통해 배열처럼 원소를 담아주며 문자열 뿐 아니라 숫자, Blooean 등을 담을수 있다.

원소 : List를 구성하고 있는 것들을 뜻하며 처음 부터 각각 0,1,2 ... 순서대로 번호를 같는다.


## 참고
[생활코딩](https://opentutorials.org/course/1750/9622)

