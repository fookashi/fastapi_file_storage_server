from uuid import UUID
import pathlib 

from fastapi import UploadFile
from interfaces import IUploadService
from db.sqlite_repo import SQLiteFileRepository

class UploadService(IUploadService):
    
    async def upload(self, name: str, file_id: UUID, file: UploadFile) -> None:
        suffixes = ''.join(pathlib.Path(file.filename).suffixes)
        with open(f'storaged_files/{file_id.hex}{suffixes}', 'wb') as upload_file:
            while block := await file.read(10 * 1024):
                upload_file.write(block)
        async with SQLiteFileRepository() as repo:
            await repo.create(id=file_id, name=f'{name}{suffixes}')