from uuid import UUID
from abc import ABC, abstractmethod
from fastapi.responses import FileResponse


class IDownloadService(ABC):
    
    @abstractmethod
    async def download(self, file_id: UUID) -> FileResponse | None:
        raise NotImplementedError