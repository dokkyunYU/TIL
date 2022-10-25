1. 전역에서는 그냥 window를 가리킨다.

2. 함수 내부에서는 호출할때 결정된다: 
  1) 함수로 호출하면 내부에서의 this는 window를 가리킨다.
  2) 메서드로 호출하면 내부에서의 this는 상위 객체를 가리킨다.

3. 이를 해결하기 위해 bind라는 문법을 사용할 수 있다. 다음과 같이 사용하여 내부함수의 this를 상위 객체를 가리키도록 변경한다.

```javascript
const obj1 = {
  outer : function () {
    const infunc = function () {
      console.log(this)
    }.bind(this)
  }
}
// this == obj1
```

4. 화살표 함수를 사용하면 이러한 바인딩을 자동으로 처리하여 상위의 this를 가리키도록 해준다. 이 경우 함수의 호출 기준이 아닌 선언을 기준으로 바인딩된다.

```javascript
const obj1 = {
  outer : function () {
    const infunc = () => {
      console.log(this)
    }
  }
}
// this == obj1
```

```javascript
const test = {
  a: 'hello'
}

const obj1 = {
  outer: function () {
    console.log(this)

    const inner = () => {
      console.log(this)
    }
    inner()
  }.bind(test)
}

// 둘다 test를 가리킨다
```

5. 콜백함수에서는 그때마다 다르다.

일반적으로 콜백함수도 함수 호출이므로 전역객체window를 가리킨다.

addEventListener에서 콜백 함수 안의 this는 이벤트가 발생하는 html요소를 가리킨다.

콜백함수를 제어하는 함수에서 this를 명시적으로 지정 가능한 것도 있다.(Array Helper Method)

```

```

(콜백함수를 사용하면 함수의 호출과 제어를 그 함수에게 맡기게 된다.)

```javascript
setTimeout(func, 5000) // 5초라는 시간 후에 func 함수를 실행한다.
```
(클래스 및 함수는 뒤에 소괄호가 없으면 인스턴스나 반환값이 아니라 그 자체를 불러온다.)