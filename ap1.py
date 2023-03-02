from tkinter import *
from tkinter import messagebox
import json

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

        # User
        self.userLabel = Label(self.container3, text='Nome do usuário')
        self.userLabel.pack(side=LEFT)

        self.user = Entry(self.container3, textvariable = StringVar())
        self.user.pack(side=LEFT)

        # Game name
        self.gameLabel = Label(self.container4, text='Nome do jogo')
        self.gameLabel.pack(side=LEFT)

        self.game = Entry(self.container4, textvariable = StringVar())
        self.game.pack(side=LEFT)

        # Avaliação
        self.ratingLabel = Label(self.container5, text='Avaliação (1-5)')
        self.ratingLabel.pack(side=LEFT)

        self.rating = Entry(self.container5, textvariable = IntVar())
        self.rating.pack(side=LEFT)

        # Número de recomendações
        self.qtdRecLabel = Label(self.container6, text='N. de Recomendações')
        self.qtdRecLabel.pack(side=LEFT)

        self.qtdRec = Entry(self.container6, textvariable = IntVar())
        self.qtdRec.pack(side=LEFT)

        # Botoes
        self.recomm = Button(self.container7, text='Recomendar Jogos')
        self.recomm['command'] = self.recommend
        self.recomm.pack(side=RIGHT)

        self.submit = Button(self.container7, text='Enviar Avaliação')
        self.submit['command'] = self.submit_rating
        self.submit.pack(side=RIGHT)

        self.quit = Button(self.container7, text='Sair')
        self.quit['command'] = root.destroy
        self.quit.pack(side=RIGHT)

    def recommend_game(self, user, k):
        games = {}
        for d in data:
            if d["user"] != user:
                if d["game_title"] not in games:
                    games[d["game_title"]] = {"rating": 0, "votes": 0}
                games[d["game_title"]]["rating"]  = d["rating"]
                games[d["game_title"]]["votes"]  = 1
        for game in games:
            games[game]["rating"] = games[game]["rating"] / games[game]["votes"]
        rec_games = []
        for game in games:
            if games[game]["rating"] >= 4:
                rec_games.append(game)

        return rec_games[:int(k)]

    def recommend(self):
        user = self.user.get()
        qtdRec = self.qtdRec.get()
        rec_games = self.recommend_game(user, qtdRec)
        messagebox.showinfo("Recomendações", f"Os {qtdRec} jogos recomendados para o usuário {user} são: {rec_games}")

    def submit_rating(self):
        game = self.game.get()
        rating = self.rating.get()
        user = self.user.get()
        if (game == '' or rating == 0 or user == ''):
            messagebox.showinfo("Erro", "Preencha os campos corretamente")
        else:
            data.append({"user": user, "game_title": game, "rating": rating})
            messagebox.showinfo("Sucesso", f"Avaliação do jogo {game} foi adicionada com sucesso")


f = open('game_ratings.json')
data = json.load(f)

root = Tk()
root.title('Sistema de Recomendação de Jogos')

App(root)
root.mainloop()
f.close()