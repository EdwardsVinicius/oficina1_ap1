import tkinter as tk
from tkinter import messagebox
import json

f = open('game_ratings.json')
data = json.load(f)

# Função para recomendar música para um usuário baseado na média das avaliações
def recommend_song(user, k):
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

    return rec_games[:k]

def submit_rating(game, rating, user):
    game = game_var.get()
    rating = rating_var.get()
    user = user_var.get()
    data.append({"user": user, "game_title": game, "rating": rating})
    messagebox.showinfo("Sucesso", f"Avaliação do jogo {game} foi adicionada com sucesso")
    
def recommend(user, k):
    user = user_var.get()
    k = k_var.get()
    rec_games = recommend_song(user, k)
    messagebox.showinfo("Recomendações", f"Os {k} jogos recomendados para o usuário {user} são: {rec_games}")


root = tk.Tk()
root.title("Sistema de Recomendação de Música")

user_label = tk.Label(root, text="Nome do usuário:")
user_label.grid(row=0, column=0)

user_var = tk.StringVar()
user_entry = tk.Entry(root, textvariable=user_var)
user_entry.grid(row=0, column=1)

song_label = tk.Label(root, text="Nome da música:")
song_label.grid(row=1, column=0)

game_var = tk.StringVar()
song_entry = tk.Entry(root, textvariable=game_var)
song_entry.grid(row=1, column=1)

rating_label = tk.Label(root, text="Avaliação (1-5):")
rating_label.grid(row=2, column=0)

rating_var = tk.IntVar()
rating_entry = tk.Entry(root, textvariable=rating_var)
rating_entry.grid(row=2, column=1)

k_label = tk.Label(root, text="Número de recomendações:")
k_label.grid(row=3, column=0)

k_var = tk.IntVar()
k_entry = tk.Entry(root, textvariable=k_var)
k_entry.grid(row=3, column=1)

submit_button = tk.Button(root, text="Enviar avaliação", command=submit_rating)
submit_button.grid(row=4, column=0)

recommend_button = tk.Button(root, text="Recomendar músicas", command=recommend)
recommend_button.grid(row=4, column=1)

root.mainloop()
