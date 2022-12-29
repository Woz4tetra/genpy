from io import StringIO
from sample.msg._TestMsgArray import TestMsgArray
from sample.msg._TestString import TestString

if __name__ == '__main__':
    x = TestMsgArray([TestString('a'.encode('utf-8')),
        TestString('b'.encode('utf-8'))],
        (TestString('c'.encode('utf-8'))),
        (0.1, 0.2, 0.3))
    buff = StringIO()
    x.serialize(buff)
    assert buff == TestMsgArray.deserialzier(buff).serialize()
