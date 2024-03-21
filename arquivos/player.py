from typing import Dict

from glob import glob
from os import curdir
from os.path import join, basename, expanduser
from sys import platform

from mutagen.mp3 import MP3

from pygame import mixer, mixer_music


class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Player(metaclass=Singleton):
    def __init__(self, **play_data):
        self.frequencia_som = 44100
        self.playlist_listbox = []
        self.volume = 0.5
        self.tocando = False
        self.encerrar = False

        self.playlist = {
            'musicas': [],
            'path': [],
            'em_reproducao': 0,
            'total_musicas': 0
        }
        self.data_musica = {
            'nome': '',
            'status': self.tocando,
            'duration': 0
        }
        # progress
        self.bar_progress_value = 0
        self.pos_music = 0
        self.duration_music = 0
        self.buscar_arquivos_mp3()
        self.iniciar()

    @property
    def get_playlist(self):
        return self.playlist['musicas'] or []

    def get_pasta_padrao(self):
        return join(expanduser('~'), 'Música' if platform in 'linux' else 'Music')

    def buscar_arquivos_mp3(self, nova_pasta: str = None):
        if self.playlist['total_musicas'] > 0:
            self.playlist['musicas'].clear()
            self.playlist['path'].clear()
            self.playlist['total_musicas'] = 0
            self.playlist_listbox.clear()

        pasta_playlist = nova_pasta if nova_pasta else self.get_pasta_padrao()

        try:
            for total_musicas, musica in enumerate(glob(join(curdir, pasta_playlist, '*.mp3'))):
                self.playlist_listbox.append(f" {total_musicas + 1}° {basename(musica[:-4]).replace('_', ' ')}")
                self.playlist.update(
                    musicas=self.playlist['musicas'] + [basename(musica[:-4]).replace('_', ' ')],
                    path=self.playlist['path'] + [musica],
                    total_musicas=total_musicas + 1,
                )
                print(total_musicas + 1, '°', basename(musica[:-4]).replace('_', ' '))

        except Exception as r:
            print(f"O player não encontrou musicas na pasta selecionada!...\n {r}")

        if nova_pasta:
            mixer_music.stop()
            mixer_music.unload()

    def mixer_pre_init(self):
        if not mixer.get_init():
            mixer.pre_init(frequency=self.frequencia_som, size=-16, channels=2, buffer=5996)
            mixer.init()
            print("bem-vindo ao Music x....")

    def iniciar(self):
        self.mixer_pre_init()
        self.tocando = mixer_music.get_busy()
        self.musica_rodando = 0

        if not self.tocando and self.playlist['total_musicas'] > 0:
            self.play_music(self.playlist['path'], self.musica_rodando)

    def encerrar_mixer_audio(self):
        self.encerrar = True
        mixer_music.stop()
        mixer.quit()
        print("Encerrando music_x player.....")

    def pause_continue(self):
        self.tocando = mixer_music.get_busy()

        if self.get_pos_music() < 0 < self.playlist['total_musicas']:
            mixer_music.play()

        if not self.tocando and self.playlist['total_musicas'] > 0:
            self.tocando = True
            mixer_music.unpause()
            return 'Pausar'

        elif self.playlist['total_musicas'] > 0:
            mixer_music.pause()
            self.tocando = False
            return 'Continuar'

    def reinicio(self):
        mixer_music.rewind()

    def set_volume(self, volume):
        self.volume = volume
        mixer_music.set_volume(self.volume)
        return self.volume

    def play_music(self, playlist_path: list, reproduzir: int, pos: float = 0.0):
        mixer_music.load(playlist_path[reproduzir])
        mixer_music.set_volume(self.volume)
        mixer_music.play(start=pos)
        self.tocando = True
        self.playlist['em_reproducao'] = reproduzir
        self.data_musica = self.get_music_infor(playlist_path[reproduzir])

    def avancar_musica(self):
        if self.playlist['total_musicas'] > 0:
            if self.musica_rodando + 1 >= self.playlist['total_musicas']:
                mixer_music.stop()
                self.musica_rodando = 0
                self.play_music(self.playlist['path'], self.musica_rodando)

            else:
                mixer_music.stop()
                self.musica_rodando = self.musica_rodando + 1
                self.play_music(self.playlist['path'], self.musica_rodando)

    def voltar_musica(self):
        if self.playlist['total_musicas'] > 0:
            if self.musica_rodando <= 0:

                mixer_music.stop()
                self.musica_rodando = self.playlist['total_musicas'] - 1
                self.play_music(self.playlist['path'], self.musica_rodando)
            else:
                mixer_music.stop()
                self.musica_rodando = self.musica_rodando - 1
                self.play_music(self.playlist['path'], self.musica_rodando)

    def get_pos_music(self):
        if self.pos_music == 0:
            self.pos_music = mixer_music.get_pos() / 1000
        return mixer_music.get_pos() / 1000

    def set_pos_music(self, value: float):
        mixer_music.set_pos(value)

    def get_duration_music(self, set_music_started: str, duration_music: int = 0):
        duration_music = MP3(set_music_started).info.length
        return duration_music

    def get_music_infor(self, musica):
        return {
            'nome': basename(musica[:-4]).replace('_', ' '),
            'status': self.tocando,
            'duration': self.get_duration_music(musica)
        }
