import math

from arquivos.player import Player
from arquivos.gui import GuiAplication
from tkinter.filedialog import askdirectory


class Aplication(GuiAplication, Player):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.buscar_arquivos_mp3()
        self.iniciar()
        self.build_interface()
        self.config_command()
        self.root.protocol("WM_DELETE_WINDOW", self.evento_close)
        self.root.after(0, self.update_bar_progress)
        self.update_music_infor()
        self.root.mainloop()

    def config_command(self):
        self.label_init.configure(text=str(self.get_pos_music()))
        self.bar_volume.configure(command=self.slide_set_volume)
        self.bt_atualizar_playlist.configure(command=self.button_atualizar_playlist)
        self.bt_voltar.configure(command=self.button_voltar)
        self.bt_avancar.configure(command=self.button_avancar)
        self.bt_play_pause.configure(command=self.button_play_pause)

    def evento_close(self):
        self.encerrar_mixer_audio()
        self.root.destroy()

    def button_play_pause(self):
        self.acao = self.pause_continue()
        self.bt_play_pause.configure(text=self.acao)

    def selecionar_musica_playlist(self, event):
        selecao = self.list_box_musicas.curselection()[0]
        self.atualizar_selecao_musica(self.musica_rodando, self.list_box_musicas.curselection()[0])
        self.musica_rodando = selecao
        self.play_music(self.playlist['path'], selecao)
        self.update_music_infor()

    def button_atualizar_playlist(self):
        self.pasta_musicas = askdirectory(title='Selecione pasta de músicas', initialdir=self.get_pasta_padrao())
        self.fechar_tela_playlist()
        self.buscar_arquivos_mp3(self.pasta_musicas)
        self.iniciar()
        if self.playlist['total_musicas'] < 1:
            self.label_musica.configure(text=f"--- Sem músicas na lista de reprodução ---")
            self.label_init.configure(text=f'00:00')
            self.label_end.configure(text=f'00:00')
        else:
            self.update_music_infor()

    def button_avancar(self):
        musica_anterior = self.musica_rodando
        self.avancar_musica()
        self.atualizar_selecao_musica(musica_anterior, self.musica_rodando)
        self.update_music_infor()

    def button_voltar(self):
        musica_anterior = self.musica_rodando
        self.voltar_musica()
        self.atualizar_selecao_musica(musica_anterior, self.musica_rodando)
        self.update_music_infor()

    def slide_set_volume(self, event):
        self.set_volume(float(format(self.bar_volume.get() / 100, '.2f')))

    def update_music_infor(self):
        duration_counter = math.trunc(float(self.data_musica['duration']))
        duration_minutes = int(duration_counter) // 60
        duration_seconds = int(duration_counter) % 60

        str_seconds = f"0{duration_seconds}" if duration_seconds < 10 else f"{duration_seconds}"
        self.label_end.configure(text=f'{duration_minutes}:{str_seconds}')
        self.label_musica.configure(text=f"musica - {self.data_musica['nome']}")

    def update_bar_progress(self):
        counter = math.trunc(float(self.get_pos_music()))
        minutes = counter // 60
        seconds = counter % 60
        self.bar_progress_value += counter

        if self.duration_music < 1:
            self.duration_music = 1

        str_seconds = f"0{seconds}" if seconds < 10 else f"{seconds}"

        self.label_init.configure(text=f'{minutes}:{str_seconds}')
        self.bar_progress.set((math.trunc((counter * 100) / self.duration_music)) / 100)

        self.root.after(500, self.update_bar_progress)


if __name__ == '__main__':
    Aplication()
