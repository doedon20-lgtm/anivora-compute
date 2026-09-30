from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.gpu.manager import gpu_manager
from app.gpu.worker import gpu_worker
from app.jobs.manager import job_manager
from app.storage.manager import storage_manager


router = APIRouter(
    prefix="/v1"
)


class CreateJobRequest(BaseModel):

    type: str

    command: str


@router.get("/status")
def status():

    return {
        "success": True,
        "service": "AniVora Compute",
        "status": "online"
    }


@router.get("/gpu")
def gpu_status():

    return {
        "success": True,
        "gpu": gpu_manager.status()
    }


@router.get("/worker")
def worker_status():

    return {
        "success": True,
        "worker": gpu_worker.status()
    }


@router.post("/jobs")
def create_job(
    request: CreateJobRequest
):

    if not request.type.strip():

        raise HTTPException(
            status_code=400,
            detail="Job type cannot be empty"
        )

    if not request.command.strip():

        raise HTTPException(
            status_code=400,
            detail="Command cannot be empty"
        )

    job = job_manager.create_job(
        request.type,
        request.command
    )

    return {
        "success": True,
        "job": job
    }


@router.get("/jobs")
def list_jobs():

    return {
        "success": True,
        "jobs": job_manager.list_jobs()
    }


@router.get("/jobs/{job_id}")
def get_job(job_id: str):

    job = job_manager.get_job(
        job_id
    )

    if not job:

        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return {
        "success": True,
        "job": job
    }


@router.post("/jobs/{job_id}/start")
def start_job(job_id: str):

    job = job_manager.update_status(
        job_id,
        "running"
    )

    if not job:

        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    worker = gpu_worker.start_job(
        job_id
    )

    return {
        "success": True,
        "job": job,
        "worker": worker
    }


@router.post("/jobs/{job_id}/stop")
def stop_job(job_id: str):

    job = job_manager.update_status(
        job_id,
        "stopped"
    )

    if not job:

        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    worker = gpu_worker.stop_job()

    return {
        "success": True,
        "job": job,
        "worker": worker
    }


@router.delete("/jobs/{job_id}")
def delete_job(job_id: str):

    deleted = job_manager.delete_job(
        job_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return {
        "success": True,
        "deleted": True
    }


@router.get("/storage")
def storage_status():

    return {
        "success": True,
        "storage": storage_manager.status()
    }
