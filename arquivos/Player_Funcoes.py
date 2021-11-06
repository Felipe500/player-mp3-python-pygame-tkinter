from pygame import mixer, mixer_music
from os.path import dirname, join, basename
from arquivos.classe_player import *
from glob import glob
from os import curdir
from sys import platform

Player_Musica = Player()
class Funcoes_Player(object):

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


    def inicio(self):
        print("bem-vindo ao Music x....")
        mixer.pre_init(frequency=Player_Musica.frequencia_som, size=-16, channels=2, buffer=5996)
        mixer.init()


    def iniciar(self):
        tocando = mixer_music.get_busy()
        if tocando == False:
            x = mixer_music.get_busy()
            musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
            mixer_music.set_volume(Player_Musica.volume)
            mixer_music.play()

        else:
            print("já inicializado")
        print("frequênci atual:  ", Player_Musica.frequencia_som)
        print(Player_Musica.rodando + 1, ' ', basename(Player_Musica.playlist[Player_Musica.rodando]))


    def encerrar_mixer_audio(self):
        mixer_music.stop()
        mixer.quit()
        print("Encerrando music_x player.....")

    def play_pause(self):
        """
        Pause e Continue a musica
        :return: string contendo o texto para usar no botão play-pause
        """
        acao = ''
        tocando = mixer_music.get_busy()
        if tocando == False:
            mixer_music.unpause()
            print("Musica tocando")
            acao = 'Pausar'
            return  acao

        else:
            mixer_music.pause()
            acao = 'Reproduzir'
            print("Musica em parad")
            return acao


    def reinicio(self):
        mixer_music.rewind()
        print("Musica reinicializada")


    def aumentar_vol(self):

        self.volume = self.volume + 0.05
        if self.volume > 1:
            self.volume = 1
            mixer_music.set_volume(self.volume)
            print('volume: ', str(self.volume))
        else:
            mixer_music.set_volume(self.volume)
            print('volume: ', str(self.volume))


    def abaixar_vol(self):
        self.volume = self.volume - 0.05
        if self.volume < 0:
            self.volume = 0
            mixer_music.set_volume(self.volume)
            print('volume: ', str(self.volume))
        else:
            vol = mixer.music.set_volume(self.volume)
            print('volume: ', str(self.volume))


    def avancar_musica(self):
        if Player_Musica.rodando + 1 >= len(Player_Musica.playlist):
            mixer_music.stop
            Player_Musica.rodando = 0
            musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
            mixer_music.play()
            print("if frequência de som atual:  ", Player_Musica.frequencia_som)
            print(Player_Musica.rodando + 1, ' ', basename(Player_Musica.playlist[Player_Musica.rodando]))

        else:
            mixer_music.stop
            Player_Musica.rodando = Player_Musica.rodando + 1
            musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
            mixer_music.play()
            print("else frequência de som atual:  ", Player_Musica.frequencia_som)
            print(Player_Musica.rodando + 1, ' ', basename(Player_Musica.playlist[Player_Musica.rodando]))


    def voltar_musica(self):
        if Player_Musica.rodando <= 0:
            mixer_music.stop
            total_musicas = len(Player_Musica.playlist)
            Player_Musica.rodando = total_musicas - 1
            musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
            mixer_music.play()
            print("frequência de som atual:  ", Player_Musica.frequencia_som)
            print(Player_Musica.rodando + 1, ' ', basename(Player_Musica.playlist[Player_Musica.rodando]))
        else:
            mixer_music.stop
            Player_Musica.rodando = Player_Musica.rodando - 1
            musica = mixer_music.load(Player_Musica.playlist[Player_Musica.rodando])
            mixer_music.play()
            print("frequência de som atual:  ", Player_Musica.frequencia_som)
            print(Player_Musica.rodando + 1, ' ', basename(Player_Musica.playlist[Player_Musica.rodando]))
