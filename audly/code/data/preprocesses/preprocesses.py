import librosa
import numpy as np


def fourier_transform(signal, n_fft, hop_length, trim=True):
    if trim:
        signal, _ = librosa.effects.trim(signal)
    
    stft = np.abs(librosa.stft(signal, n_fft=n_fft, hop_length=hop_length))
    return stft


def spectrogram(stft):
    spec = librosa.amplitude_to_db(stft, ref=np.max)
    return np.mean(spec)[0]


def melspectrogram(signal, sr):
    melspec_signal = librosa.feature.melspectrogram(signal, sr=sr)
    melspec = librosa.amplitude_to_db(melspec_signal, ref=np.max)
    return np.mean(melspec)[0]
    

def harmonics_and_perceptuals(signal):
    harmonics, perceptuals = librosa.effects.hpss(signal)
    return np.mean(harmonics), np.mean(perceptuals)


def spectral_centroids(signal, sr):
    spectral_centroids = librosa.feature.spectral_centroid(signal, sr=sr)[0]
    spectral_centroids_delta = librosa.feature.delta(spectral_centroids)
    spectral_centroids_accelerate = librosa.feature.delta(spectral_centroids, order=2)
    
    return np.mean(spectral_centroids), np.mean(spectral_centroids_delta), np.mean(spectral_centroids_accelerate)


def chromogram(signal, sr, hop_length):
    chromagram = librosa.feature.chroma_stft(signal, sr=sr, hop_length=hop_length)
    return np.mean(chromagram)


def tempo(signal, sr):
    tempo_y, _ = librosa.beat.beat_track(signal, sr=sr)
    return tempo_y


def spectral_rolloff(signal, sr):
    spectral_rolloff = librosa.feature.spectral_rolloff(signal, sr=sr)[0]
    return np.mean(spectral_rolloff)


def spectral_flux(signal, sr):
    onset_env = librosa.onset.onset_strength(y=signal, sr=sr)
    return np.mean(onset_env)


def spectral_bandwidth(signal, sr):
    spectral_bandwidth_2 = librosa.feature.spectral_bandwidth(signal, sr=sr)[0]
    spectral_bandwidth_3 = librosa.feature.spectral_bandwidth(signal, sr=sr, p=3)[0]
    spectral_bandwidth_4 = librosa.feature.spectral_bandwidth(signal, sr=sr, p=4)[0]
    
    return np.mean(spectral_bandwidth_2), np.mean(spectral_bandwidth_3), np.mean(spectral_bandwidth_4)


def mfcc_features(signal, sr, n_mfcc):
    mfcc_feature = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=n_mfcc)
    mfcc_delta = librosa.feature.delta(mfcc_feature)
    mfcc_accelerate = librosa.feature.delta(mfcc_feature, order=2)
    
    return np.mean(mfcc_feature, axis=1), np.mean(mfcc_delta, axis=1), np.mean(mfcc_accelerate, axis=1)


def zero_crossings(signal):
    zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(signal)[0])
    zero_crossing = np.sum(librosa.zero_crossings(signal, pad=False))
    
    return zero_crossing_rate, zero_crossing


