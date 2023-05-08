import sys

sys.path.insert(0, './')

from audly.tests.test_factory import TEST_BUNDLE
from audly.code.data.preprocess import preprocess

bundle = TEST_BUNDLE('preprocess_test_bundle')

@bundle.add_test('preprocess_creation_test', {'x': ['Anubhav', 'Sheldon'], 'y': ['There', 'world']})
def preprocess_creation_test(x, y):    
    @preprocess(False)
    def add_hello(inp_str):
        return 'hello' + inp_str

    results_x, results_y = add_hello(x, y)
    
    print(results_x, results_y)
    

@bundle.add_test('preprocess_sample_test', {'x': [[1, 2, 3]], 'y': [[4, 5, 6]]})
def preprocess_sample_test(x, y):    
    @preprocess(True)
    def square(inp_arr):
        return [i**2 for i in inp_arr]
    
    result_x, result_y = square(x, y)
    print(result_x, result_y)