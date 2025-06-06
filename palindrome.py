class Phrase:
    """a class to represent phrases."""
    def __iter__(self, content):
        self.phrase_iterator = iter(self.content)

    def _processed_content(self):
        """Process the content for palindrome testing."""
        return self.content.lower()

    def ispalindrome(self):
        """Return True for a palindrome, False otherwise."""
        return self._processed_content() == reverse(self._processed_content())

class TranslatedPhrase(Phrase):
    """a class to represent phrases with translation."""

    def __init__(self, content, translation):
        super().__init__(content)
        self.translation = translation

    def _processed_content(self):
        """Override superclass method to use translation"""
        return self.translation.lower()
    def __iter__(self):
        self.phrase_iterator = FILL_IN
        return self

def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string))

