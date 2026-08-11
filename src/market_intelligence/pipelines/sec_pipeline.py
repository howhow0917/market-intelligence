from market_intelligence.collectors.sec import fetch_nvidia_filings
from market_intelligence.normalizers.sec import normalize_sec_filing


def run():
    filings = fetch_nvidia_filings(limit=10)

    events = []

    for filing in filings:
        event = normalize_sec_filing(filing)
        events.append(event)

    return events


if __name__ == "__main__":
    events = run()

    for event in events:
        print(event)
