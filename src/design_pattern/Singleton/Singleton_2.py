"""
使用类装饰器实现单例
"""


class Singleton:
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self, *args, **kwargs):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        else:
            pass

        return self._instance[self._cls]


@Singleton
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


