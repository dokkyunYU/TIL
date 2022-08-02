# Today I learned

## 자주 있는 실수

1. git이 관리하는 git 저장소 내의 디렉토리에 또 git 저장소를 생성하면 submodule이 된다.

2. 파일의 공백문자는 전부 _로 치환해서 저장한다.

3. git 명령어는 항상 .git 폴더가 있는 곳에서 해야한다.

## 깃허브

1. README.md

    README.md는 처음 들어온 사람들에게 이 프로젝트에 대해 알려준다.

2. .gitignore

    .gitignore파일에 파일이름이나 폴더이름을 적어서 저장하면, 해당 파일의 버전 관리를 하지 않는다.
    이를 통해 다음을 올리지 않을 수 있다.
    - 남에게 보여주면 안되는 보안파일
    - 올리고 싶지 않은 파일이나 폴더

    * .gitignore가 생성되기 이전에 git으로 버전 관리가 되고 있던 파일들은(git add를 해놓은 파일들) .gitignore에 의해 무시당하지 않고 계속 버전관리가 이루어진다.
    * 그러므로 모든 프로젝트에서 가장 먼저 READ.md와 함께 만들어야 한다.

    + 이것을 도와주기 위해 [gitignore.io](https://www.toptal.com/developers/gitignore/) 에서 .gitignore 내용을 생성해준다.

3. Clone & Pull
    - clone
        Remote storage에서 local로 복제하는 것.
        "git clone 원격저장소_URL" 라는 명령어를 사용하면 다음의 일이 일어난다.
        * 폴더 생성
        * git init
        * git remote add
        * 버전, 파일 생성
    
    - pull
        Remote storage에 업로드된 버전으로 local을 업데이트 하는 것.
        "git pull 저장소_이름 브랜치_이름" 라는 명령어로 사용한다.

4. 

## Python 설치

- 3.9.13 버전을 설치하고 VSCode에 확장프로그램을 추가하면 VSCode에서도 간편하게 사용할 수 있다.

## API

- API는 서로 다른 두 어플리케이션 간에 통신하는 방법을 말한다.
- API를 통해 두 어플리케이션은 서로간에 원활하게 요청과 응답을 주고 받을 수 있다.