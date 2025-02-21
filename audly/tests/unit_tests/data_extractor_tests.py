import sys

sys.path.insert(0, './')

from audly.tests.test_factory import TEST_BUNDLE
from audly.code.data.data_extractor import dir_extractor

bundle = TEST_BUNDLE('data_extractor_test_bundle')

@bundle.add_test('data_extraction_test', {'x': 'C:/Users/abtex/Downloads/audios'})
def data_extraction_test(x):
    extractor = dir_extractor
    features, targets = extractor.get_data_info(x)
    print(features)
    print(targets)