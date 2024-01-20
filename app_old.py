from arquivos.player import Player
from tkinter import *
from tkinter.ttk import Progressbar, Scale
import math

root = Tk()


class Aplication(Player):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root = root
        self.acao = 'Play'
        self.buscar_arquivos_mp3()
        self.iniciar()
        self.tela_principal()
        self.frames_tela()
        self.widgets_frame1()
        self.widgets_frame2()
        self.root.protocol("WM_DELETE_WINDOW", self.evento_close)
        self.root.after(0, self.update_bar_progress)
        self.update_music_infor()
        self.root.mainloop()

    def update_music_infor(self):
        duration_counter = math.trunc(float(self.duration_music))
        duration_minutes = int(duration_counter) // 60
        duration_seconds = int(duration_counter) % 60
        str_seconds = f"0{duration_seconds}" if duration_seconds < 10 else f"{duration_seconds}"

        self.label_end.configure(text=f'{duration_minutes}:{str_seconds}')

    def update_bar_progress(self):
        self.bar_progress_value = 1
        self.pos_music += 1
        counter = math.trunc(float(self.get_pos_music()))
        minutes = counter // 60
        seconds = counter % 60
        self.bar_progress_value += counter

        if self.duration_music < 1:
            self.duration_music = 1

        str_seconds = f"0{seconds}" if seconds < 10 else f"{seconds}"

        self.label_init.configure(text=f'{minutes}:{str_seconds}')
        self.bar_progress.config(value=math.trunc((counter * 100) / self.duration_music))

        self.root.after(500, self.update_bar_progress)

    def tela_principal(self):
        self.root.title("Player de musica")
        self.root.configure(background='#6a50c9')
        self.root.geometry("800x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=500)
        self.root.minsize(width=400, height=300)

    def evento_close(self):
        self.encerrar_mixer_audio()
        self.root.destroy()

    def evento_play_pause(self):
        self.acao = self.pause_continue()
        self.bt_play_pause.config(text=self.acao)

    def atualizar_playlist(self):
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

    def slider_pos_music(self, event):
        value_progress_bar = math.trunc((self.slider.get() * self.duration_music) / 100)
        self.set_pos_music(value_progress_bar)
        self.bar_progress.config(value=math.trunc((value_progress_bar * 100) / self.duration_music))

    def frames_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg="#6600bc",
                            highlightbackground="#b471f8", highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

        self.frame2 = Frame(self.root, bd=4, bg="#6600bc", highlightbackground="#b471f1", highlightthickness=3)
        self.frame2.place(relx=0.025, rely=0.60, relwidth=0.95, relheight=0.15)
        self.frame2.after(100, self.update_bar_progress)

    def widgets_frame1(self):
        # botão limpar
        self.bt_buscar = Button(self.frame1, text="Atualizar playlist",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command=self.atualizar_playlist)
        self.bt_buscar.place(relx=0.02, rely=0.8, relwidth=0.18, relheight=0.1)

        # botão Buscar
        self.bt_voltar = Button(self.frame1, text="<<",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command=self.button_voltar)
        self.bt_voltar.place(relx=0.35, rely=0.8, relwidth=0.1, relheight=0.1)

        # botão Novo
        self.bt_play_pause = Button(self.frame1, text=self.acao,
                                    bg="#583bbf", fg="white", font=('verdana', 8, 'bold'),
                                    command=self.evento_play_pause)
        self.bt_play_pause.place(relx=0.45, rely=0.8, relwidth=0.1, relheight=0.1)

        # Botão Altera
        self.bt_avançar = Button(self.frame1, text=">>",
                                 bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command=self.button_avancar)
        self.bt_avançar.place(relx=0.55, rely=0.8, relwidth=0.1, relheight=0.1)

        self.bar_volume = Scale(self.frame1, from_=0, to=100, orient='horizontal', command=self.slide_set_volume)
        self.bar_volume.place(relx=0.70, rely=0.83, relwidth=0.2, relheight=0.05)

    def widgets_frame2(self):
        self.bar_progress = Progressbar(self.frame2, orient=HORIZONTAL, length=100, mode='determinate', value=50)
        self.bar_progress.place(relx=0.08, rely=0.15, relwidth=0.82, relheight=0.3)
        self.bar_progress.after(1000, self.update_bar_progress)

        self.slider = Scale(self.frame2, from_=0, to=100, orient='horizontal', command=self.slider_pos_music)
        self.slider.place(relx=0.08, rely=0.1, relwidth=0.82, relheight=0.2)

        self.label_init = Label(self.frame2, text=str(self.get_pos_music()), bg="#583bbf", fg="white",
                                font=('verdana', 9, 'bold'))
        self.label_init.place(relx=0, rely=0.1, relwidth=0.08, relheight=0.21)

        self.label_end = Label(self.frame2, text="01:00", bg="#583bbf", fg="white", font=('verdana', 9, 'bold'))
        self.label_end.place(relx=0.92, rely=0.1, relwidth=0.08, relheight=0.21)


Aplication()
