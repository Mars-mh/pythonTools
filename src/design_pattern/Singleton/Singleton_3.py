"""
使用 __new__ 实现单例模式
"""


class Singleton(object):
    _instance = None
    _flag = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        else:
            pass

        return cls._instance

    def __init__(self, name):
        """
        如果不加以限制，init 会被重复执行
        :param name:
        """
        if Singleton._flag:
            print('Instance already existed !')
            pass
        else:
            self.name = name
            Singleton._flag = True


if __name__ == '__main__':
    my_class_1 = Singleton('name_1')
    my_class_2 = Singleton('name_2')

    print(f"class_1 id is {id(my_class_1)}")
    print(f"class_2 id is {id(my_class_2)}")

    print(f"They are same: {id(my_class_1) == id(my_class_2)}")

    print(f"class-1`s name is {my_class_1.name} and class-2`s name is {my_class_2.name}")
