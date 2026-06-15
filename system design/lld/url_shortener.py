import string
import threading
from typing import Dict, Optional


# 1. THE DATA MODEL
class URLMapping:
    """Represents the core database entity."""

    def __init__(self, id: int, long_url: str, short_key: str):
        self.id = id
        self.long_url = long_url
        self.short_key = short_key


# 2. THE REPOSITORY LAYER (Data Storage)
class URLRepository:
    """Manages data storage. Implemented as an interface/abstract concept."""

    def __init__(self):
        # Thread-safe lock to prevent race conditions during parallel updates
        self._lock = threading.Lock()
        self._counter = 100000               # Atomic ID counter
        self._storage_by_key: Dict[str, URLMapping] = {}

    def get_next_id(self) -> int:
        """Safely increments and returns the next unique ID."""
        with self._lock:
            current = self._counter
            self._counter += 1
            return current

    def save(self, mapping: URLMapping) -> None:
        """Saves the mapping to memory."""
        with self._lock:
            self._storage_by_key[mapping.short_key] = mapping

    def find_by_key(self, short_key: str) -> Optional[URLMapping]:
        """Retrieves a mapping using the short key."""
        return self._storage_by_key.get(short_key)


# 3. THE CODE ALGORITHM (Base62 Strategy Pattern)
class Base62Encoder:
    """Handles the math conversion between numeric IDs and short strings."""
    ALPHABET = string.digits + string.ascii_lowercase + \
        string.ascii_uppercase  # 62 chars

    @classmethod
    def encode(cls, unique_id: int) -> str:
        """Converts an integer ID into a unique Base62 string string."""
        if unique_id == 0:
            return cls.ALPHABET[0]

        chars = []
        while unique_id > 0:
            unique_id, remainder = divmod(unique_id, 62)
            chars.append(cls.ALPHABET[remainder])

        return "".join(reversed(chars))


# 4. THE CORE SERVICE LAYER (Business Logic)
class URLShortenerService:
    """The central brain orchestrating the encoding and storage layers."""

    def __init__(self, repository: URLRepository):
        self.repository = repository

    def shorten(self, long_url: str) -> str:
        """Core business logic to create a short link."""
        # Step A: Fetch a globally unique ID
        next_id = self.repository.get_next_id()

        # Step B: Run the encoding math algorithm
        short_key = Base62Encoder.encode(next_id)

        # Step C: Persist the object mapping
        mapping = URLMapping(
            id=next_id, long_url=long_url, short_key=short_key)
        self.repository.save(mapping)

        return short_key

    def resolve(self, short_key: str) -> str:
        """Core business logic to fetch a original link."""
        mapping = self.repository.find_by_key(short_key)
        if not mapping:
            raise ValueError(f"Short key '{short_key}' does not exist.")
        return mapping.long_url


if __name__ == "__main__":
    # Initialize our system dependencies
    repo = URLRepository()
    shortener = URLShortenerService(repository=repo)

    # 1. Shorten a link
    original_url = "https://google.com"
    key = shortener.shorten(original_url)

    print(f"Original URL: {original_url}")
    print(f"Generated Key: {key}")  # Outputs something like: q0U

    # 2. Resolve a link back
    resolved_url = shortener.resolve(key)
    print(f"Resolved URL:  {resolved_url}")

    # 3. Simulate failure
    try:
        shortener.resolve("FakeKey")
    except ValueError as e:
        print(f"Error Caught:  {e}")
