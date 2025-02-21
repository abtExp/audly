import os
import glob

class DATA_EXTRACTOR:
    def __init__(self, extractor_function):
        self.extractor_function = extractor_function
    
    def get_data_info(self, feature_source, target_source=''):
        return self.extractor_function(feature_source, target_source)       

def data_extractor(extractor_function):
    extractor = DATA_EXTRACTOR(extractor_function)
    return extractor

@data_extractor
def dir_extractor(feature_src: str, target_src: str = '') -> tuple[list[str], list[str]]:
    train_file_paths = glob.glob(os.path.join(feature_src, 'train/*'))
    valid_file_paths = glob.glob(os.path.join(feature_src, 'valid/*'))
    labels = [[[]*len(train_file_paths)], [[]*len(valid_file_paths)]]
    return [train_file_paths, valid_file_paths], labels