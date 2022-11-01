# eval()

javascript로 프로그래밍을 하다가 보면 변수를 동적으로 생성하거나 변수와 텍스트를 결합해서 다른 변수를 생성해야 할 경우가 있습니다. 그냥 서로 합친다고 새로이 변수가 생성되는 것이 아니고 eval()라는 함수를 이용해야 합니다.  
eval() 함수
eval()의 괄호 안에 들어 있는 모든 내용을 스크립트로 인식을 합니다.  
사용법
copy javascript  var key = "nara";
  eval("var haha" + key + "= 100");

 console.log(hahanara)
 => 100
위의 코드 처럼 문자열처럼 변수를 생성할 수 있습니다. 
hahanara 변수를 확인해 보면 결과 값은 100이 표시됩니다. 
객체의 key값을 변수 형태로 사용하기
또하나는 객체를 사용할때 애를 먹었던 건데..
객체의 key값을 기본적으로는 문자형태로 사용을 하는데 이 key값을 스크립트 형태로 사용해야 할 경우가 있습니다. 
원래는 아래와 같이 사용합니다. 
copy javascriptvar aa = {
  'bb': 'cc'
};
console.log(aa['bb'])
=> cc
그런데 'bb'를 변수의 형태로 적용하려면 어떻게 해야 할까요?
사용법
copy javascriptlet key = 'bb';

var aa = {
  [key]: 'cc'
};

console.log(aa['bb'])
=> cc
객체의 key에 []를 사용하면 됩니다.


출처: https://ux.stories.pe.kr/195 [UX 공작소:티스토리]