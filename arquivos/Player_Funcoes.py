from pygame import mixer, mixer_music
from os.path import join, basename
from arquivos.classe_player import *
from glob import glob
from os import curdir
from sys import platform
import audioread

Player_Musica = Player()


class Funcoes_Player(Player):
    bar_progress_value = 1
    duration_music = 1
    pos_music = 0

    def __init__(self):
        super().__init__()
        self.tocando = None

    def buscar_arquivos_mp3(self):
        #verificar se a lista já possui musicas
        # caso sim, a lista será limpada
        if len(Player_Musica.playlist) > 0:
            Player_Musica.playlist.clear()
            print('limpando lista')
        #verificando qual o sistema operacional está em uso
        if 'linux' in platform:
            print(Player_Musica.Linux)
            try:
                Player_Musica.nmusicas = 0
                for musica in glob(join(curdir, Player_Musica.pasta_linux, '*.mp3')):
                    # contar numero de musicas
                    Player_Musica.nmusicas = Player_Musica.nmusicas + 1
                    # nome da musica
                    print(Player_Musica.nmusicas, '°', basename(musica[:-4]).replace('_', ' '))
                    # exibir caminhos de musicas
                    # adicionar a lista de reprodrução
                    Player_Musica.playlist.append(musica)
            except:
                print("O player não encontrou musicas na pasta selecionada!...")

            print("player de musica inicializou...")
        # verificando qual o sistema operacional está em uso
        if 'win' in platform:
            print(Player_Musica.windows)
            try:
                Player_Musica.nmusicas = 0
                for musica in glob(join(curdir, Player_Musica.pasta_windows, '*.mp3')):
                    # contar numero de musicas
                    Player_Musica.nmusicas = Player_Musica.nmusicas + 1
                    # nome da musica
                    print(Player_Musica.nmusicas, '°', basename(musica[:-4]).replace('_', ' '))
                    # adicionar a lista de reprodrução
                    Player_Musica.Player_Musica.append(musica)

            except:
                print("O player não encontrou musicas na pasta selecionada!...")

        print("player de musica inicializou...")

    def mixer_pre_init(self):
        print("bem-vindo ao Music x....")
        mixer.pre_init(frequency=Player_Musica.frequencia_som, size=-16, channels=2, buffer=5996)
        mixer.init()

    def iniciar(self):
        self.mixer_pre_init()
        self.tocando = mixer_music.get_busy()

        if not self.tocando:
            self.play_music(Player_Musica.playlist[Player_Musica.rodando])

    def encerrar_mixer_audio(self):
        mixer_music.stop()
        mixer.quit()
        print("Encerrando music_x player.....")

    def pause_continue(self):
        self.tocando = mixer_music.get_busy()

        if self.get_pos_music() < 0:
            mixer_music.play()

        if not self.tocando:
            self.tocando = True
            mixer_music.unpause()
            return 'Pausar'

        else:
            mixer_music.pause()
            self.tocando = False
            return 'Reproduzir'

    def reinicio(self):
        mixer_music.rewind()

    def set_volume(self, volume):
        self.volume = volume
        mixer_music.set_volume(self.volume)
        return self.volume

    def play_music(self, music: str, pos: float = 0.0):
        mixer_music.load(music)
        mixer_music.set_volume(Player_Musica.volume)
        mixer_music.play(start=pos)
        self.get_duration_music(music)
        self.tocando = True

    def avancar_musica(self):
        if Player_Musica.rodando + 1 >= len(Player_Musica.playlist):
            mixer_music.stop()
            Player_Musica.rodando = 0
            self.play_music(Player_Musica.playlist[Player_Musica.rodando])

        else:
            mixer_music.stop()
            Player_Musica.rodando = Player_Musica.rodando + 1
            self.play_music(Player_Musica.playlist[Player_Musica.rodando])

    def voltar_musica(self):
        if Player_Musica.rodando <= 0:
            mixer_music.stop()
            total_musicas = len(Player_Musica.playlist)
            Player_Musica.rodando = total_musicas - 1
            self.play_music(Player_Musica.playlist[Player_Musica.rodando])
        else:
            mixer_music.stop()
            Player_Musica.rodando = Player_Musica.rodando - 1
            self.play_music(Player_Musica.playlist[Player_Musica.rodando])

    def get_pos_music(self):
        if self.pos_music == 0:
            self.pos_music = mixer_music.get_pos() / 1000
        return mixer_music.get_pos() / 1000

    def set_pos_music(self, value: float):
        self.play_music(Player_Musica.playlist[Player_Musica.rodando], float(value))

    def get_duration_music(self, set_music_started: str):
        with audioread.audio_open(set_music_started) as f:
            self.duration_music = f.duration
        return self.duration_music
