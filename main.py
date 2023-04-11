class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.key_dict = tuple(self.__dict__.keys())
        self.len_attr = len(kwargs)

    def __check_key(self, key):
        if type(key) != int or not (-self.len_attr <= key < self.len_attr):
            raise IndexError('неверный индекс поля')

    def __setitem__(self, key, value):
        self.__check_key(key)
        setattr(self, self.key_dict[key], value)

    def __getitem__(self, key):
        self.__check_key(key)
        return getattr(self, self.key_dict[key])