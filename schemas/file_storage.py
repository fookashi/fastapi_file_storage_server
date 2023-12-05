from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class FileStorageResponse(BaseModel):
    file_id: UUID