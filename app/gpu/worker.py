from datetime import datetime, timezone


class GPUWorker:

    def __init__(self):

        self.status_value = "idle"

        self.current_job = None

    def status(self):

        return {
            "status": self.status_value,
            "current_job": self.current_job
        }

    def start_job(self, job_id):

        self.status_value = "running"

        self.current_job = {
            "id": job_id,
            "started_at": datetime.now(
                timezone.utc
            ).isoformat()
        }

        return self.status()

    def stop_job(self):

        self.status_value = "idle"

        self.current_job = None

        return self.status()


gpu_worker = GPUWorker()
