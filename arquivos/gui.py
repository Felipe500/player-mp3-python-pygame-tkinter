from tkinter import Label, HORIZONTAL, Listbox, SINGLE, END
from tkinter.ttk import Scrollbar

import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()


class GuiAplication:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root = root
        self.tela_secundaria = None
        self.label_musica = None
        self.barra_progresso = None
        self.bar_progress = None
        self.label_end = None
        self.label_init = None
        self.controles = None
        self.bar_volume = None
        self.bt_avancar = None
        self.bt_play_pause = None
        self.bt_voltar = None
        self.bt_atualizar_playlist = None
        self.acao = 'Play'
        self.playlist_aberta = False

    def build_interface(self):
        self.tela_principal()
        self.frames_tela()
        self.widgets_tela_musica()
        self.widgets_controles()
        self.widgets_barra_progresso()

    def tela_principal(self):
        self.root.title("Player de musica")
        self.root.configure(background='#6a50c9')
        width = 800  # Width
        height = 500  # Height

        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        # self.root.geometry("800x500")

        self.root.resizable(True, True)

    def frames_tela(self):
        self.tela_secundaria = customtkinter.CTkFrame(master=self.root, width=320, height=360, corner_radius=15)
        self.tela_secundaria.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.97)

        self.descricao_musica = customtkinter.CTkFrame(master=self.tela_secundaria, width=320, height=100,
                                                       corner_radius=0)
        self.descricao_musica.place(relx=0.025, rely=0.01, relwidth=0.98, relheight=0.06)

        self.barra_progresso = customtkinter.CTkFrame(master=self.tela_secundaria, width=320, height=100,
                                                      corner_radius=0)
        self.barra_progresso.place(relx=0.025, rely=0.80, relwidth=0.95, relheight=0.05)

        self.controles = customtkinter.CTkFrame(master=self.tela_secundaria, width=320, height=100, corner_radius=0)
        self.controles.place(relx=0.025, rely=0.87, relwidth=0.95, relheight=0.10)

    def widgets_tela_musica(self):
        self.label_musica = Label(
            self.descricao_musica,
            text='musica - xxxxxxxxxxxxxxxxxxxx.xxxxxxxxxxxxxx',
            bg="#583bbf",
            fg="white",
            width=100,
            anchor="center",
            font=('verdana', 9, 'bold')
        )
        self.label_musica.place(relx=0, rely=0, relwidth=0.91, relheight=1)

        img_btn = customtkinter.CTkImage(
            light_image=Image.open("examples/open_.png"),
            dark_image=Image.open("examples/open_.png"),
            size=(30, 30)
        )

        customtkinter.CTkButton(
            self.descricao_musica,
            image=img_btn,
            border_color='red',
            fg_color="#583bbf",
            text='',
            corner_radius=3,
            hover_color='#6242d5',
            command=self.tela_playlist

        ).place(relx=0.90, rely=0, relwidth=0.1, relheight=1.01)

    def widgets_controles(self):
        self.bt_atualizar_playlist = customtkinter.CTkButton(
            self.controles,
            border_spacing=0,
            text="Atualizar playlist",
            hover_color='#6242d5',
            fg_color="#583bbf",
            font=('verdana', 10, 'bold'),
        )
        self.bt_atualizar_playlist.place(relx=0.02, rely=0.05, relwidth=0.18, relheight=0.9)

        self.bt_voltar = customtkinter.CTkButton(
            self.controles, text="<<",
            border_spacing=0,
            hover_color='#6242d5',
            fg_color="#583bbf",
            font=('verdana', 10, 'bold')
        )
        self.bt_voltar.place(relx=0.36, rely=0.05, relwidth=0.1, relheight=0.9)

        self.bt_play_pause = customtkinter.CTkButton(
            self.controles,
            text=self.acao,
            corner_radius=0,
            hover_color='#6242d5',
            fg_color="#583bbf",
            font=('verdana', 10, 'bold')
        )

        self.bt_play_pause.place(relx=0.46, rely=0.05, relwidth=0.1, relheight=0.9)

        self.bt_avancar = customtkinter.CTkButton(
            self.controles,
            text=">>",
            border_spacing=0,
            border_color='red',
            hover_color='#6242d5',
            fg_color="#583bbf",
            font=('verdana', 10, 'bold')
        )
        self.bt_avancar.place(relx=0.55, rely=0.05, relwidth=0.1, relheight=0.9)

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

    def fechar_tela_playlist(self):
        if self.playlist_aberta:
            self.playlist_aberta = False
            self.frame_playlist.destroy()

    def tela_playlist(self):
        self.playlist_aberta = True

        self.frame_playlist = customtkinter.CTkFrame(
            self.tela_secundaria,
            width=300,
            height=500,
        )
        self.frame_playlist.place(relx=0.5, rely=0, relwidth=0.50, relheight=0.79)
        self.frame_playlist.grid_forget()

        img_close = customtkinter.CTkImage(
            light_image=Image.open("examples/close.png"),
            dark_image=Image.open("examples/close.png"),
            size=(30, 30)
        )

        nome_tela = Label(
            self.frame_playlist,
            text='Minha Playlist',
            bg="#583bbf",
            fg="white",
            font=('verdana', 9, 'bold')
        )
        nome_tela.place(relx=0.01, rely=0.01, relwidth=0.85, relheight=0.07)

        customtkinter.CTkButton(
            self.frame_playlist,
            text='',
            image=img_close,
            border_width=0,
            corner_radius=0,
            command=self.fechar_tela_playlist,
            fg_color="#583bbf",
            hover_color='#6242d5',
            font=('verdana', 9, 'bold')
        ).place(relx=0.85, rely=0.01, relwidth=0.15, relheight=0.07)

        scrollbar = Scrollbar(self.frame_playlist, orient="vertical")
        scrollbar.pack(side="right", fill="y")
        scrollbar.place(relx=0.90, rely=0.09, relwidth=0.10, relheight=0.80)

        self.list_box_musicas = Listbox(
            self.frame_playlist,
            width=2,
            height=15,
            selectmode=SINGLE,
            yscrollcommand=scrollbar.set,
            selectbackground='#7349bb',
            selectforeground='#fff'
        )
        self.list_box_musicas.place(relx=0.02, rely=0.09, relwidth=0.90, relheight=0.80)

        scrollbar.config(command=self.list_box_musicas.yview)

        musicas = getattr(self, "playlist_listbox")

        if len(musicas) > 0:
            for musica in musicas:
                self.list_box_musicas.insert(END, musica)

            self.list_box_musicas.itemconfigure(getattr(self, 'musica_rodando'), bg="#583bbf", fg="#fff")
            self.list_box_musicas.bind('<Double-1>', getattr(self, 'selecionar_musica_playlist'))

    def atualizar_selecao_musica(self, anterior, atual):
        if self.playlist_aberta:
            self.list_box_musicas.itemconfigure(anterior, bg="#fff", fg="black")
            self.list_box_musicas.itemconfigure(atual, bg="#583bbf", fg="#fff")
