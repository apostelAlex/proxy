# Rotating Proxy Scraper Framework

Ein skalierbares Scraping-Framework mit IP-Rotation über dedizierte Proxies oder eigene VPS-Infrastruktur. Ziel ist die zuverlässige Extraktion von Webdaten unter Berücksichtigung von IP-Rate-Limits und Blockierungen.

## Übersicht

Das System basiert auf einer modularen Architektur mit folgenden Komponenten:

- **Asynchrone Scraper-Worker** mit Proxy-Zuweisung
- **Zentral verwaltete Proxy-Liste** (lokale Datei oder API-Anbindung)
- **Dockerisierung** für Isolation und Skalierbarkeit
- **Optionales Logging** und erweiterbare Fehlerbehandlung

## Voraussetzungen

- Docker & Docker Compose
- Python 3.10+
- Proxies (HTTP/S, SOCKS5) mit oder ohne Authentifizierung

## Schnellstart

1. Repository klonen:

```bash
git clone https://github.com/username/rotating-scraper.git
cd rotating-scraper
```

2. Proxies konfigurieren:

Datei `proxies.txt` mit einer IP pro Zeile (Format: `http://[user:pass@]ip:port`):

```
http://user:pass@192.0.2.1:8000
socks5://192.0.2.2:1080
http://192.0.2.3:8080
```

3. Zielseiten definieren:

In `targets.csv` (einfaches CSV mit Spalten wie `url`, `id` o. Ä.):

```
url,id
https://example.com/page1,1
https://example.com/page2,2
```

4. Container starten:

```bash
docker-compose up --build --scale scraper=5
```

Jeder Container wird mit einem Proxy aus der Liste konfiguriert.

## Verzeichnisstruktur

```
.
├── core/
│   ├── proxy_manager.py       # Verwaltung und Rotation von Proxies
│   ├── scraper_worker.py      # Asynchrone Verarbeitung der Ziel-URLs
│   └── config.py              # Zeitlimits, Header, Einstellungen
├── data/
│   └── results.jsonl          # Ergebnisdaten im JSON Lines-Format
├── proxies.txt                # Liste der verfügbaren Proxies
├── targets.csv                # Zielseiten für den Abruf
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## Funktionen

- Rotation von Proxies pro Request oder pro Worker
- Asynchrone Verarbeitung für hohe Parallelität
- Erweiterbares Fehler- und Timeout-Handling
- Logging mit URL, Proxy, Statuscode und Zeitstempel
- Modulare Architektur für spätere Erweiterungen (z. B. Captcha-Bypass, Proxy-Health-Checks, API-Control-Plane)

## Hinweise

- Achte auf die rechtlichen Rahmenbedingungen und die Nutzungsbedingungen der Zielseiten.
- Verwende nur Proxies, für deren Nutzung du berechtigt bist.
- Dieses Framework ist nicht für aggressives Crawling oder Missbrauch vorgesehen.

## Lizenz

MIT-Lizenz. Nutzung auf eigene Verantwortung.
