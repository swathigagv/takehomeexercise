import requests
import pandas as pd
from typing import List, Dict, Optional

def fetch_papers(query: str) -> List[Dict[str, Optional[str]]]:
    # Construct the API URL
    url = f"https://pubmed.ncbi.nlm.nih.gov/api/query?query={query}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses

    # Process the response (this is a placeholder, actual parsing needed)
    papers = []  # This should be populated with actual data from the response
    return papers

def filter_papers(papers: List[Dict[str, Optional[str]]]) -> List[Dict[str, Optional[str]]]:
    # Filter papers based on author affiliations
    filtered_papers = []
    for paper in papers:
        # Logic to identify non-academic authors and company affiliations
        # Placeholder logic
        if paper.get('author_affiliation') and 'pharmaceutical' in paper['author_affiliation']:
            filtered_papers.append(paper)
    return filtered_papers

def save_to_csv(papers: List[Dict[str, Optional[str]]], filename: str) -> None:
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
