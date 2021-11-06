

class Player(object):
    def __init__(self):
        self.frequencia_som = 44100
        self.playlist = []
        self.tocar = True
        self.volume = 0.4000000
        # numero da lista de directorio
        self.rodando = 0
        # contador de musicas
        self.mm = 0
        self.nmusicas = 0
        # plataformas
        self.windows = "Sistema Operacional: windows"
        self.Linux = "Sistema Operacional: Linux"
        # veja qual o sistema operacional que você esta utilizando e coloque o diretorio de suas músicas aqui
        self.pasta_linux = "/media/the_felipe/Arquivos2/musicas/"
        self.pasta_windows = "D:/musicas"


