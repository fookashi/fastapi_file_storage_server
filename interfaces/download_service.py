from uuid import UUID
from abc import ABC, abstractmethod
from fastapi.responses import FileResponse


class IUploadService(ABC):
    
    @abstractmethod
    async def download_file(self, file_id: UUID) -> FileResponse | str:
        raise NotImplementedError