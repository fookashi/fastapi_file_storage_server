from uuid import UUID

from abc import ABC, abstractmethod
from fastapi import UploadFile


class IUploadService(ABC):
    
    @abstractmethod
    async def upload_file(self, file_id: UUID, file: UploadFile) -> None:
        raise NotImplementedError