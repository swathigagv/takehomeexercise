import argparse
from fetcher import fetch_papers, filter_papers, save_to_csv

def main():
    parser = argparse.ArgumentParser(description='Fetch research papers from PubMed.')
    parser.add_argument('query', type=str, help='Search query for PubMed')
    parser.add_argument('-f', '--file', type=str, help='Output filename for CSV')
    args = parser.parse_args()

    papers = fetch_papers(args.query)
    filtered_papers = filter_papers(papers)

    if args.file:
        save_to_csv(filtered_papers, args.file)
    else:
        print(filtered_papers)

if __name__ == '__main__':
    main()
