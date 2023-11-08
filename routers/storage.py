from uuid import uuid4
from typing import Optional

from fastapi import APIRouter, status, UploadFile, Depends
from fastapi.background import BackgroundTasks

from schemas.file_storage import FileStorageResponse
from services.upload_service import UploadService


storage_router = APIRouter('/storage')


@storage_router.post(
    '/upload',
    tags=["upload"],
    summary="Perform a storage upload operation",
    status_code=status.HTTP_200_OK,
    response_model=FileStorageResponse,
)
async def get_health(name: Optional[str] = None,
                     file: UploadFile = None,
                     upload_service: UploadService = Depends(UploadService),
                     background_tasks: BackgroundTasks
                     ) -> FileStorageResponse:
    file_id = uuid4()
    if name is None:
        name = file_id.hex
    background_tasks.add_task(upload_service.upload_file(file_id, file)
    return FileStorageResponse(file_id, name)


# @storage_router.get(
#     tags=["download"],
#     summary="Perform a Health Check",
#     response_description="Return HTTP Status Code 200 (OK)",
#     status_code=status.HTTP_200_OK,
#     response_model=FileStorageResponse,
# )
# async def get_health() -> FileStorageResponse:
#     return FileStorageResponse(status="OK")
