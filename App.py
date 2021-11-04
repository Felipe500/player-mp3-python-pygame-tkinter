from arquivos.Player_Funcoes import *
from tkinter import *


root = Tk()

class Aplication(Funcoes_Player):
    def __init__(self):
        self.root = root
        #Texto do botão play-pause
        self.acao = 'Play'
        self.buscar_arquivos_mp3()
        self.inicio()
        self.iniciar()
        self.tela_principal()
        self.frames_tela()
        self.widgets_frame1()
        self.root.protocol("WM_DELETE_WINDOW", self.evento_close)
        self.root.mainloop()

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
        self.acao= (self.play_pause())
        self.bt_play_pause.config(text=self.acao)

    def atualizar_playlist(self):
        self.buscar_arquivos_mp3()
        self.inicio()
        self.iniciar()


    def frames_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg="#6600bc",
                            highlightbackground="#b471f8", highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def widgets_frame1(self):

        # botão limpar
        self.bt_buscar = Button(self.frame1, text="Atualizar playlist",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'),command=self.atualizar_playlist)
        self.bt_buscar.place(relx=0.02, rely=0.8, relwidth=0.18, relheight=0.1)

        # botão Buscar
        self.bt_voltar = Button(self.frame1, text="<<",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'),command=self.voltar_musica)
        self.bt_voltar.place(relx=0.35, rely=0.8, relwidth=0.1, relheight=0.1)

        # botão Novo
        self.bt_play_pause = Button(self.frame1, text=self.acao,
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'),command=self.evento_play_pause)
        self.bt_play_pause.place(relx=0.45, rely=0.8, relwidth=0.1, relheight=0.1)

        # Botão Altera
        self.bt_avançar = Button(self.frame1, text=">>",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'),command=self.avancar_musica)
        self.bt_avançar.place(relx=0.55, rely=0.8, relwidth=0.1, relheight=0.1)




Aplication()