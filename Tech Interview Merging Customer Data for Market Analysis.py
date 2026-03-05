import unittest
#unittest is Python’s built-in framework for testing. 
#unittest allows you to write "test cases" that automatically verify if your code is behaving exactly as expected.

def merge_customer_data(customerData1, m, customerData2, n):
    #Replaces the placeholder zeros in customerData1 with the actual data from customerData2, and then sorts the combined list.
    customerData1[m:] = customerData2
    #Re-sorts the combined list to ensure the final output is in the correct order.
    customerData1.sort()

class TestMinimalMerge(unittest.TestCase): #Creates a "Folder" for our tests
    # Normal Cases
    def test_standard(self): #Defines specific test case scenarios. Each method that starts with "test" is a separate test case.
        #This test case tests a basic merge of two equally sized sorted arrays.
        d1 = [101, 104, 107, 0, 0, 0]; merge_customer_data(d1, 3, [102, 105, 108], 3)
        self.assertEqual(d1, [101, 102, 104, 105, 107, 108])
        #merge_customer_data runs the function we want to test, and self.assertEqual checks if the result is what we expect.

    def test_diff_len(self):
        d1 = [1, 2, 0, 0, 0]; merge_customer_data(d1, 2, [3, 4, 5], 3)
        self.assertEqual(d1, [1, 2, 3, 4, 5])

    def test_overlap(self):
        d1 = [10, 20, 0, 0]; merge_customer_data(d1, 2, [10, 20], 2)
        self.assertEqual(d1, [10, 10, 20, 20])

    # Edge Cases
    def test_empty_2(self):
        d1 = [103]; merge_customer_data(d1, 1, [], 0)
        self.assertEqual(d1, [103])

    def test_empty_1(self):
        d1 = [0, 0]; merge_customer_data(d1, 0, [1, 2], 2)
        self.assertEqual(d1, [1, 2])

    def test_reverse_order(self):
        d1 = [10, 11, 0, 0]; merge_customer_data(d1, 2, [1, 2], 2)
        self.assertEqual(d1, [1, 2, 10, 11])

if __name__ == '__main__':
    #This line checks if the script is being run directly by you
    #It prevents the tests from running automatically if you were to "import" this file into a different program later.

    unittest.main(argv=[''], exit=False)
    #tells the unittest library to go find every function starting with the word test_ and execute it.