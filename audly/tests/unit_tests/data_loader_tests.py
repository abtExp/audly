import sys

sys.path.insert(0, './')

from audly.tests.test_factory import TEST_BUNDLE
from audly.code.data.data_loader import audio_loader
# from audly.code.data.data_feeder improt data_feeder

bundle = TEST_BUNDLE('data_loader_test_bundle')

@bundle.add_test('data_loading_test', {'x': 'C:/Users/abtex/Downloads/audios/train/not_like_us_2.mp3'})
def data_loading_test(x):    
    loader = audio_loader
    audio, sr = loader.load_batch([x], [''])
    print(audio.shape)
    print('Sample Rate:', sr)