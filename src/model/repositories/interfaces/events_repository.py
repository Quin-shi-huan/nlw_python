from abc import ABC, abstractmethod
from src.model.entities.events import Eventos


class EventosRepositoryInterface(ABC):
    
    @abstractmethod
    def insert(self, event_name: str) -> None: pass

    @abstractmethod
    def select_event(self, event_name: str) -> Eventos: pass
