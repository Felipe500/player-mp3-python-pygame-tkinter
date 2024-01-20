import audioread
from pygame import mixer, mixer_music
from os.path import join, basename

from glob import glob
from os import curdir, path
from sys import platform

from .var_player import  VariablesPlayer


class Player(VariablesPlayer):
    def __init__(self, **play_data):
        super().__init__()

    def get_pasta_padrao(self):
        return join(path.expanduser('~'), 'Música' if platform in 'linux' else 'Music')

    def buscar_arquivos_mp3(self, nova_pasta: str = None):
        if len(self.playlist) > 0:
            self.playlist.clear()

        self.pasta_musicas = nova_pasta if nova_pasta else self.get_pasta_padrao()

        try:
            for musica in glob(join(curdir, self.pasta_musicas, '*.mp3')):
                self.count_musicas += 1
                self.playlist.append(musica)
                print(self.count_musicas, '°', basename(musica[:-4]).replace('_', ' '))

        except Exception as r:
            print(f"O player não encontrou musicas na pasta selecionada!...\n {r}")

        if nova_pasta:
            mixer_music.stop()
            mixer_music.unload()

    def mixer_pre_init(self):
        print("bem-vindo ao Music x....")
        mixer.pre_init(frequency=self.frequencia_som, size=-16, channels=2, buffer=5996)
        mixer.init()

    def iniciar(self):
        self.mixer_pre_init()
        self.tocando = mixer_music.get_busy()
        total_musicas = len(self.playlist)

        if not self.tocando and total_musicas > 0:
            self.play_music(self.playlist[self.musica_rodando])

    def encerrar_mixer_audio(self):
        self.encerrar = True
        mixer_music.stop()
        mixer.quit()
        print("Encerrando music_x player.....")

    def pause_continue(self):
        self.tocando = mixer_music.get_busy()

        if self.get_pos_music() < 0 < len(self.playlist):
            mixer_music.play()

        if not self.tocando and len(self.playlist) > 0:
            self.tocando = True
            mixer_music.unpause()
            return 'Pausar'

        elif len(self.playlist) > 0:
            mixer_music.pause()
            self.tocando = False
            return 'Continuar'

    def reinicio(self):
        mixer_music.rewind()

    def set_volume(self, volume):
        self.volume = volume
        mixer_music.set_volume(self.volume)
        return self.volume

    def play_music(self, music: str, pos: float = 0.0):
        mixer_music.load(music)
        mixer_music.set_volume(self.volume)
        mixer_music.play(start=pos)
        self.tocando = True
        self.data_musica = self.get_music_infor(music)

    def avancar_musica(self):
        if len(self.playlist) > 0:
            if self.musica_rodando + 1 >= len(self.playlist):
                mixer_music.stop()
                self.musica_rodando = 0
                self.play_music(self.playlist[self.musica_rodando])

            else:
                mixer_music.stop()
                self.musica_rodando = self.musica_rodando + 1
                self.play_music(self.playlist[self.musica_rodando])

    def voltar_musica(self):
        if len(self.playlist) > 0:
            if self.musica_rodando <= 0:
                mixer_music.stop()
                total_musicas = len(self.playlist)
                self.musica_rodando = total_musicas - 1
                self.play_music(self.playlist[self.musica_rodando])
            else:
                mixer_music.stop()
                self.musica_rodando = self.musica_rodando - 1
                self.play_music(self.playlist[self.musica_rodando])

    def get_pos_music(self):
        if self.pos_music == 0:
            self.pos_music = mixer_music.get_pos() / 1000
        return mixer_music.get_pos() / 1000

    def set_pos_music(self, value: float):
        mixer_music.set_pos(value)

    def get_duration_music(self, set_music_started: str, duration_music: int = 0):
        with audioread.audio_open(set_music_started) as f:
            duration_music = f.duration
            self.duration_music = f.duration
        return duration_music

    def get_music_infor(self, music):
        return {
            'nome': basename(music[:-4]).replace('_', ' '),
            'status': self.tocando,
            'duration': self.get_duration_music(music)
        }
