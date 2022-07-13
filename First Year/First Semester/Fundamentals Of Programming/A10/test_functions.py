import unittest
from main import GenericSort, Sorting, Filter

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def testGnomeSort(self):
        list = [1,4,2,3]
        Sorting.sort(list)
        self.assertEqual(list, [1,2,3,4])
        GenericSort.sort(GenericSort)

        Sorting.sort(list,None,reverse=True)
        self.assertEqual(list, [4,3,2,1])

    def even_number(self, x):
        return x%2 == 0

    def testfilter(self):
        list = [1, 4, 2, 3]
        l = Filter.filter(self.even_number, list)
        self.assertEqual(l, [4, 2])

#if __name__ == '__main__':
    #unittest.main()
