from abc import ABC, abstractmethod
from fastapi import UploadFile

class IUploadService(ABC):
    
    @abstractmethod
    async def upload_file(self, file: UploadFile) -> None:
        raise NotImplementedError