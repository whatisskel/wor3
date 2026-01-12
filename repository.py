
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def list_all(self):
        pass

    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def remove(self, obj_id):
        pass
