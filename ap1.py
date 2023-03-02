from tkinter import *
import recommender as rec

class App:
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1['pady'] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2['padx'] = 20
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3['padx'] = 20
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4['padx'] = 20
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5['padx'] = 20
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6['padx'] = 20
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7['padx'] = 20
        self.container7['pady'] = 20
        self.container7.pack()

        self.title = Label(self.container1, text='Sistema de Recomendação de Jogos')
        self.title.pack()

        # User
        self.userLabel = Label(self.container3, text='Nome do usuário')
        self.userLabel.pack(side=LEFT)

        self.user = Entry(self.container3, textvariable = StringVar())
        self.user['width'] = 30
        self.user.pack(side=LEFT)

        # Game name
        self.gameLabel = Label(self.container4, text='Nome do jogo')
        self.gameLabel.pack(side=LEFT)

        self.game = Entry(self.container4, textvariable = StringVar())
        self.game['width'] = 30
        self.game.pack(side=LEFT)

        # Avaliação
        self.ratingLabel = Label(self.container5, text='Avaliação (1-5)')
        self.ratingLabel.pack(side=LEFT)

        self.rating = Entry(self.container5, textvariable = IntVar())
        self.rating['width'] = 30
        self.rating.pack(side=LEFT)

        # Número de recomendações
        self.qtdRecLabel = Label(self.container6, text='N. de Recomendações')
        self.qtdRecLabel.pack(side=LEFT)

        self.qtdRec = Entry(self.container6, textvariable = IntVar())
        self.qtdRec['width'] = 30
        self.qtdRec.pack(side=LEFT)

        # Botoes
        self.recommend = Button(self.container7, text='Recomendar Jogos')
        self.recommend['width'] = 12
        self.recommend['command'] = self.recommend
        self.recommend.pack(side=RIGHT)

        self.recommend = Button(self.container7, text='Enviar Avaliação')
        self.recommend['width'] = 12
        self.recommend['command'] = self.submit_rating
        self.recommend.pack(side=RIGHT)

        self.quit = Button(self.container7, text='Sair')
        self.quit['width'] = 12
        self.quit['command'] = root.destroy
        self.quit.pack(side=RIGHT)

    def recommend(self):
        user = self.user.get()
        qtdRec = self.qtdRec.get()
        rec.recommend(user, qtdRec)

    def submit_rating(self):
        game = self.game.get()
        rating = self.rating.get()
        user = self.user.get()
        rec.submit_rating(game, rating, user)



root = Tk()

# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text='Sistema de Recomendação').pack()

# ttk.Entry(root).pack()

# ttk.Button(frm, text='Quit', command=root.destroy).pack()
App(root)
root.mainloop()