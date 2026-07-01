from plugins.base import BaseExtractor

class PluginRegistry:

    def __init__(self):
        self._plugins = []

    def register(self, plugin):
        self._plugins.append(plugin)

    def get_plugins(self):
        return self._plugins
