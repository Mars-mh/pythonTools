"""
learn singleton
    使用函数装饰器实现单例模式
"""


def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        else:
            pass

        return _instance[cls]

    return inner


@singleton
class MyClass:
    __cls_name = "None"

    def __init__(self):
        pass

    @property
    def cls_name(self):
        return self.__cls_name

    @cls_name.setter
    def cls_name(self, new_name):
        self.__cls_name = new_name


if __name__ == '__main__':
    my_class_1 = MyClass()
    my_class_2 = MyClass()

    print(f"class_1 id is {id(my_class_1)}")
    print(f"class_2 id is {id(my_class_2)}")

    print(f"They are same: {id(my_class_1) == id(my_class_2)}")

