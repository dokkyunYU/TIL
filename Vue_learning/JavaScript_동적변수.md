[JavaScript] 동적변수 사용하기

코드를 작성하다보면 동일한 반복문 안에서 같은 규칙의 이름을 가지고 있는 배열들을 호출할 때 또는 반복문을 통한 결과값을 배열에 저장할 때 변수명을 동적으로 생성하면 코드의 길이도 줄어들어 효율적이게 됩니다. 자바스크립트에서 제공하고 있는 eval() 함수를 사용해서 동적 변수를 사용하는 방법도 있지만 제가 주로 사용하는 방법은 객체를 하나 생성하고 객체의 키값으로 변수명을 할당하는 방법입니다.

간단한 예제를 예시로 들겠습니다.

let object = {};
for (let i = 0; i < 10; i++){ 
  object[`variable${i}`] = 'test';
}
Output:

{ 
  variable0: 'test',
  variable1: 'test',
  ...
  variable9: 'test',
}
복잡한 로직 내에서 한 함수의 여러 개의 결과값을 다른 함수의 인자로 전달해야 하는 경우 매우 유용하게 사용할 수 있습니다. 다만 변수명을 작성할 때 동일한 규칙을 갖고 있어야 한다는 것을 유의하세요!

객체 안에는 변수 말고도 함수도 넣을 수 있습니다. 이를 활용한 방법으로 computed-property-name이 있는데요. 객체 안에 함수명을 동적으로 할당할 수 있습니다 !

const phaseA = 'getRide';
const phaseB = 'getStart';
const phaseC = 'getBreak';
const phaseD = 'getStop';

const obj = {
  [phaseA]: () => {	
    return '자동차에 탑니다.'; 
  }
  [phaseB]() {
    return '시동을 겁니다.';
  }
  [phaseC]: () => {
    return '브레이크를 밟습니다.';
  }
  [phaseD]: () => {
   return '자동차를 멈춥니다.';
  }
}


const RIDE = 'Ride';
console.log(obj[`get${RIDE}`); // 자동차에 탑니다.
const START = 'Start';
console.log(obj[`get${START}`);	// 시동을 겁니다.

console.log(obj['getBreak']()); // 브레이크를 밟습니다.
console.log(obj['getStop']()); // 자동차를 멈춥니다.



https://velog.io/@ragnarok_code/JavaScript-%EB%8F%99%EC%A0%81%EB%B3%80%EC%88%98-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0