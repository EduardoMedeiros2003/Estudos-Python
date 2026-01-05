class Musica:
    musicas= []
    def __init__(self,nome,artista,duracao):
        self.nome = nome
        self.artista= artista
        self.duracao = duracao
        Musica.musicas.append(self)
        

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def mostrar_musica():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')
    

musica_planos=Musica('Planos', 'BK', 216)
musica_folhas=Musica('Folhas', 'BK', 322)

Musica.mostrar_musica()