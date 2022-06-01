



# I - Poker - Informations générales

Poker = famille de jeux de cartes

Variantes | Modes | Formats | Types de jeu| Tournois |
|------|----------|-------|-------|-------|
| Le Texas Hold'em | Low | No limit(montant et relances illimité)| cash game = joueur peut quitter la table et échanger ses jetons contre de l'argent|World Series of Poker|
|Omaha|High| Pot Limit (relance maximale égale à la valeur du pot)| tournoi = impossible de convertir ses jetons en argent, on gagne de l’argent en ayant bien classés dans le tournoi, à une place payée|World Poker Tour|
|Le Razz|High low| Limit| tournoi bounty = quand j’élimine un joueur je gagne de l’argent|European Poker Tour|
|Le Stud ||Half pot limit|sit and go|Asia Pacific Poker Tour|
|5 Card Draw, ...|||| Latin American Poker Tour|


### No limit Texas Hold’em, règles de base :

= se joue avec des cartes et des jetons
= jeu de combinaisons à 5 cartes
= alterne les étapes de distribution de cartes et les enchères
= 52 cartes, réparties en 4 couleurs qui chacune comportent 13 cartes, plus forte carte est l'AS la moins forte est le 2
= 2 à 10 joueurs
= heads-up = une partie qui ne confronte que deux joueurs

But : gagner les jetons des autres joueurs, être le dernier joueur avec des jetons

**Le board** = les 5 cartes qu’on met sur la table
Objectif d’avoir la meilleure combinaison de 5 cartes (7 cartes en tout) 

- Quinte Flush Royale (10,V,D,R,A+Couleur)
- Quinte Flush (Suite+Couleur)
- Carré
- Full (Brelan+Paire)
- Couleur / Flush
- Suite / Quinte : as carte la plus haute ET carte la plus basse
- Brelan
- Double paire
- Paire
- Hauteur / carte haute

**Cave** = nombre minimum de jetons à avoir pour pouvoir jouer sur une table
**Croupier** = celui qui mélange et distribue les cartes
**Petite Blinde (SB) et Grosse Blinde (BB)** = l’un à côté de l’autre, tourne à chaque main, sont obligés de miser (force à jouer) BB = 2x la SB
**Joueur au cut off** = le dealer précédent
**Dealer (=donneur)** = personne qui distribue les cartes, compte les jetons et s'assure du bon déroulement du jeu à la table, Dealer suit joueur Small Blind et Big Blind avant le SB (tourne a chauqe tour)
**kicker** = carte d'accompagnement, qui fait la difference
**Buying in** = ce qu'on paye pour rentrer en tournoi
**Bakroll** = Cagnotte consacrée au poker, matelas d'argent qu'un joueur professionnel ou amateur gagnant possède, généralement sur un compte disjoint de son compte courant, et dans lequel il puise pour payer ses inscriptions de tournois ou pour se caver en cash-game
**Tells** = indices que révèlent le comportement d’un joueur, attitude, tempo des mises, mimiques, émotions
**Fish** = joueur novice
**limp** = Limper, action qui ne peut se produire qu'avant le flop. Si un joueur décide d'aller voir le flop en investissant le moins d'argent possible alors il paye juste le montant de la big blind
**stratégie push/fold** = réduire votre liste d'options à 2, soit partir à tapis, soit se coucher, avant le flop
**78o** = 7 et 8 offsuit, pas de même couleur
**78s** = un sept et un huit de même couleur

Tout le vocabulaire du Poker dictionnaire [ici](https://www.ludo9.com/poker/regles-poker/dictionnaire-poker/vocabulaire-poker-d/definition-dealer-poker/)

BB ---- SB ---- BOUTON


| 1. PREFLOP, enchères tour 1 |2. FLOP + enchères tour 2|3. TURN + enchères tour 3|4. RIVER + enchères tour 4| 5. SHOWDOWN (= Abbatage)|
|-----------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
|SB et BB mettent leur jetons |Le dealer brûle une carte + 3 cartes retournées (=**flop**)| Le dealer brûle une seconde carte + 1 carte retournée (=**le turn**)|Le dealer brûle une troisième carte + 1 dernière carte retournée (=**la river**)|Les 2 joueurs au moins dévoilent  leurs cartes. Soit 1 joueur gagne, soit plusieurs joueurs gagnent et on partage le pot|
|Personne à gauche de la BB qui parle en premier|SB qui commence à parler (ou tout joueur encore en jeu, à la gauche immédiate du dealer)|SB qui commence à parler (ou tout joueur encore en jeu, à la gauche immédiate du dealer)|SB qui commence à parler (ou tout joueur encore en jeu, à la gauche immédiate du dealer)|
| options: fold (se coucher), check (=parole, que si a déjà misé assez avant), call (suivre, minimum BB pour entrer ds le coup), raise (miser)| idem |idem |idem|
|dernier joueur à parler est BB| dernier joueur à parler est le dealer | dernier joueur à parler est le dealer|dernier joueur à parler est le dealer|
|quand tout le monde est ok --> FLOP|quand tout le monde est ok --> TURN|quand tout le monde est ok --> RIVER|quand tout le monde est ok --> SHOWDOWN|BB, SB, D se déplacent d'un cran vers gauche : dealer suivant récupère toutes les cartes, les mélanges, puis effectue une nouvelle distribution des cartes de poker, nouveau coup débute|

# II - Théorie des jeux
 
Theory of Games and Economic Behavior, John von Neumann et Oskar Mergenstern, 1944. La théorie des jeux est un domaine des mathématiques fournissant des outils pratiques pour modéliser et raisonner sur des situations interactives (= des jeux). (Définition : La theorie des jeux permet une analyse formelle des problemes posés par l’interaction strategique d’un groupe d’agents rationnels poursuivant des buts qui leur sont propres).

- La théorie des jeux **classifie les jeux en catégories** en fonction de leurs approches de résolution
- **et cherche à mettre en évidence des stratégies optimales** selon cette catégorisation

==> Depuis le début des années 1980, la théorie des jeux occupe une place de plus en plus importante en informatique : application dans la théorie des automates, logique, vérification de programmes, optimisation, et apprentissage par renforcement...

### 1. Classification des jeux

Les situations interactives peuvent avoir une nature très différente en fonction de nombreux facteurs comme le nombre de joueurs, la structure des utilitaires ou l'ordre des coups, etc. Sur la base de ces caractéristiques, nous pouvons classer les jeux en types (tel que les jeux à somme nulle, jeux simultanés, jeux séquentiels, jeux à information complète et information incomplète, etc.)

Classification | Définition| Exemple |
|------|----------|-------|
| Jeux à somme nulle (=strictement compétitifs) / Jeux à somme non-nulle |jeu à somme nulle = les jeux où l'intérêt de l'un des deux joueurs est strictement opposé à l'intérêt de l'autre joueur. Si les préférences des joueurs sont représentées par une fonction de gain ou une fonction d'utilité, alors la somme des deux fonctions est toujours égale à 0|A somme nulle : pierre-feuille-ciseaux, Poker, échecs. Non-nulle : dilemme du prisonnier (dans certains cas, les deux joueurs peuvent perdre).|
| Jeux à information complète / Jeux à information incomplète|information complète si chaque joueur connaît lors de la prise de décision : ses possibilités d'action ; les possibilités d'action des autres joueurs ; les gains résultants de ces actions ; les motivations des autres joueurs.|Perfect-Information Games : échecs, jeu de Go. Imformation incomplète : Poker, Tarot|
|Jeux à information parfaite / Jeux à information imparfaite|||
|Jeux finis / Jeux non finis|On dit qu'un jeu est fini lorsque l'ensemble des stratégies de chacun des joueurs est fini|Jeu fini : dilemme du prisonnier est un jeu fini car chacun des joueurs n'a que deux stratégies possibles. Non fini : jeu du duopole de Cournot (chaque entreprise choisit la quantité de bien qu'elle produit dans l'ensemble des réels positifs)|
|Jeux coopératifs / Jeux non-coopératifs|||
|Jeux à 2 joueurs / Jeux à n joueurs|||

Notations :
- un ensemble N de joueurs N = {1, 2, ..., n}
- pour chaque joueur i un ensemble de stratégies Si = {s1, s2, ..., sni}
- pour chaque joueur i une fonction de valuation (=utilité) ui : S1 * S2 * ... Sn, qui à chaque ensemble de stratégies associe les gains du joueur i.


Dans tous les jeux, les décisions peuvent être représentées par un arbre, dont chaque nœud est associé au joueur qui décide. Les gains de tous les joueurs sont associés aux terminaisons (derniers noeuds) de l'arbre. Dans les Imperfect-Information Games = situations dans lesquelles un joueur qui doit prendre une décision ne connaît pas les choix effectués par les joueurs qui ont joué avant lui : il ne connaît pas parfaitement le noeud auquel il se situe. Une fois que nous avons classifié un jeu, nous pouvons commencer à raisonner à son sujet en utilisant des théorèmes génériques connus qui s'appliquent à notre type de jeu.

### 2. Stratégies Optimales

Stratégie = décrit comment agir dans toutes les situations possibles. Une strategie pure du joueur i est un plan d’action qui prescrit une action de ce joueur pour chaque fois qu’il est susceptible de jouer. On note par **Si** l’ensemble des stratégies pures du joueur i et par **si** une stratégie pure de ce joueur.

**2.1 : La stratégie de l'elimination des stratégies dominées (EISD)**

|| u| v | w |
|------|----------|-------|-------|
|x|3,6| 7,1|4,8|
|y|5,1|8,2|6,1|
|z|6,0|6,2|3,2|

- Joueur ligne parle en premier : élimine x (=14)
- Joueur colonne : a le choix entre tout ce qui reste, prend le meilleur choix (2,2) donc v, élimine le pire (1,0) donc u
- Joueur ligne : (8,6) > (6,3) donc élimine z
- Joueur colonne : 2 > 1 donc élimine w
- Solution : (8,2) (y,v) = c'est l'équilibre de nash

==> Parfois la stratégie dominante de l'un et la stratégie dominante de l'autre amènent à une seule et même réponse
==> Problème majeur de cette méthode: tous les jeux ne sont pas résolvable par EISD

**2.2 : L'équilibre de Nash**
- équilibre dans lequel aucun des joueurs ne va changer sa stratégie parce qu'il va etre moins bien placé que s'il decidait de rester dans sa stratégie
- n'implique pas que les joueurs acquièrent leur utilité max : ça peut être un équilibre sous-performant
- un jeu peut avoir plusieurs équilibres de Nash
- [video](https://www.youtube.com/watch?v=wZAztwm4gI8)


# III - Poker Bots


### 1. Type de jeu du Heads up NLTH

Heads Up No Limit Texas Hold'em Poker = is an example of two person zero-sum finite game with imperfect information and chance moves
- **two person** : deux personnes car il y a deux joueurs impliqués
- **finite game** : implique qu'il y a un nombre fini d'histoires possibles d'actions. Au poker, ce nombre est énorme mais en effet fini.
- **zero-sum** :le jeu est considéré comme à somme nulle si tous les gains (les joueurs gagnent/perdent) totalisent zéro. Cela vaut pour le poker. À moins qu'il n'y ait un match nul où aucun joueur ne gagne quoi que ce soit, le pot va à l'un des joueurs, ce qui fait que l'autre perd l'équivalent
- **imperfect information** : signifie que les joueurs ne sont pas conscients de l'état exact du jeu - il y a des informations cachées dont les joueurs ne sont pas conscients. Au poker, cette information cachée est la main de l'adversaire.
- **chance moves** : signifie qu'il y a certains éléments aléatoires du jeu sur lesquels les joueurs n'ont aucun contrôle - au poker, ce sont des tours d'enchères aléatoires consécutifs ou les cartes initiales distribuées

Ce type de jeu implique certains théorèmes ou modèles.

### 2. Avoir une stratégie au Poker

Dans des jeux comme le poker, les actions choisies via des stratégies ne peuvent pas être entièrement déterministes (Les stratégies doivent être aléatoires, la randomisation est nécessaire, sinon l'adversaire connaît notre modèle de pari). Dans la théorie des jeux, une randomisation des décisions en points de décision est réalisée via des probabilités.

**Behavioral Strategy** = consiste en une description complète de la façon d'agir via des distributions de probabilités sur les actions aux points de décision. Imaginons pour une main 8/9 au preflop, on peut avoir une distribution de probabilités : 0.15 check, 0.35 bet 5, 0.4 bet 10, 0.05 all-in ... Les probabilités guarantissent la randomization puisqu'à chaque action différente des probabilités différentes, ce qui limite l'exploitabilité.

<img width="629" alt="Behavioral_strategy" src="https://user-images.githubusercontent.com/57531966/171422678-84a97163-40ac-4f6c-8299-50c276898253.png">

- Profils de stratégie (=ensemble des stratégies) composé de 2 stratégies au HUNLTH, une par joueur - bleu et jaune)
- Un tour de jeu serait une séquence d'actions tirées de distributions de probabilités données par les stratégies des joueurs (+ actions du croupier comme chance)
- Une fois qu'un jeu est terminé, les joueurs gagnent leurs utilités (ou gains). Parce que nous sommes installés dans un cadre probabiliste, chaque joueur a des utilités attendues. Cela signifie que nous pouvons évaluer les stratégies via les utilités attendues.

### 2. Nash Equilibrium, la stratégie optimale

Y a t-il une stratégie optimale au Poker ? Selon la théorie des jeux, oui : le profil de stratégie Nash-Equilibrium. Et l'algorithme CFR tente d'en faire une approximation.

Nash Equilibrium = profil de stratégie tel qu'aucun joueur n'a d'incitation à dévier. Equilibre entre les joueurs, **point où aucun joueur ne gagne à changer de stratégie**. Les deux joueurs jouent un profil de stratégie Nash-Equilibrium si changer sa stratégie pour un joueur n'apporte aucune valeur supplémentaire (en termes d'utilité) lorsque l'autre joueur joue sa stratégie d'origine - les deux joueurs jouent les meilleures réponses l'un à l'autre (c'est le cas en bas à gauche de la figure en dessous).

Exemple : deux marchands de glace, bleu et rouge se partagent la plage. Imagineons que chaque plagiste va au glacier le plus proche.
- en haut à gauche, ils gagneront la même utilité
- en haut à droite, le glacier bleu a + d'utilité
- en bas a gauche = Nash equilibirum (aucun glacier ne gagne à changer de stratégie. Si l'un bouge, peu importe de quel côté, il perdera de la surface de plage. Même si ça n'est pas forcément la solution optimale, car les plagistes aux extrémités peuvent être découragés du chemin à parcourir)
- en bas à droite, le glacier bleu joue à l'équilibre de Nash, le glacier rouge non. Le glacier bleu a + d'utilité

![nash_equilibrium](https://user-images.githubusercontent.com/57531966/171424601-4f523508-0bb5-46a5-839d-3c79092613af.png)


**Est-ce que Nash Equilibrium existe pour le poker ?**
- Nash’s Existence Theorem indique que pour les jeux finis (dont le poker), l'équilibre de Nash est garanti d'exister
- le théorème Minimax prouve que pour les jeux finis à somme nulle à deux joueurs, il existe la meilleure utilité unique possible appelée valeur du jeu pour les deux joueurs en gain d'équilibre

**Y a-t-il qu'un ou plusieurs NE ?**
- Toutes les valeurs d'équilibre de Nash au poker sont égales - elles produisent la même utilité attendue
- les NE sont interchangeables : vous pouvez jouer n'importe quelle stratégie contre n'importe quelle stratégie adverse à partir de n'importe quel équilibre de Nash et vous atterrirez avec le même gain : la valeur du jeu

Si l'on choisi de jouer n'importe quelle stratégie à partir de n'importe quel équilibre de Nash, on est assuré de ne pas perdre. Il est hautement improbable que votre adversaire humain joue la stratégie NE, vous le surpasserez surement car il s'écartera de sa stratégie NE (en bas à droite) et il obtiendra donc un gain inférieur. Or le jeu de poker est un jeu à somme nulle pour deux joueurs, ce qui signifie que nous obtiendrons surement des gains plus élevés.

==> En pratique donc, jouer à Nash Equilibrium permet en principe de gagner (contre des humains sujets aux erreurs)
==> Notre algorithme CFR – produit une approximation du profil de stratégie Nash-Equilibrium

### 3. Poker Game Tree

Tic-tac-toe game tree (= perfect information game):

<img width="505" alt="tictactoe_game_tree" src="https://user-images.githubusercontent.com/57531966/171430225-6d030585-7b2e-4b0b-9730-f030f80a9b19.png">

Kuhn Poker game tree (=imperfect information game):
<img width="751" alt="Poker_game_tree" src="https://user-images.githubusercontent.com/57531966/171431519-8bc2061b-5553-4149-b834-28564afeb508.png">

Le Kuhn Poker est un poker simplifié où seulement 3 cartes différentes sont distribuées (Q,J,K). Pour 2 joueurs, 1 carte est distribuée par joueur (le joueur a soit un K, soit un J, soit un Q). Il n'y a pas de cartes publiques.

- les nœuds représentent les états du jeu
- les noeuds jaunes représentent les états du jeu où le joueur n°1 (j1) agit, les nœuds bleus représentent les états du jeu où le joueur n°2 (j2) agit
- ici la distribution des cartes pourraît être (selon la forme carte j1../..carte j2)  : Q/J, K/J, J/Q, Q/K, J/K, K/Q. D'où, 6 noeuds au départ.
- les arêtes représentent la transition les états de jeux, cad les actions jouées (checker ou bet=miser ici)
- le chance node est un type spécial de nœud où aucune décision n'est prise mais où une action est effectuée. Ici y a de la chance que lors de la distribution des cartes. Au NLTH y a la distribution des cartes + les cartes publiques. Ce noeud permet de modéliser le facteur chance.
- on voit que le j2 a la carte J. Mais il se nait pas quelle est la carte du j1. Donc lorsque c'est à lui de joueur il ne sait pas où il se situe, d'où les noeuds sont reliés en pointillés. 


==> le véritable état du jeu ne peut être observé par aucun des joueurs. Par conséquent, lorsque nous considérons l'arbre de jeu, nous devons séparer l'état réel du jeu de ce que les joueurs observent. Différentes perspectives de l'arbre de jeu :

- le véritable état de jeu - non observable par les joueurs, utile lors de l'apprentissage par l'auto-jeu
- perspective du joueur #1 - ensemble d'états indiscernables pour le joueur #1 (perspective de ses cartes et des actions publiques)
- perspective du joueur #2 - ensemble d'états indiscernables pour le joueur #2 (perspective de ses cartes et des actions publiques)

Perspective d'un joueur = information sets (ensemble d'états de jeux ou nodes qui ne peuvent pas être distingués pour un autre joueur)
Les information sets pour les deux joueurs dans tous les points de décision au poker sont différents. Pour le poker, les stratégies comportementales (probabilités sur les actions) sont définies pour des ensembles d'informations, pas pour des états de jeu.


### 4. Historique

**2019** : Pluribus

**2017** : Libratus (20 jours d’affrontements dans un casino de Pittsburgh, 120.000 mains jouées au Heads up no-limit Texas Hold'em, a combattu contre 4 joueurs professionnels de Poker (Dong Kim, Jason Les, Jimmy Chou et Daniel McAulay), affrontés en duel dans des parties simultanées, IA crée par 2 chercheurs de Carnegie Mellon University, Brains vs. AI competition, article cité par un des chercheurs Cernegie [site](https://www.engadget.com/2017-02-10-libratus-ai-poker-winner.html))

**2015** : AI Claudico

**2015** : Cepheus (University of Alberta too)

**2017** : DeepStackAI (University of Alberta Computer Poker Research Group [leur site](https://webdocs.cs.ualberta.ca/~games/poker/))

**2007** : Polaris (s'est mesuré à deux joueurs de poker américains de renommée mondiale, Phil Laak et Ali Eslami, lors de la Conférence annuelle sur l'intelligence artificielle en 2007 à Vancouver. Les deux joueurs humains ont gagné de justesse après quatre parties, avec un match nul, une victoire pour le logiciel et deux victoires pour les hommes)

===> Tous les programmes de Poker utilisent une forme de **Counterfactual Regret Minimization** comme composante principale (Par ex, DeepStack a utilisé un algorithme de type CFR (aidé par des réseaux de neurones) pour la résolution de sous-jeux, la stratégie de Libratus (équilibre de Nash d'une abstraction de jeu) a été calculé avec le Monte Carlo counterfactual regret minimization).


### 5. Poker en ligne & bots

- Pokerstars et Winamax reçoivent chaque mois plusieurs centaines de mails de la part de joueurs estimant avoir affronté un bot
Article [Usbek & Rica](https://usbeketrica.com/fr/article/poker-en-ligne-les-bots-finiront-ils-par-chasser-les-humains)
de nommbre


# III - Understand the CFR algorithm

### 1. Concept principal du CFR = le regret

Le concept de regret est central dans les problèmes de prise de décision répétée dans un environnement incertain (= on appelle ça online learning) 

Exemple :
- contexte incertain : résultats de matchs de NBA
- times **t** : à des moments consécutifs times t on reçoit des prédictions d'experts NBA
- **H** : notre algorithme H a pour objectif de répartir notre confiance entre les différents experts. Cad va calculer un vecteur de distribution de probabilité pt sur nos **N** experts.
- H(advices, history) = pt
- **pt** : où pt est le vecteur de distribution de probabilités de confiance sur les N experts.
- Après avoir le résultat réel des matchs :
- **lt** : vecteur de perte qui évalue les N experts. Assigne une perte pour chaque conseil d'expert N à un time t

Avec le vecteur de perte lt + la distribution de confiance pt, on peut calculer la perte attendue **ltH** :
**ltH = somme pour chaque i de N de pti * lti**

En considérant toute la temporalité T on peut calculer la perte totale attendue de notre algorithme
**LTH = somme pour chaque t de T de ltH**

Et on peut calculer la perte totale pour un seule expert i :
**Lti = somme pour chaque t de T de lti**

Le regret au temps t = la différence entre la perte totale de notre algorithme (LtH) et la meilleure perte unique (Lti) d'expert (= l'expert qui a donné les meilleurs conseils). Le regret peut être exprimé par la réflexion suivante : Si seulement j'avais écouté l'expert i tout le temps, la perte totale serait la plus faible.

**R = LTH - minLTi**

### 2. No regret learning

Un online algorithm (algorithms that build predictive models by processing data one at the time) apprend sans regret si quand T tend vers l'infini, la moyenne de son regret tend vers 0 au pire des cas (sinon vers + que 0). 
==> dans ce cas, ça veut dire qu'aucun expert n'est meilleur que notre algorithme H. Il n'y a regret envers aucun expert.

- Y a plein de online learning algorithms (=algorithms that build predictive models by processing data one at the time.)
- Mais c'est pas tous des no-regret learning algorithms

Si notre algorithme H produit un vecteur de probabilité qui place toute la masse de probabilité sur un expert, il n'apprendra pas sans regret. La randomisation est nécessaire. 

**2.3 Exemple d'algorithme No regret learning : le Regret Matching**

Regret matching est un exemple de no-regret learning algorithm.

Regret Matching = algorithme d'apprentissage sans regret qui emprunte sa logique de mise à jour au Polynomially Weighted Average Forecaster (PWA)

- L'algorithme Regret Matching Ĥ maintiendra le vecteur de poids attribué aux experts
- Une fois que le vecteur de perte (représentant les conséquences des conseils de nos experts) est révélé, nous pouvons calculer le regret cumulé par rapport à un expert i au temps t (il exprime comment nous regrettons de ne pas avoir écouté un expert particulier i)
- une fois qu'on a les regrets cumulés par expert, les poids des experts sont mis à jour avec la formule : ..
- et enfin les composantes de notre vecteur pt en question (produit de l'algorithme) sont données par : ..


# IV - Create a Poker Bot for Heads-up NLTH

### 1. Reinforcement learning
### 2. Counterfactual Regret Minimization (CFR) algorithm
- vanilla cfr
- monte carlo cfr 
### 3. Abstractions
### 4. Nested subgame solving







