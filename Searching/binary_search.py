TARGET_NOT_FOUND = -1

UNIT_TEST_OUTPUT_WIDTH = 80
from random import seed, randint, choice
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # requires O(logn) so lets use recursion
        # T(N) = 1 + 2T(n/2)
        if (len(nums) == 0) or \
            (len(nums) == 1 and nums[0] != target):
            return TARGET_NOT_FOUND 
        # halfway point check also works for list with 1 item
        middle_index = len(nums) // 2
        if target == nums[middle_index]:
            return middle_index
        # since our sentinel is negative...
        # any "found" index (>=) would be the result
        return max(
            self.search(nums[0:middle_index], target),
            self.search(nums[middle_index:], target)
        )

class SearchTester:
    TEST_PASSED_SYMBOL = u'\u2713' # check
    TEST_FAILED_SYMBOL = u'\u274c' # cross
    
    def __init__(self, search_function, 
                 test_seed=0, list_size=6, list_min=-5, list_max=5):
        self.search_function = search_function
        seed(test_seed)
        # for simplicity, let's use the same list generation parameters 
        # for all calls in an instance of Tester.
        self.list_size = list_size
        self.list_min = list_min
        self.list_max = list_max
        
    def generate_nums_list(self):
        return [randint(self.list_min, self.list_max) for _ in range(self.list_size)]
    
    def generate_target(self, nums_list):
        return choice(nums_list)
    
    def display_test_header(self, function_being_tested="binary search",
                            test_case_name="", requirements_strings=[]):
        print(f" Testing {function_being_tested} ".center(UNIT_TEST_OUTPUT_WIDTH, "="))
        print(f" Case -- {test_case_name} ".center(UNIT_TEST_OUTPUT_WIDTH, '-'))
        if requirements_strings:
            print("Requirements")
            # turn the list of string requirements into what looks like a bullet list.
            print("\n".join([f"\t [~] {requirement}" for requirement in requirements_strings]))
        print('-' * UNIT_TEST_OUTPUT_WIDTH)
    
    def display_test_status(self, parameters_dict, return_value, expected_value):
        print("Parameters:\t", parameters_dict)
        print("Got:\t\t", return_value)
        print("Expected:\t", expected_value)
        print("Match?\t\t", 
              self.TEST_PASSED_SYMBOL if return_value == expected_value 
              else self.TEST_FAILED_SYMBOL)
    
    # test 1 - found (non zero return) + index!
    def test_element_found(self):
        self.display_test_header(test_case_name="Element Found",
                                 requirements_strings=["Non-zero result", "Index Match"])
        nums_with_target = self.generate_nums_list()
        target = self.generate_target(nums_with_target)
        parameters_dict = {"nums": nums_with_target, "target": target}
        search_result = self.search_function(nums_with_target, target)
        expected_result = nums_with_target.index(target)
        
        self.display_test_status(parameters_dict, search_result, expected_result)
        
    def test_element_not_found(self):
        # idea: generate a list, 
        # take the max/min, +- 1 respectively, search for that 
        # since it definitely wouldn't be in the list.
        pass
    
    
if __name__ == '__main__':
    mySolution = Solution()
    myTester = SearchTester(mySolution.search)
    myTester.test_element_found()
    
    
    
    
    