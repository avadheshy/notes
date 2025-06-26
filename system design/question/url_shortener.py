import time
from enum import Enum


class Expiry(Enum):
    NEVER = 0
    ONE_HOUR = 3600
    ONE_DAY = 86400
    ONE_WEEK = 86400 * 7
    ONE_MONTH = 86400 * 30


class Base62:
    ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    @staticmethod
    def encode(num):
        if num == 0:
            return Base62.ALPHABET[0]
        base62 = []
        while num:
            num, rem = divmod(num, 62)
            base62.append(Base62.ALPHABET[rem])
        return ''.join(reversed(base62))


class URLShortener:
    def __init__(self):
        self.count_id = int(time.time())  # Unique counter
        self.short_url_map = {}  # short_code -> (long_url, expiry_time, access_count)
        self.base_url = "https://short.ly/"

    def shorten_url(self, long_url, alias=None, expiry=Expiry.NEVER):
        """Shorten a URL with an optional custom alias and expiry time."""
        if alias:
            if alias in self.short_url_map:
                raise ValueError("Alias already exists")
            short_code = alias
        else:
            self.count_id += 1
            short_code = Base62.encode(self.count_id)

        expiry_time = int(time.time()) + expiry.value if expiry.value else None
        self.short_url_map[short_code] = (long_url, expiry_time, 0)
        return self.base_url + short_code

    def get_long_url(self, short_url):
        """Retrieve the original URL and update access count."""
        key = short_url.replace(self.base_url, "")

        if key not in self.short_url_map:
            return "Error: Short URL not found."

        long_url, expiry_time, count = self.short_url_map[key]

        if expiry_time and expiry_time < int(time.time()):
            del self.short_url_map[key]
            raise ValueError("Error: This URL has expired.")

        # Update access count
        self.short_url_map[key] = (long_url, expiry_time, count + 1)
        return long_url

    def get_url_redirect_count(self, short_url):
        """Return the number of times a short URL has been accessed."""
        key = short_url.replace(self.base_url, "")
        if key in self.short_url_map:
            return self.short_url_map[key][2]
        return "Error: Short URL not found."


# Example Usage
if __name__ == "__main__":
    shortener = URLShortener()
    
    # Generate a short URL
    short_url = shortener.shorten_url("https://example.com", expiry=Expiry.ONE_HOUR)
    print("Shortened URL:", short_url)
    
    # Retrieve the long URL multiple times
    print("Original URL:", shortener.get_long_url(short_url))
    print("Original URL:", shortener.get_long_url(short_url))
    print("Redirect Count:", shortener.get_url_redirect_count(short_url))
    print("Original URL:", shortener.get_long_url(short_url))
    # Check the redirect count
    print("Redirect Count:", shortener.get_url_redirect_count(short_url))
