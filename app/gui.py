from tkinter import *
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()


class GuiAplication:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root = root
        self.acao = 'Play'

    def tela_principal(self):
        self.root.title("Player de musica")
        self.root.configure(background='#6a50c9')
        self.root.geometry("800x500")
        self.root.resizable(True, True)

    def frames_tela(self):
        self.tela_secundaria = customtkinter.CTkFrame(master=self.root, width=320, height=360, corner_radius=15)
        self.tela_secundaria.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.97)

        self.barra_progresso = customtkinter.CTkFrame(master=self.tela_secundaria, width=320, height=100, corner_radius=0)
        self.barra_progresso.place(relx=0.025, rely=0.80, relwidth=0.95, relheight=0.05)

        self.controles = customtkinter.CTkFrame(master=self.tela_secundaria, width=320, height=100, corner_radius=0)
        self.controles.place(relx=0.025, rely=0.87, relwidth=0.95, relheight=0.10)

    def widgets_controles(self):
        self.bt_atualizar_playlist = customtkinter.CTkButton(
            self.controles,
            text="Atualizar playlist",
            hover_color='#6242d5',
            fg_color="#583bbf",
            font=('verdana', 8, 'bold'),
        )
        self.bt_atualizar_playlist.place(relx=0.02, rely=0.1, relwidth=0.18, relheight=0.8)

        self.bt_voltar = customtkinter.CTkButton(
            self.controles, text="<<",
            hover_color='#6242d5',
            bg_color="white",
            fg_color="#583bbf",
            font=('verdana', 8, 'bold')
        )
        self.bt_voltar.place(relx=0.35, rely=0.1, relwidth=0.1, relheight=0.8)

        # botão Novo
        self.bt_play_pause = customtkinter.CTkButton(
            self.controles,
            text=self.acao,
            hover_color='#6242d5',
            bg_color="white",
            fg_color="#583bbf",
            corner_radius=0,
            font=('verdana', 8, 'bold')
        )
        self.bt_play_pause.place(relx=0.45, rely=0.1, relwidth=0.1, relheight=0.8)

        # Botão Altera
        self.bt_avancar = customtkinter.CTkButton(
            self.controles,
            text=">>",
            hover_color='#6242d5',
            bg_color="white",
            fg_color="#583bbf",
            font=('verdana', 8, 'bold')
        )
        self.bt_avancar.place(relx=0.55, rely=0.1, relwidth=0.1, relheight=0.8)

        self.bar_volume = customtkinter.CTkSlider(
            self.controles,
            height=0,
            from_=0,
            to=100,
            orientation='horizontal',
            button_hover_color='#6242d5',
            button_color='#583bbf')
        self.bar_volume.place(relx=0.80, rely=0.3, relwidth=0.2, relheight=0.4)

    def widgets_barra_progresso(self):
        self.bar_progress = customtkinter.CTkProgressBar(
            self.barra_progresso,
            fg_color='white',
            progress_color='#6242d5',
            orientation=HORIZONTAL,
            mode='determinate'
        )
        self.bar_progress.place(relx=0.1, rely=0.1, relwidth=0.80, relheight=0.50)

        self.label_init = Label(
            self.barra_progresso,
            text='',
            bg="#583bbf",
            fg="white",
            font=('verdana', 9, 'bold')
        )
        self.label_init.place(relx=0, rely=0.1, relwidth=0.08, relheight=0.50)

        self.label_end = Label(
            self.barra_progresso,
            text="01:00",
            bg="#583bbf",
            fg="white",
            font=('verdana', 9, 'bold')
        )
        self.label_end.place(relx=0.92, rely=0.1, relwidth=0.08, relheight=0.50)
