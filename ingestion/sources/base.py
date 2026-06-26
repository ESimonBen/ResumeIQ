# base.py
from abc import ABC, abstractmethod

class JobSource(ABC):
    @abstractmethod
    def fetch(self, keywords, max_pages=5):
        """
        Returns raw jobs in SOURCE FORMAT
        """
        pass

    def normalize(self, raw_job):
        """
        Returns normalized jobs
        """
        pass