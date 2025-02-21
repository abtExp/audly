import sys

sys.path.insert(0, './')

from audly.tests.test_factory import TEST_BUNDLE
from audly.code.data.data_feeder import DATA_FEEDER

bundle = TEST_BUNDLE('data_feeder_test_bundle')

@bundle.add_test('data_feeding_test', {'config_path': 'C:/Users/abtex/Desktop/projects/audly/audly/configs/config.yaml'})
def data_feeding_test(config_path):
    feeder = DATA_FEEDER(config_path)
    x, y = feeder.get_batch()

    print(x.shape)
    print(y.shape)