# 중앙저장소

하나의 앱에 대한 상태관리를 위해 만들어짐

props & emit 으로는 컴포넌트의 중첩이 깊어질 경우 데이터 전달이 쉽지 않다.

공통의 상태를 유지해야하는 컴포넌트가 많아지면 데이터 전달 구조가 복잡해짐

중앙저장소에 데이터를 모아서 상태 관리

각 컴포넌트는 중앙저장소의 데이터를 사용

컴포넌트의 계층에 상관없이 중앙저장소에 접근해서 데이터를 얻거나 변경할 수 있음

중앙저장소의 데이터가 변경되면 각각의 컴포넌트는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영함

규모가 크거나 컴포넌트 중첩이 깊은 프로젝트 관리가 매우 편리


# Vuex

"state management pattern + Library" for vue.js

중앙저장소를 통해 상태관리를 할 수 있도록 하는 라이브러리

데이터가 예측 가능한 방식으로만 변경될 수 있도록 하는 규칙을 설정하며, Vue의 반응성을 효율적으로 사용하는 상태 관리 기능을 제공

Vue의 공식 도구로서 다양한 기능을 제공