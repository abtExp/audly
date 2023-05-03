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

from typing import Tuple, Optional

import librosa
import torchaudio
from scipy.io import wavfile
from dask.distributed import Client

from audly.utils.base import BASE


def dataloader(load_function):
    loader = DATA_LOADER(load_function)
    return loader
    
    
class DATA_LOADER(BASE):
    def __init__(self, load_function):
        self.client = Client(processes=False)
        self.load_function = load_function
        
    def load_batch(self, features: list, targets: Optional[list])-> Tuple[np.ndarray, np.ndarray]:
        # Load Everything In Distributed Mode And Also Run Preprocessing And Augmenting In Distributed Mode.
        x, y = self.load_function(features, targets)
        
        # Run Preprocessing
        
        # Run Augmenting
        
        return x, y


@dataloader
def audio_loader(features, targets):
    signal, sampling_rate = wavfile.read(audio_path)
    return signal