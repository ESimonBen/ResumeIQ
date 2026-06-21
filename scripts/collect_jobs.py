# collect_jobs.py
from usajobs_client import fetch_jobs

def main():
    data = fetch_jobs(keyword="software engineer")

    jobs = data["SearchResult"]["SearchResultItems"]

    print(f"Found {len(jobs)} jobs:\n")

    for job in jobs:
        position = job["MatchedObjectDescriptor"]

        print(position["PositionTitle"])
        print(position["OrganizationName"])
        print(position["PositionLocationDisplay"])
        print("-" * 40)

if __name__ == "__main__":
    main()