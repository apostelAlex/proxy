import itertools
import random
from pathlib import Path

class ProxyManager:
    """Simple proxy manager loading proxies from a file and rotating them."""

    def __init__(self, proxies_file: str = "proxies.txt", shuffle: bool = True) -> None:
        self.proxies_file = Path(proxies_file)
        self.proxies = self._load_proxies()
        if shuffle:
            random.shuffle(self.proxies)
        self._cycle = itertools.cycle(self.proxies) if self.proxies else None

    def _load_proxies(self):
        if not self.proxies_file.exists():
            return []
        proxies = []
        with self.proxies_file.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    proxies.append(line)
        return proxies

    def get_next_proxy(self) -> str | None:
        """Return the next proxy from the rotation or None if none available."""
        if self._cycle:
            return next(self._cycle)
        return None
