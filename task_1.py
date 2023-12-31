# Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и возвращает
# их плоское представление, т. е. последовательность, состоящую из вложенных элементов. Функция test в коде ниже также
# должна отработать без ошибок.

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_iter = iter(self.list_of_list)
        self.result = []
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.result) == self.cursor:
            self.result = None
            self.cursor = 0
            while not self.result:
                self.result = next(self.list_iter)
        return self.result[self.cursor]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()