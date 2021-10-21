from unittest import TestCase, main
from LRUcache import LRUcache


class LRUtest(TestCase):
    def setUp(cls):
        cls.p = LRUcache(3)
        cls.p.put(1, 2)
        cls.p.put(2, 3)
        cls.p.put(3, 4)

    def test_get(self):
        self.assertEqual(self.p.get(1), 2)


if __name__ == '__main__':
    main()

