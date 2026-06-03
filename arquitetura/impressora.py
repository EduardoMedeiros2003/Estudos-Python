from abc import ABC, abstractmethod

class InterfaceImpressora(ABC):
    @abstractmethod
    def imprimir(self, documento: str):
        pass

class InterfaceScanner(ABC):
    @abstractmethod
    def digitalizar(self, documento: str):
        pass
    
class InterfaceFax(ABC):
    @abstractmethod
    def enviar_fax(self, numero: str, documento: str):
        pass

class ImpressoraAntiga(ABC):
    def imprimir(self, documento: str):
        print(f'Imprimindo: {documento}')

class ImpressoraMultifuncional(InterfaceImpressora, InterfaceScanner, InterfaceFax):
    def imprimir(self, documento: str):
        print(f"Imprimindo: {documento}")

    def digitalizar(self, documento: str):
        print(f'Digitando: {documento}')

    def enviar_fax(self, numero: str, documento: str):
        print(f'Enviando fax para: {numero} : {documento}')

muilt = ImpressoraMultifuncional()

muilt.imprimir('Contatos.pdf')
muilt.digitalizar('Documentos.pdf')
muilt.enviar_fax('81923442', 'Contatos.pdf')