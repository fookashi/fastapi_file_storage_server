from uuid import UUID

from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException
from interfaces import IDownloadService
from db.sqlite_repo import SQLiteFileRepository

class DownloadService(IDownloadService):
    
    async def download(self, file_id: UUID) -> FileResponse | None:
        
        try:
            file = open(f'storaged_files/{file_id.hex}.html', 'rb')
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail='File not found')
        else:
            file.close()
        async with SQLiteFileRepository() as repo:
            name = await repo.read(file_id)
            print(name)
        return FileResponse(f'storaged_files/{file_id.hex}.html', media_type='application/octet-stream', filename=f'{name}')
            
