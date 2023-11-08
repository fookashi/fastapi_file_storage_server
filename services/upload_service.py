import os
from uuid import UUID

from fastapi import UploadFile
from interfaces.upload_service import IUploadService


class UploadService(IUploadService):
    
    async def upload_file(self, file_id: str, file: UploadFile) -> None:
        with open(f'storaged_files/{file_id.hex}', 'wb') as upload_file:
            while block := await file.read(10 * 1024):
                upload_file.write(block)
        