from uuid import UUID
import pathlib
import os, fnmatch

from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException
from interfaces import IDownloadService
from db.sqlite_repo import SQLiteFileRepository

class DownloadService(IDownloadService):

    def find(self, pattern, path):
        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        return result
    
    async def download(self, file_id: UUID) -> FileResponse | None:
        async with SQLiteFileRepository() as repo:
            info = await repo.read(id=file_id)
        path=self.find(f"{file_id.hex}*", f"{os.getcwd()}/storaged_files")
        if not(path and info):
            raise HTTPException(status_code=404, detail='Файл не найден на сервере!')
        match info[1]:
            case 'uploading':
                raise HTTPException(status_code=400, detail='Файл еще не загружен на сервер!')
            case 'failed':
                raise HTTPException(status_code=400, detail='Произошла ошибка при загрузке файла, попробуйте загрузить еще раз!')
        path = path[0]
        name = info[0]
        suffixes = ''.join(pathlib.Path(path).suffixes)
        return FileResponse(path, media_type='application/octet-stream', filename=f'{name}{suffixes}')
            
