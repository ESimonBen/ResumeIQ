# transformer.py

def transform_job(raw_job):
    job = raw_job["MatchedObjectDescriptor"]

    return {
        "id": job["PositionID"],
        "title": job["PositionTitle"],
        "company": job["OrganizationName"],
        "location": job["PositionLocationDisplay"],
        "description": job.get("UserArea", {}).get("Details", {}).get("JobSummary", ""),
        "source": "USAJobs",
        "date_posted": job.get("PublicationStartDate")
    }