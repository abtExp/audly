import numpy as np
from typing import Tuple

from audly.code.utils import CONFIG, BASE
from audly.code.data.data_extractor import dir_extractor, DATA_EXTRACTOR
from audly.code.data.data_loader import audio_loader, DATA_LOADER
    

class DATA_FEEDER(BASE):
    def __init__(self, config_path: str=''):
        self.config = CONFIG(config_path)
        self.data_conf = self.config.dataset
        
        self.extractor = self.get_extractor(self.data_conf.source_type)
        self.loader = self.get_loader(self.data_conf.feature_type, self.data_conf.target_type)
        
        features, targets = self.extractor.get_data_info(self.data_conf.feature_source, self.data_conf.target_source)
        features, targets = np.array(features), np.array(targets)
        self.train_features, self.valid_features, self.train_targets, self.valid_targets = *features, *targets

        self.train_indices = [i for i in range(len(self.train_features))]
        self.valid_indices = [i for i in range(len(self.valid_features))]
        
        self.shuffle()
        
        self.train_iterator = 0
        self.valid_iterator = 0
    
    def shuffle(self):
        np.random.shuffle(self.train_indices)
        np.random.shuffle(self.valid_indices)
    
    def get_extractor(self, source_type: str)-> DATA_EXTRACTOR:
        if source_type == 'dir':
            return dir_extractor
    
    def get_loader(self, feature_type: str, target_type: str)-> DATA_LOADER:
        if feature_type == 'audio':
            return audio_loader
    
    def get_batch(self, data_split: str='train')-> Tuple[np.ndarray, np.ndarray]:
        def step(iterator: int, num_samples: int, batch_size: int)-> int:
            iterator += 1
            
            if iterator > len(indices)//batch_size:
                self.shuffle()
                iterator = 0
            
            return iterator
        
        if data_split == 'train':
            features = self.train_features
            targets = self.train_targets
            indices = self.train_indices
            iterator = self.train_iterator
            batch_size = self.data_conf.train_batch_size
            self.train_iterator = step(iterator, len(indices), batch_size)
        else:
            features = self.valid_features
            targets = self.valid_targets
            indices = self.valid_indices
            iterator = self.valid_iterator
            batch_size = self.data_conf.valid_batch_size
            self.valid_iterator = step(iterator, len(indices), batch_size)
        
        load_indices = indices[iterator*batch_size:(iterator+1)*batch_size]
        print(indices)
        print(features)
        print(targets)
        print(iterator)
        print(load_indices)
        batch_features, batch_targets = features[load_indices], targets[load_indices]
        
        x, y = self.loader.load_batch(batch_features, batch_targets)
        
        return x, y
