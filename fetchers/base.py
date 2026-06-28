from abc import ABC, abstractmethod


class BaseFetcher(ABC):
    """
    Base class for all fetchers.
    """

    @abstractmethod
    def fetch(self, url: str):
        """
        Fetch data from the given URL.
        """
        pass
