import argparse
from fetcher import fetch_papers, save_to_csv

def main():
    parser = argparse.ArgumentParser(description='Fetch research papers from PubMed.')
    parser.add_argument('query', type=str, help='Search query for PubMed')
    parser.add_argument('-o', '--output', type=str, default="pubmed_results.csv", help='Output CSV filename')
    parser.add_argument('-n', '--num', type=int, default=10, help='Number of results to fetch')

    args = parser.parse_args()

    print(f"🔍 Fetching {args.num} papers for query: {args.query}")
    papers = fetch_papers(args.query, args.num)

    if papers:
        print("📄 Papers Fetched:", papers)  
        save_to_csv(papers, args.output)
    else:
        print("⚠️ No papers found for the query.")

if __name__ == '__main__':
    main()
