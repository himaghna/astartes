"""Abstract Sampling class"""
from abc import ABC, abstractmethod


class Sampler(ABC):
    @abstractmethod
    def __init__(self, X, y=None, distance_matrix=None, **kwargs):
        pass

    @abstractmethod
    def get_sample(self):
        """
        Get one sample.

        """
        pass

    @abstractmethod
    def get_sample_id(self):
        """
        Get the id of the next sample.

        """
        pass

    @abstractmethod
    def get_batch_sample(self, n_samples):
        """
        Get a batch of samples

        """
        pass

    @abstractmethod
    def get_batch_sample_idx(self, n_samples):
        """
        Get idx of the next batch of samples.

        """
        pass
