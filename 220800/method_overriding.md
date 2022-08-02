```python
class Person:
    counts = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call_name(self):
        return f'dd대전 2반 {self.name}, {self.age}살 입니다!'

    def call_age(self):
        return f'{self.age}살 입니다!'

    @staticmethod
    def hello():
        return '안녕하세요!'


class Student(Person):
    @staticmethod
    def call_name(name):
        return f'대전 2반 {name} 입니다!'


person1 = Person("김성준", 25)
student1 = Student("박승재", 25)
print(student1.call_name('김진호'))
```

위의 경우 staticmethod에 의해 메서드는 오버라이딩 된다. div()를 사용해 클래스 및 인스턴스의 내용을 확인할 수 있다.