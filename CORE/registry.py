from plugins.base import BaseExtractor

class PluginRegistry:
 
   def _init_(self):
      self._plugin: list[BaseExtractor]=[]

   def register(self, plugin: BaseExtractor):
      self._plugin.append(plugin)

   def get_plugin(self) -> list[BaseExtractor]:
      return self._plugin
   def clear(self):   
      self._plugin.clear()
 