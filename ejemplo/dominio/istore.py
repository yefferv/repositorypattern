import abc

class IStore(abc.ABC):

    @abc.abstractmethod
    def add(self,obj):
        pass

    @abc.abstractmethod
    def query_all(self, obj):
        pass
