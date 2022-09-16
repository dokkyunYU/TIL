from clipboard import copy  # pip install clipboard

# 입력된 문자열을 변환해서 자동으로 복사한 상태로 만들어준다
copy(input().replace(" ", "_").replace(".", ""))
