import numpy as np

def regrets_normalisation(cumulate_regret):
    #on additionne tous nos regrets dans normalizing_sum
    new_sum = np.clip(cumulate_regret, a_min=0, a_max=None)  #tout ce qui est sous 0 dans regret_sum est mis à 0
    normalizing_sum = np.sum(new_sum) # on additionne tous les regrets de new_sum, on met ce chiffre dans normalizing_sum
    #on divise chaque regret par normalizing_sum
    if normalizing_sum > 0: #on divise new_sum par normalizing_sum
        new_sum /= normalizing_sum #chaque float de new_sum est divisé par normalizing_sum
    else: #si normalizing_sum (=l'addition de tous les regrets de new_sum) est <= 0 (passe dedans à la première itération)
        new_sum = np.repeat(1/3, 3) #equivaut a dire répète 3x 1/3 ==> new_sum = [0.333333,0.333333,0.333333]
    return new_sum #new_sum contient les regrets normalisés pour la stratégie suivante


def average_strategy(cumulate_strategy):
        average_strategy = [0, 0, 0]
        normalizing_sum = sum(cumulate_strategy)
        for a in range(3):
            if normalizing_sum > 0:
                average_strategy[a] = cumulate_strategy[a] / normalizing_sum
            else:
                average_strategy[a] = 1.0 / 3
        return average_strategy


def entrainement(iterations):
    actions = [0, 1, 2] # où 0=pierre, 1=feuille, 2=ciseaux
    utility_matrix = np.array([
                    [0, -1, 1],
                    [1, 0, -1],
                    [-1, 1, 0]])#actionUtility ==> permet de calcul les rewards. en (0,0) c'est le pierre-pierre, en (0,1) c'est le pierre pour moi, feuille pour l'opponent ce qui me donne une reward de -1. etc
    cumulate_regret_j1 = np.zeros(3) #crée une array avec [0.,0.,0.] ==> [regrets cumulés pierre, regrets cumulés feuille, regrets cumulés ciseau]. On met pas des int parce que ensuite on fait des division dedans pour normaliser
    cumulate_regret_j2 = np.zeros(3) #idem pour adversaire
    cumulate_strategy_j1 = np.zeros(3)
    cumulate_strategy_j2 = np.zeros(3)
    for i in range(iterations):
        strategy_j1 = regrets_normalisation(cumulate_regret_j1) #strategy_j1 contient les probabilités avec lesquelles ont doit choisir telle ou telle action, se perfectionne d'iteration en iteration
        strategy_j2 = regrets_normalisation(cumulate_regret_j2) #idem pour l'adversaire
        cumulate_strategy_j1 += strategy_j1
        cumulate_strategy_j2 += strategy_j2
        #on choisit une action : pierre-feuille-ciseau
        action_j1 = np.random.choice(actions, p=strategy_j1)#choisi une action parmi actions[action 0, action 1, action 2], et choisi les actions selon la distribution normalise qui au premier tour sera : [0.3333,0.3333,0.3333]
        action_j2 = np.random.choice(actions, p=strategy_j2)#la meme pour mon adversaire selon sa distribution a lui normalise_j2
        #on en deduie ce qu'on a gagné ou perdu 0 si égalité, 1 si gagné, -1 si perdu
        actual_reward_j1 = utility_matrix[action_j1, action_j2] #puisque sur les x de la matrice d'utilité c'est j1 et les y c'est j2. Je lui envoie (0,1) si y a eu pierre-feuille
        actual_reward_j2 = utility_matrix[action_j2, action_j1] #idem pour mon adversaire
        # pour chaque action pierre-feuille-ciseau (0,1,2) on va calculer le counterfactual rwrd, et donc le regret associé à chaque action
        for j in range(3):
            counterfactual_reward_j1 = utility_matrix[j, action_j1] #on déduit le counterfactual rwrd
            counterfactual_reward_j2 = utility_matrix[j, action_j2] #idem pour mon adversaire
            regret_j1 = counterfactual_reward_j1 - actual_reward_j1 #on calcule le regret
            regret_j2 = counterfactual_reward_j2 - actual_reward_j2 #idem pour mon adversaire
            #on additionne les regrets trouvé eux regrets stockés précédemment dans l'array cumulate_regret_j1[rock_regrets, paper_regrets, scissors_regrets]
            cumulate_regret_j1[j] += regret_j1 #pour l'action 0, cumulate_regret_j1[0] = cumulate_regret_j1[0]+regret_j1, pareil pour action 1 et 2
            cumulate_regret_j2[j] += regret_j2 #idem pour l'adversaire
        #average_strategy_j1 = average_strategy(cumulate_strategy_j1)
        #average_strategy_j2 = average_strategy(cumulate_strategy_j2)
        #print('--------iteration N°', i, '--------')
        #print('strategie moyenne j1', average_strategy_j1)
        #print('strategie moyenne j2:', average_strategy_j2)
    print('--------Final Average Strategy--------')
    average_strategy_j1 = average_strategy(cumulate_strategy_j1)
    average_strategy_j2 = average_strategy(cumulate_strategy_j2)
    print('strategie moyenne j1', average_strategy_j1)
    print('strategie moyenne j2:', average_strategy_j2)

def main():
    iterations = 10000
    entrainement(iterations)

if __name__ == "__main__":
    main()

#J1 c'est moi, J2 c'est mon adversaire
#np.arrange(10) ==> a = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#np.clip(arraytoclip, a_min, a_max). exemple : np.clip(a, 1, 8) ==> a = ([1, 1, 2, 3, 4, 5, 6, 7, 8, 8])
#np.zeros(). exemple : np.zeros(5) ==> array([ 0.,  0.,  0.,  0.,  0.]). np.zeros((5,), dtype=int) ==> array([0, 0, 0, 0, 0])
#test = np.sum(a) où a=[3,7] ==> test = 10
#numpy.random.choice(a, p=..), ici p est the probabilities associated with each entry in a. exemple : numpy.random.choice(self.possible_actions, p=strategy). Donne un échantillon de sel.possible_actions en random, selon la distrubution de strategy. Si p n'est pas fourni, l'échantillon suppose une distribution uniforme sur toutes les entrées de a.
