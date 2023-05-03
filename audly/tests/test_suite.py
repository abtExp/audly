from time import time


class TEST_SUITE(object):
    test_list = []
    
    @staticmethod
    def add_test(test):
        TEST_SUITE.test_list.append(test)
        
    @staticmethod
    def run_tests():
        print('----Running Test Suite----')
        successful_tests = 0
        failed_tests = []
        for test in TEST_SUITE.test_list:
            start_time = time()
            print(f'############################ Test Run : {test.test_name} ############################')
            try:
                test()
                successful_tests += 1
            except Exception as e:
                print(f'!!!!!!!!!!!!!!!!! Test Failed : Exception Occured : {e} !!!!!!!!!!!!!!!!!')
                failed_tests.append(test.test_name)
            end_time = time()
            print(f'------Finished Running Test : {test.test_name}, Took : {end_time - start_time} seconds to run.-------')
        print('--Finished Running Test Suite--')
        print(f'{successful_tests} out of {len(TEST_SUITE.test_list)} tests passed successfully.')
        print(f'Failed Tests : {", ".join(failed_tests)}')
            
    @staticmethod
    def list_tests():
        i = 0
        for test in TEST_SUITE.test_list:
            print(f'{i}. {test}')
            print(test)
            print('---------------------------------------------')