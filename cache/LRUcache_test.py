from unittest import TestCase, main
from cash.LRUcache import LRUcache


class LRUtest(TestCase):
    def setUp(self):
        self.data = LRUcache(3)
        self.data.put(1, 2)
        self.data.put(2, 3)
        self.data.put(3, 4)

    def test_get(self):
        self.assertEqual(self.data.get(1), 2)
    def test_put(self):
        self.data.put(5,'data')
        self.assertEqual(self.data.get(5),'data')

if __name__ == '__main__':
    main()

