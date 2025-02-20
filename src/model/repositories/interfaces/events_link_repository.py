from abc import ABC, abstractmethod
from src.model.entities.events_link import EventosLink


class EventosLinkRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, event_id: int, subscriber_id: int) -> str: pass

    @abstractmethod
    def select_eventsw_link(self, event_id: int, subscriber_id: int) -> EventosLink: pass
