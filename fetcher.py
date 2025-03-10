import requests
import pandas as pd
from typing import List, Dict, Optional

# Correct PubMed API URLs
SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_papers(query: str, max_results: int = 10) -> List[Dict[str, Optional[str]]]:
    """Fetch PubMed papers based on a query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(SEARCH_URL, params=params)
    print("🔍 API Response Status Code:", response.status_code)
    print("🔍 API Response Content:", response.text)
    #response.raise_for_status()
    if response.status_code != 200:
        print("⚠️ Error fetching papers!")
        return []

    paper_ids = response.json().get("esearchresult", {}).get("idlist", [])
    
    if not paper_ids:
        print("⚠️ No papers found!")
        return []

    return fetch_paper_details(paper_ids)
    
    #paper_ids = response.json()["esearchresult"]["idlist"]
    #return fetch_paper_details(paper_ids)

def fetch_paper_details(paper_ids: List[str]) -> List[Dict[str, Optional[str]]]:
    """Fetch details for a list of PubMed IDs."""
    if not paper_ids:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    response = requests.get(SUMMARY_URL, params=params)
    response.raise_for_status()

    results = response.json()["result"]
    papers = []
    
    for paper_id in paper_ids:
        paper = results.get(paper_id, {})
        papers.append({
            "PubmedID": paper_id,
            "Title": paper.get("title", "N/A"),
            "Publication Date": paper.get("pubdate", "N/A"),
            "Non-academic Author(s)": "N/A",  # Need NLP for real filtering
            "Company Affiliation(s)": "N/A",  # Needs additional processing
            "Corresponding Author Email": "N/A"  # Email not available in this API
        })

    return papers

def save_to_csv(papers: List[Dict[str, Optional[str]]], filename: str) -> None:
    """Save paper data to a CSV file."""
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
    print(f"✅ Results saved to {filename}")
