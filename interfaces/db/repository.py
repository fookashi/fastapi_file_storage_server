from abc import ABC, abstractmethod
from uuid import UUID


class IRepository(ABC):
    
    
    @abstractmethod
    def create(self, name: str, id: UUID) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def read(self, id: UUID) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def update(self, id: UUID, new_name: str) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, id: UUID) -> str:
        raise NotImplementedError


    