import math

from app.player import Player
from app.gui import GuiAplication


class Aplication(GuiAplication, Player):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.buscar_arquivos_mp3()
        self.iniciar()
        self.tela_principal()
        self.frames_tela()
        self.widgets_controles()
        self.widgets_barra_progresso()
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

    def button_atualizar_playlist(self):
        self.buscar_arquivos_mp3()
        self.iniciar()

    def button_avancar(self):
        self.avancar_musica()
        self.update_music_infor()

    def button_voltar(self):
        self.voltar_musica()
        self.update_music_infor()

    def slide_set_volume(self, event):
        self.set_volume(float(format(self.bar_volume.get() / 100, '.2f')))

    def update_music_infor(self):
        duration_counter = math.trunc(float(self.duration_music))
        duration_minutes = int(duration_counter) // 60
        duration_seconds = int(duration_counter) % 60

        str_seconds = f"0{duration_seconds}" if duration_seconds < 10 else f"{duration_seconds}"
        self.label_end.configure(text=f'{duration_minutes}:{str_seconds}')

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
