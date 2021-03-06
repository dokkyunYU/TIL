## 제어문

- 파이썬은 기본적으로 위에서부터 아래로 차례대로 명령을 수행

- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함

- 제어문은 순서도로 표현이 가능

## 조건문

### 기본형식

- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용됨

- 조건에는 참/거짓에 대한 조건식과 함께 사용
    + 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블록을 실행
    + 이외의 경우 else 이후 들여쓰기 되어있는 코드 블록을 실행
        * else는 써도되고 안써도 됨

### 복수 조건문

- 복수의 조건식을 활용할 경우 elif를 활용하여 표현함

### 중첩 조건문

- 조건문은 다른 조건문에 중첩되어 사용될 수 있음
    + 들여쓰기에 유의하여 작성

### 조건 표현식

- 조건 표현식을 일반적으로 조건에 따라 값을 정할때 활용
- 삼항 연산자로 부르기도 함

true인 경우 값 if 조건 else false인 경우 값

ex) value = num if num >= 0 else -num (절대값을 저장하는 코드)

## 반복문

- 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을때 사용

- 반복문의 종류
    + while
    + for

### while 문

- 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야함

- 조건식이 참인 경우 반복적으로 코드를 실행
    + 조건이 참인 경우 들여쓰기 되어있는 코드 블록이 실행됨
    + 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
    + while문은 종료조건이 있어야 무한 루프를 하지 않는다

#### 복합 연산자

- 복합 연산자는 연산과 할당을 합쳐놓은것 +=

### for 문

- 반복가능한 객체를 모두 순회하면 종료 (별도의 종료 조건이 필요없음)

- 시퀀스를 포함한 순회가능한(iterable) 객체의 요소를 모두 순회함
    + iterable
        * 순회할 수 있는 자료형 : string, list, dict, tuple, range, set 등
        * 순회형 함수 : range, enumerate

- 처음부터 끝까지 순회하면 끝나므로 별도의 종료조건은 필요치 않음

- 딕셔너리의 경우 추가 메서드를 활용하여 순회할 수 있음
    + key() : key로 구성된 결과
    + values() : value로 구성된 결과
    + items() : (Key, value)의 튜플로 구성된 결과

- enumerate 순회
    + enumerate() : 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
        * (index, value) 형태의 tuple로 구성된 열거 객체를 반환

- List Comprehension
    + 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
        * [code for 변수 in iterable]
        * [code for 변수 in iterable if 조건식]

- Dictionary Comprehension
    + 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법
        * {key : value for 변수 in iterable}
        * {key : value for 변수 in iterable if 조건식}

### 반복제어

- break, continue, for-else, pass

- break : 반복문을 종료

- continue : continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

- for-else : 끝까지 반복문을 실행한 이후에 else 문 실행
    + break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음

- pass : 아무것도 하지 않음 (문법적으로 필요하지만, 할 일이 없을때 사용)