

class A:
    def __new__(cls, **kwargs):
        print(f'calling __new__, {cls}')
        return super(cls).__new__(cls, **kwargs)

    def __init__(self, **kwargs):
        print('calling init', self)

