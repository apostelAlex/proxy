import asyncio
import csv
import json
from pathlib import Path

import aiohttp

from .proxy_manager import ProxyManager
from .config import Config


def load_targets(filename: str = "targets.csv") -> list[str]:
    """Read target URLs from a CSV file."""
    targets = []
    path = Path(filename)
    if not path.exists():
        return targets
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            url = row.get("url")
            if url:
                targets.append(url)
    return targets


async def fetch(session: aiohttp.ClientSession, url: str, proxy: str | None, config: Config) -> dict:
    try:
        async with session.get(url, proxy=proxy, timeout=config.timeout) as resp:
            text = await resp.text()
            return {
                "url": url,
                "status": resp.status,
                "proxy": proxy,
                "body": text[:1000],
            }
    except Exception as e:
        return {
            "url": url,
            "proxy": proxy,
            "error": str(e),
        }


async def run(targets: list[str], proxy_manager: ProxyManager, config: Config) -> list[dict]:
    async with aiohttp.ClientSession(headers=config.headers) as session:
        tasks = []
        for url in targets:
            proxy = proxy_manager.get_next_proxy()
            tasks.append(fetch(session, url, proxy, config))
        return await asyncio.gather(*tasks)


def save_results(results: list[dict], filename: str):
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        for item in results:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
