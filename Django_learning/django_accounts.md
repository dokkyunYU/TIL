# 사용자 인증 및 권한

## custom user model

개발자들이 작성하는 일부 프로젝트에서는 django에서 제공하는 bult-in user model의 기본 인증 요구사항이 적절하지 않을 수 있음

- 예를 들어 username대신 email을 식별값으로 하는 것이 더 적합한 사이트의 경우, django의 user model은 기본적으로 username을 식별값으로 사용하기 때문에 적합하지 않음

django는 현재 프로젝트에서 사용할 user model을 결정하는 AUTH_USER_MODEL 설정값으로 default user model을 재정의(override)할 수 있도록 함

### AUTH_USER_MODEL

- 프로젝트가 user를 나타낼때 사용하는 모델
- 프로젝트가 진행되는 동안(모델을 만들고 마이그레이션 한 후) 변경 불가
- 프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 첫번째 마이그레이션에서 사용할 수 있어야함
  + 즉 첫번째 마이그레이션 전에 확정지어야하는 값
- 다음의 기본값을 가진다
```python
# settings.py

AUTH_USER_MODEL = 'auth.User'
```

### settings의 로드 구조

AUTH_USER_MODEL은 settings.py에 보이지 않는데 어디에 기본값이 있는가

settings.py 파일은 사실 global_settings.py를 상속받아 재정의한다

https://github.com/django/django/blob/main/django/conf/global_settings.py


## Custom User Model로 대체하기

대체하는 과정은 공식문서에도 기술되어있다

https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model

### 1. AbstrctUser를 상속받는 커스텀 User 클래스 작성

기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스 역시 완전히 같은 모습을 가지게 됨

```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

### 2. django 프로젝트에서 User를 나타내는데 사용하는 모델을 방금 생성한 커스텀 User 모델로 지정

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```

### 3. admin.py에 커스텀 User 모델을 등록

기존 User모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음

```python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

### AbstractUser

관리자 권한과 함께 완전한 기능을 가지고 잇는 User model을 구현하는 추상 기본 클래스

- abstract base classes (추상 기본 클래스)
  + 몇가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
  + 데이터베이스 테이블을 만드는데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가됨
  + https://docs.python.org/3/library/abc.html


### 데이터베이스 초기화

데이터베이스 초기화 후 마이그레이션(프로젝트 중간일 경우)

1. migrations 파일 삭제
   - migrations 폴더 및 __init__.py는 삭제하지 않음
   - 번호가 붙은 파일만 삭제
2. db.sqlite3 삭제
3. migrations 진행
   - makemigrations
   - migrate

