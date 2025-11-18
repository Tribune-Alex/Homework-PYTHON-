class Meta(type):
    def __new__(mcls, name, bases, attrs):
        for key,value in attrs.items():
            if callable(value) and not key.startswith("_"):
                raise ValueError(f"This method is not valid, Method should start from _")
        return super().__new__(mcls, name, bases, attrs)
    

class FirstClass(metaclass=Meta):
    def _test(self):
        return "This is valid method"
    

class SecondClass(metaclass=Meta):
    def test(self):
        return "That is not valid method"
