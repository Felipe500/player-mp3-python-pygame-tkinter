
class VariablesPlayer(object):
    def __init__(self):
        self.frequencia_som = 44100
        self.playlist = []
        self.volume = 0.5
        self.tocando = False
        self.encerrar = False
        # numero da lista de directorio
        self.rodando = 0
        # contador de musicas
        self.mm = 0
        self.nmusicas = 0
        # progress
        self.bar_progress_value = 0
        self.pos_music = 0
        self.duration_music = 0
        # plataformas
        self.windows = "Sistema Operacional: windows"
        self.Linux = "Sistema Operacional: Linux"
        # veja qual o sistema operacional que você esta utilizando e coloque o diretorio de suas músicas aqui
        self.pasta_linux = "/home/felipe-brx/Música"
        self.pasta_windows = "D:/musicas"
