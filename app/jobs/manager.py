import secrets
from datetime import datetime, timezone


class JobManager:

    def __init__(self):

        self.jobs = {}

    def create_job(
        self,
        job_type: str,
        command: str
    ):

        job_id = (
            "job_"
            + secrets.token_hex(8)
        )

        job = {
            "id": job_id,
            "type": job_type,
            "command": command,
            "status": "queued",
            "created_at": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.jobs[job_id] = job

        return job

    def list_jobs(self):

        return list(
            self.jobs.values()
        )

    def get_job(self, job_id):

        return self.jobs.get(
            job_id
        )

    def update_status(
        self,
        job_id,
        status
    ):

        job = self.get_job(
            job_id
        )

        if not job:
            return None

        job["status"] = status

        return job

    def delete_job(self, job_id):

        if job_id not in self.jobs:
            return False

        del self.jobs[job_id]

        return True


job_manager = JobManager()
