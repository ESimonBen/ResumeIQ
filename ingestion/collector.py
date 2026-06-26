# collector.py

class JobCollector:

    def __init__(self, sources):
        self.sources = sources
        self.seen_ids = set()

    def collect(self, keywords, max_pages=5):

        all_jobs = []

        for source in self.sources:
            jobs = source.fetch(keywords, max_pages)

            for job in jobs:
                if job["id"] not in self.seen_ids:
                    self.seen_ids.add(job["id"])
                    all_jobs.append(job)

        return all_jobs