from dataclasses import dataclass, field

@dataclass
class Config:
    timeout: int = 10
    headers: dict = field(default_factory=lambda: {
        "User-Agent": "rotating-scraper/0.1"
    })
    results_file: str = "data/results.jsonl"
