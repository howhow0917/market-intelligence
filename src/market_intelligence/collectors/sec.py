import json
import urllib.request


SEC_URL = "https://data.sec.gov/submissions/CIK0001045810.json"

HEADERS = {
    "User-Agent": "MarketIntelligence research tsaishunghow@gmail.com"
}


def fetch_nvidia_filings(limit=10):
    request = urllib.request.Request(
        SEC_URL,
        headers=HEADERS
    )

    with urllib.request.urlopen(request) as response:
        data = json.load(response)

    recent = data["filings"]["recent"]

    filings = []

    for i in range(min(limit, len(recent["form"]))):
        filings.append({
            "company": "NVIDIA",
            "cik": "0001045810",
            "form": recent["form"][i],
            "filed_at": recent["filingDate"][i],
            "accession_number": recent["accessionNumber"][i],
            "primary_document": recent["primaryDocument"][i],
        })

    return filings


if __name__ == "__main__":
    filings = fetch_nvidia_filings()

    for filing in filings:
        print(filing)
