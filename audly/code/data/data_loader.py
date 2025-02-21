# Using Dask For Multiprocessing and Distributed processing

# 1. Read an audio file.
# 2. Clip a fixed length segment starting from a random location in the audio.
# 2. Chunk it into fixed duration segments.
# 3. Scatter all chunks using dask.
# 4. Submit feature extraction task to all dast workers for each chunk.
# 5. Gather features from each chunk and append.
# 6. Pass to model.

# Use audiofile for faster audio file reading.
import numpy as np
import audiofile

from typing import Tuple, Optional

from audly.code.utils.base import BASE


def dataloader(load_function):
    loader = DATA_LOADER(load_function)
    return loader
    
    
class DATA_LOADER(BASE):
    def __init__(self, load_function):
        self.load_function = load_function
        
    def load_batch(self, features: list, targets: Optional[list])-> Tuple[np.ndarray, Optional[np.ndarray]]:
        x, y = self.load_function(features, targets)
        return x, y


@dataloader
def audio_loader(features, targets=None):
    x, y = [], []
    
    for feature in features:
        signal, sampling_rate = audiofile.read(feature)
        targ = []
        x.append(signal)
        y.append(targ)
    x = np.array(x)
    y = np.array(y)
    return x, y