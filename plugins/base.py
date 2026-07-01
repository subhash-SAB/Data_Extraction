# plugins/base.py

from abc import ABC, abstractmethod


class BaseExtractor(ABC):
    """
    Base class for all website extractors.

    Every extractor (Amazon, GitHub, Wikipedia, etc.)
    must inherit from this class.
    """
    def __init__(self, fetcher, parser):
        self.fetcher = fetcher
        self.parser = parser

    @abstractmethod
    def name(self) -> str:
        """
        Returns the extractor name.

        Example:
            AmazonExtractor
            WikipediaExtractor
        """
        pass

    @abstractmethod
    def supports(self, url: str) -> bool:
        """
        Returns True if this extractor
        can handle the given URL.
        """
        pass

    @abstractmethod
    def strategy(self) -> str:
        """
        Returns extraction strategy.

        Example:
            STATIC_HTML
            REST_API
            GRAPHQL
            PLAYWRIGHT
        """
        pass

    @abstractmethod
    def supported_fields(self) -> list[str]:
        """
        Returns all fields this extractor supports.
        """
        pass

    @abstractmethod
    def required_fields(self) -> list[str]:
        """
        Returns fields that must always be extracted.
        """
        pass

    @abstractmethod
    def extract(
        self,
        url: str,
        fields: list[str]
    ) -> dict:
        """
        Extract requested fields
        and return structured data.
        """
        pass
