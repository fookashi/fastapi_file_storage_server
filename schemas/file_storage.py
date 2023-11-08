from uuid import UUID

from pydantic import BaseModel
from typing import Literal


class FileStorageResponse(BaseModel):
    file_id: UUID
    name: str