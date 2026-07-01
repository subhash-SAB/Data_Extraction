from CORE.router import Router

class ExtractionEngine:
    
    def __init__(self, router: Router):
        self.router = router

    def extract(
        self,
        url: str,
        fields: list[str],
        output_format: str = "json"
    ) -> dict:
        """
        Extract requested fields from a URL.
        """

        # Step 1: Find the correct plugin
        plugin = self.router.resolve(url)

        # Step 2: Ask plugin to extract
        data = plugin.extract(url, fields)

        # Step 3: Return extracted data
        return data
