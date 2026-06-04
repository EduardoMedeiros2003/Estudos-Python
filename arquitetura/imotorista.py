from abc import ABC, abstractmethod

class IMotorista(ABC):
    @abstractmethod
    def aceitar_corrida(self, destino: str) -> None:
        pass

class ICaronaCompartilhada(ABC):
    @abstractmethod
    def aceitar_carona_compartilhada(self, destino: str, passageiros: list) -> None:
        pass

class ICarga(ABC):
    @abstractmethod
    def transportar_carga(self, peso: float) -> None:
        pass

#Conferir como q vai funcionar aqui

class MotoristaComum(IMotorista):
    def aceitar_corrida(self, destino: str)-> None:
        print(f'Corrida aceita, para: {destino}')

class MotoristaCarona(ICaronaCompartilhada):
    def aceitar_carona_compartilhada(self, destino: str)-> None:
        print(f'Carona compartilahda aceita, para: {destino}')

class IMotoristacarga(ICarga):
    def transportar_carga(self, peso: float)->None:
        print(f'Trasporte de carga aceita, de peso: {peso}')


motorista = MotoristaComum()
motorista.aceitar_corrida("Recife")
motorista2 = MotoristaCarona()
motorista2.aceitar_carona_compartilhada('Caruaru')
motorista3 = IMotoristacarga()
motorista3.transportar_carga(34245)
