# 파이선 (주석)

주석은 영어로는 comment 라고 한다 프로그래밍을 한다면 누구나 활용하고 누구든지 활용해야 한다 굉장히 로직이 길어질 경우 주석을 달아야 한다.

## 주석

1. 한 줄 주석

```
print(1)

#print(2)
```

print(1) 이 2개가 있다 하나는 앞에 # 이 붙어 있다 위 로직을 출력해보면 1 이 하나만 출력 되는 것을 볼 수 있다.

어떠한 코드 앞에 # 을 붙인다면 그 코드는 주석처리 되어 코드를 실행시키지 않는다.

혹은 그 코드에 대한 설명을 주석으로 달아 놓기도 한다.

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

# 위 로직은 로그인을 하기위한 로직입니다.
``` 

이런 식으로 코드와 로직에 설명을 붙여 이해를 돕기도 한다.

2. 다중 주석

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

# 위 로직은 로그인을 하기위한 로직입니다.
# 2020.04.07 update

```

다중으로 주석을 사용하고 싶을땐 어떻게 할까 물론 # 을 두번 이용해서 할수 있다 그러나 ''' 을 사용해준다면 더 간편하게 할 수 있다.

''' 을 이용해 다중의 코드를 묶어준다면 다중 주석 처리가 가능하다

또 위 처럼 ''' 을 이용해 묶어준다면 문자열로 인식하기도 하는데 만약 이 문자열은 변수에 넣어준다면 ' , " 과는 다르게 여러칸의 문자열을 변수에 담을수 있다.

## 키워드

주석 : comment 로 프로그래밍을 하는데 반듯이 필요하다 #, ''' 로  프로그램이 코드를 인식하지 못하게 해 설명이나 참고를 기술한다.



## 참고
[생활코딩](https://opentutorials.org/course/1750/9626)





