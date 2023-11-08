from uuid import uuid4
from typing import Optional

from fastapi import APIRouter, status, UploadFile
from schemas.file_storage import FileStorageResponse

storage_router = APIRouter('/storage')


@storage_router.post(
    '/upload',
    tags=["upload"],
    summary="Perform a Health Check",
    response_description="Return 200 if file is in uploading queue",
    status_code=status.HTTP_200_OK,
    response_model=FileStorageResponse,
)
async def get_health(name: Optional[str] = None,
                     file: UploadFile = None,
                     ) -> FileStorageResponse:
    file_id = uuid4()
    if name is None:
        name = file_id.hex
    
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
