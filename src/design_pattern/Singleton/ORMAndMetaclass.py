"""
元编程用于ORM
例：操作数据库
"""


class Field(object):
    """
    数据字段类
    """

    def __init__(self, name, clo_type):
        self.name = name
        self.clo_type = clo_type

    def __str__(self):
        return f"<{self.__class__.__name__}:{self.name}>"


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntField(Field):
    def __init__(self, name):
        super(IntField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(mcs, name, bases, attrs: dict):
        if name == 'Model':
            return type.__new__(mcs, name, bases, attrs)
        print(f'Found model: {name}')

        mappings = dict()

        for k, v in attrs.items():
            if isinstance(v, Field):
                print(f'Found mapping: {k} ==> {v}')
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        # 保存属性和列的映射关系
        attrs['__mappings__'] = mappings

        # 将表名设置为类名
        attrs['__table__'] = name

        return type.__new__(mcs, name, bases, attrs)
