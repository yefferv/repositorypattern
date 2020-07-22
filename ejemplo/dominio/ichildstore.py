import abc

class IChildStore(abc.ABC):

    @abc.abstractmethod
    def add_one(self,obj):
        pass

    @abc.abstractmethod
    def get_all(self, obj):
        pass
