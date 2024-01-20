
class VariablesPlayer(object):
    def __init__(self):
        self.frequencia_som = 44100
        self.playlist = []
        self.volume = 0.5
        self.tocando = False
        self.encerrar = False
        self.musica_rodando = 0
        self.count_musicas = 0

        self.data_musica = {
            'nome': '',
            'status': self.tocando,
            'duration': 0
        }

        # progress
        self.bar_progress_value = 0
        self.pos_music = 0
        self.duration_music = 0
        # plataformas
        self.pasta_musicas = "pasta_musicas"
