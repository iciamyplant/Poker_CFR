import numpy as np
from random import shuffle

cartes = [0,1,2]
nodes_matrix = {} #déclare un empty dictionnay without any items

def get_node(card, history):
    key = str(card) + " " + history #crée une chaine de caracteres dans key = la carte(0,1,2) + un espace + history, ce sera les keys de notre dict nodeMap
    #print('key = ', key)
    if key not in nodes_matrix: #si ce noeud n'a pas encore été rempli dans nodeMap
        action_dict = {0: 'p', 1: 'b'}
        #print('action_dict = ', action_dict)
        info_set = Node(key, action_dict) #Node est une structure de donnée qui stocke une valeur qui peut etre de nimporte quelle type de data 
        #print('info_set = ', info_set)
        nodes_matrix[key] = info_set
        #print('nodemap = self.nodeMap', nodes_matrix)
        return info_set
    return nodes_matrix[key]

def get_reward(history, card_player, card_opponent):
    terminal_pass = history[-1] == 'p' #history[-1] si la dernière occurence de la liste history est pass
    double_bet = history[-2:] == "bb" #history[-2:] affiche les 2 dernières occurances de la liste history, ca veut dire les 2 ont bet
    if terminal_pass:
        if history[-2:] == 'pp': #si les deux joueurs ont pass
            return 1 if card_player > card_opponent else -1 #1 pour le gagnant -1 pour le perdant
        else: #si le permier joueur a bet et ensuite l'autre a pass, on donne 1 au joueur qui a bet
            return 1
    elif double_bet:
        return 2 if card_player > card_opponent else -2 #si les deux ont bet, 2 pour le gagnant, -2 pour le perdant

def cfr(history, pr_1, pr_2): # fonction récursive qui parcourt chaque branche de l'arbre
    #print('------------cfr------------')

    # On initialise is_player_1 à true ou false et player_card avec les cartes du joueur
    n = len(history)
    #print('history = ', history) # au format "bb", "pbp", "pp" ... où p=pass et b=bet
    is_player_1 = n % 2 == 0 #is_player_1 boolean true if n % 2 == 0, sinon false
    #print('is_player_1 = ', is_player_1)
    player_card = cartes[0] if is_player_1 else cartes[1] #si c'est le j1 on lui donne la carte cartes[0] sinon cartes[1]

    # Si on est sur un noeud terminal on return la reward, et permet d'arrêter la récursivité
    if history[-2:] == 'pp' or history[-2:] == "bb" or history[-2:] == 'bp': #si les deux derniers caracteres de history sont bb, bp ou pp on est sur un noeud final
        card_player = cartes[0] if is_player_1 else cartes[1]
        card_opponent = cartes[1] if is_player_1 else cartes[0]
        reward = get_reward(history, card_player, card_opponent)
        #print('terminal node - reward =', reward, 'for is_player_1', is_player_1)
        return reward

    # On initialise node, strategy et action_utils
    node = get_node(player_card, history) #nous renvoie le noeud auquel nous sommes, sous forme key-value avec key = N°carte(0-1 ou 2) espace history(cad chemin déjà empruntés)
    #print('node = ', node)
    strategy = node.strategy
    #print('node.strategy =', node.strategy)
    #print('strategy =', strategy)
    action_utils = np.zeros(2) #action_utils = [0. 0.]
    #print('action_utils =', action_utils)

    # Permet de parcourir recursivement chaque branche d'un noeud : pass (act=0) et bet (act=1)
    for act in range(2): 
        next_history = history + node.action_dict[act]
        #print('node.action_dict[act] =', node.action_dict[act])
        #print('node.action_dict =', node.action_dict)
        #print('next_history =', next_history)
        #print('act =', act)
        #print('pr_1 before = ', pr_1)
        #print('pr_2 = ', pr_2)
        #print('strategy[act] = ', strategy[act])
        if is_player_1:#on appelle récursivement la cfr function, et ca va nous donner une rwd.
            action_utils[act] = -1 * cfr(next_history, pr_1 * strategy[act], pr_2) #a chaque fois qu'on monte dans l'arbre on multiplie par (-1). Parce que si le J1 a rwd de 1,P2 aura une rwd de -1
        else:
            action_utils[act] = -1 * cfr(next_history, pr_1, pr_2 * strategy[act]) #récursivité
        #print('action_utils[act] =', action_utils[act])

    # On calcule l'utilité de notre information set
    util = sum(action_utils * strategy) #calculer les regrets, on va tous les sum dans util
    regrets = action_utils - util #on va soustraire chaque action individuelle par cette récompense totale util
    if is_player_1:
        node.reach_pr += pr_1 #on met a jour la reach probability
        node.regret_sum += pr_2 * regrets #on met a jour la regret sum. pr_2, probabilité datteindre un noeud
    else:
        node.reach_pr += pr_2
        node.regret_sum += pr_1 * regrets
    
    # On retourne l'utilité de notre information set
    #print('util = ', util)
    return util

def entrainement(iterations):
    expected_game_value = 0

    # On itère iterations fois, pour entraîner notre modèle
    for i in range(iterations):
        #print('---------------- iteration N°', i, '----------------')
        shuffle(cartes) #permet de mélanger cartes (variable globale initialisé à [0, 1, 2])
        #print('cartes tirées = ', cartes, '\n')
        expected_game_value += cfr('', 1, 1)
        for _, v in nodes_matrix.items(): #pour chaque item de notre dictionnaire nodes_matrix
                v.update_strategy()

    #print('expected_game_value = ', expected_game_value)
    expected_game_value /= iterations
    #print('expected_game_value', expected_game_value)
    #print('nodes_matrix', nodes_matrix)
    print('nodes_matrix[0]', nodes_matrix.items())
    display_results(expected_game_value, nodes_matrix)

class Node:
    def __init__(self, key, action_dict, n_actions=2):
        self.key = key
        self.n_actions = n_actions
        self.regret_sum = np.zeros(self.n_actions)
        self.strategy_sum = np.zeros(self.n_actions)
        self.action_dict = action_dict
        self.strategy = np.repeat(1/self.n_actions, self.n_actions)
        self.reach_pr = 0
        self.reach_pr_sum = 0

    def update_strategy(self): #exécuté à chaque itération du jeu
        self.strategy_sum += self.reach_pr * self.strategy #reach c'est la probabilité d'atteindre ce noeud
        self.reach_pr_sum += self.reach_pr
        self.strategy = self.get_strategy()
        self.reach_pr = 0

    def get_strategy(self):
        regrets = self.regret_sum
        regrets[regrets < 0] = 0
        normalizing_sum = sum(regrets)
        if normalizing_sum > 0:
            return regrets / normalizing_sum
        else:
            return np.repeat(1/self.n_actions, self.n_actions)

    def get_average_strategy(self):
        strategy = self.strategy_sum / self.reach_pr_sum
        # Re-normalize
        total = sum(strategy)
        strategy /= total
        return strategy

    def __str__(self):
        strategies = ['{:03.2f}'.format(x)
                      for x in self.get_average_strategy()]
        return '{} {}'.format(self.key.ljust(6), strategies)


def display_results(ev, nodes_matrix):
    print('player 1 expected value: {}'.format(ev))
    print('player 2 expected value: {}'.format(-1 * ev))

    print()
    print('player 1 strategies:')
    sorted_items = sorted(nodes_matrix.items(), key=lambda x: x[0])
    for _, v in filter(lambda x: len(x[0]) % 2 == 0, sorted_items):
        print(v)
    print()
    print('player 2 strategies:')
    for _, v in filter(lambda x: len(x[0]) % 2 == 1, sorted_items):
        print(v)




if __name__ == "__main__":
    iterations = 25000
    entrainement(iterations)