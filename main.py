import asyncio

from core.proxy_manager import ProxyManager
from core.scraper_worker import load_targets, run, save_results
from core.config import Config


def main():
    config = Config()
    targets = load_targets()
    proxy_manager = ProxyManager()
    results = asyncio.run(run(targets, proxy_manager, config))
    save_results(results, config.results_file)


if __name__ == "__main__":
    main()
