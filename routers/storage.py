from uuid import uuid4, UUID
from typing import Optional

from fastapi import APIRouter, status, UploadFile, File, Depends
from fastapi.background import BackgroundTasks
from fastapi.responses import FileResponse

from schemas.file_storage import FileStorageResponse
from services import DownloadService, UploadService


storage_router = APIRouter(prefix='/storage')


@storage_router.post(
    '/upload',
    tags=["upload"],
    summary="Perform a file upload operation",
    status_code=status.HTTP_200_OK,
    response_model=FileStorageResponse,
)
async def upload(name: Optional[str] = None,
                 file: UploadFile = File(),
                 upload_service: UploadService = Depends(UploadService),
                 background_tasks: BackgroundTasks = BackgroundTasks()
                ) -> FileStorageResponse:
    file_id = uuid4()
    if name is None:
        name = file_id.hex
    background_tasks.add_task(upload_service.upload, name, file_id, file)
    return FileStorageResponse(file_id=file_id, name=name)


@storage_router.get(
    '/download/{file_id}',
    tags=["download"],
    summary="Perform a file download operation",
    response_class=FileResponse,
    status_code=status.HTTP_202_ACCEPTED
)
async def download(file_id: UUID,
                   download_service: DownloadService = Depends(DownloadService)
                   ) -> FileStorageResponse:
    return await download_service.download(file_id)
