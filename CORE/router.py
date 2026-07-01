# core/router.py

from plugins.base import BaseExtractor
from CORE.registry import PluginRegistry


class Router:
    """
    Responsible for finding the correct extractor
    for a given URL.
    """

    def __init__(self, registry: PluginRegistry):
        self.registry = registry

    def resolve(self, url: str) -> BaseExtractor:
        """
        Return the plugin that supports the URL.
        """

        for plugin in self.registry.get_plugins():

            if plugin.supports(url):
                return plugin

        raise ValueError(
            f"No extractor found for URL: {url}"
        )
