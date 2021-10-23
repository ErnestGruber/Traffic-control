from unittest import TestCase, main
from bin_text import bin_dict, json_dict
class bin_dict(TestCase):
    def setUp(self):
        self.file_output = 'bin_test_data.txt'
        self.dict = {}

    def go_to_bin_dict(self):
        self.assertEqual(self.file_output.go_to_bin_dict(), {'0111' : '1110'})

if __name__ == '__main__':
    main()
