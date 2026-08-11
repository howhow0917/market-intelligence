FORM_EVENT_TYPES = {
    "8-K": "material_corporate_event",
    "10-K": "annual_report",
    "10-Q": "quarterly_report",
    "20-F": "annual_report",
    "6-K": "foreign_company_report",
    "3": "insider_transaction",
    "4": "insider_transaction",
    "5": "insider_transaction",
    "SCHEDULE 13D": "major_shareholder_change",
    "SCHEDULE 13G": "major_shareholder_change",
}


def normalize_sec_filing(filing):
    form = filing["form"]

    return {
        "company": filing["company"],
        "source": "SEC",
        "source_type": "regulatory_filing",
        "event_type": FORM_EVENT_TYPES.get(form, "other_filing"),
        "form": form,
        "published_at": filing["filed_at"],
        "accession_number": filing["accession_number"],
        "primary_document": filing["primary_document"],
    }


if __name__ == "__main__":
    test_filing = {
        "company": "NVIDIA",
        "form": "8-K",
        "filed_at": "2026-07-02",
        "accession_number": "0001045810-26-000060",
        "primary_document": "nvda-20260628.htm",
    }

    event = normalize_sec_filing(test_filing)

    print(event)
