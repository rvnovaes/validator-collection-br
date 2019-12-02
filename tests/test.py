
import unittest
import validatorsGMP as val

class UnitTest(unittest.TestCase):

    cellphoneValidatorsTests = [
        ["33991749686", True],
        ["XXX", False],
        ["33 9 9174 - 7498", True],
        ["(37)982159000", True],
        ["37J982159000", False],
        ["+(55)31991749686", True],
        ["", False]
    ]

    alphanumericValidatorsTests = [
        ["123456", True],
        ["XXX", True],
        ["XXX456", True],
        ["", False],
        ["....", False],
        ["asas.5464", False],
        ["", False]
    ]

    def testCellphoneValidator(self):
        for phone in self.cellphoneValidatorsTests:
            self.assertEqual(val.cellphoneValidator(phone[0]), phone[1])


    def testAlphanumericValidator(self):
        for value in self.alphanumericValidatorsTests:
            self.assertEqual(val.alphanumericValidator(value[0]), value[1])


if __name__ == '__main__':
    unittest.main()



