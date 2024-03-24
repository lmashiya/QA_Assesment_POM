from jproperties import Properties


class ConfigFactory:

    def __init__(self):
        """
        Initialize class , Loads properties from the 'Resources/config.properties' file.
        """
        self.configs = Properties()
        with open(r"Resources/config.properties", "rb") as read_prop:
            self.configs.load(read_prop)

    def fetch(self, property_key: str) -> str:
        """
        Fetch a specific property value by its key.
        """
        return self.configs.get(property_key)[0]

    def factorial_page_url(self) -> str:
        """
        Fetch page url.
        """
        return self.fetch("FACTORIAL_PAGE_URL")

    def browser(self) -> str:
        """
        Fetch browser property value.
        """
        return self.fetch("BROWSER")

    def timeout(self) -> int:
        """
        Fetch the timeout property value.
        """
        return int(self.fetch("TIMEOUT"))
