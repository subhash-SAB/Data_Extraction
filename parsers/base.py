from abc import ABC, abstractmethod


class BaseParser(ABC):
    """
    Base class for all parsers.
    """

    @abstractmethod
    def parse(self, content):
        """
        Convert raw content into a structured object.
        """
        pass
