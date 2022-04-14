"""
使用 metaclass 创建单例对象
理解在 metaclass 中 new 与 call 的关系
"""


class SingletonMetaclass(type):
    _instance = None

    def __new__(mcs, *args, **kwargs):
        """

        :param args: None
        :param kwargs: None
        """
        if not mcs._instance:
            mcs._instance = super(SingletonMetaclass, mcs).__new__(mcs, *args, **kwargs)
        else:
            pass

        print('__new__')
        return mcs._instance

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonMetaclass, cls).__call__(cls)
        else:
            pass

        print('__call__')
        return cls._instance


class MyClass(metaclass=SingletonMetaclass):
    pass


if __name__ == '__main__':

    print('__main__ is running ...')
    my_class_1 = MyClass()
    my_class_2 = MyClass()

    print(f"class_1 id is {id(my_class_1)}")
    print(f"class_2 id is {id(my_class_2)}")

    print(f"They are same: {id(my_class_1) == id(my_class_2)}")
