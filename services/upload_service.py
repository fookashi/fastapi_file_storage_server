from uuid import UUID
import pathlib 

import aiofiles
from fastapi.exceptions import HTTPException

from fastapi import UploadFile
from interfaces import IUploadService
from db.sqlite_repo import SQLiteFileRepository
import os

class UploadService(IUploadService):
    
    async def upload(self, name: str, file_id: UUID, file: UploadFile) -> None:
        
        name = file.headers.get('name')
        suffixes = ''.join(pathlib.Path(name).suffixes)
        async with SQLiteFileRepository() as repo:
            await repo.create(id=file_id, name=f'{name}{suffixes}')
        try:
            async with aiofiles.open(f'storaged_files/{file_id.hex}{suffixes}', 'wb') as upload_file:    
                async for chunk in file.stream():
                    await upload_file.write(chunk)
        except:
            async with SQLiteFileRepository() as repo:
                await repo.delete(id=file_id)
            os.remove(f'storaged_files/{file_id.hex}{suffixes}')
            raise HTTPException(400, "Произошла ошибка во время загрузки файла!")
        
        async with SQLiteFileRepository() as repo:
            await repo.update(id=file_id, new_status='uploaded')
            