exists 관련, Django의 쿼리셋은 lazy loading(지연 평가)를 기본적으로 따르는데, 여기서 평가란 실제로 DB에 쿼리를 날리는 것을 의미한다. 즉 Django는 ORM 명령을 실행했다고 해서 바로 쿼리를 날리지 않고 마지막 필요한 순간에 날리게 된다.
​if queryset 으로 T/F 판단을 할 때는 평가가 이루어져 DB에 쿼리를 날리게 된다. 하지만 if queryset.exists() 로 T/F 판단을 할 때는 평가가 이루어지지 않고 쿼리셋이 존재하는지만 검사한다.그래서 불필요하게 쿼리를 발생시키지 않고 T/F만 빠르게 검사할 수 있으므로 exists()가 웬만하면 더 빠르다.

​참고) https://docs.djangoproject.com/en/3.2/ref/models/querysets/#django.db.models.query.QuerySet.exists