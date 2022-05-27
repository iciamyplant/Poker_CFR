



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

Tout le vocabulaire du Poker dictionnaire [ici](https://www.ludo9.com/poker/regles-poker/dictionnaire-poker/vocabulaire-poker-d/definition-dealer-poker/)

BB ---- SB ---- BOUTON


| 1. PREFLOP, enchères tour 1 |2. FLOP + enchères tour 2|3. TURN + enchères tour 3|4. RIVER + enchères tour 4| 5. SHOWDOWN (= Abbatage)|
|-----------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
|SB et BB mettent leur jetons |Le dealer brûle une carte + 3 cartes retournées (=**flop**)| Le dealer brûle une seconde carte + 1 carte retournée (=**le turn**)|Le dealer brûle une troisième carte + 1 dernière carte retournée (=**la river**)|Les 2 joueurs au moins dévoilent  leurs cartes. Soit 1 joueur gagne, soit plusieurs joueurs gagnent et on partage le pot|
|Personne à gauche de la BB qui parle en premier|SB qui commence à parler (ou tout joueur encore en jeu, à la gauche immédiate du dealer)|SB qui commence à parler (ou tout joueur encore en jeu, à la gauche immédiate du dealer)|SB qui commence à parler (ou tout joueur encore en jeu, à la gauche immédiate du dealer)|
| options: fold (se coucher), check (=parole, que si a déjà misé assez avant), call (suivre, minimum BB pour entrer ds le coup), raise (miser)| idem |idem |idem|
|dernier joueur à parler est BB| dernier joueur à parler est le dealer | dernier joueur à parler est le dealer|dernier joueur à parler est le dealer|
|quand tout le monde est ok --> FLOP|quand tout le monde est ok --> TURN|quand tout le monde est ok --> RIVER|quand tout le monde est ok --> SHOWDOWN|BB, SB, D se déplacent d'un cran vers gauche : dealer suivant récupère toutes les cartes, les mélanges, puis effectue une nouvelle distribution des cartes de poker, nouveau coup débute|


#### Stratégie

##### 1. La position
##### 2. Probabilités de première main
52 cartes, probabilité Brelan = 4,83 %

# II - Les Poker Bots

### 1. Poker = Imperfect-Information Game

- Theory of Games and Economic Behavior, John von Neumann et Oskar Mergenstern, 1944
- La théorie des jeux classifie les jeux en catégories en fonction de leurs approches de résolution (jeux à somme nulle, Jeux simultanés, Jeux séquentiels, Jeux à information complète et information incomplète, etc.), et cherche à mettre en évidence des stratégies optimales
- Depuis le début des années 1980, Théorie des jeux occupe une place de plus en plus importante en informatique : application dans la théorie des automates, logique, vérification de programmes, optimisation, et apprentissage par renforcement

- Dans tous les jeux, les décisions peuvent être représentées par un arbre, dont chaque nœud est associé au joueur qui décide. Les gains de tous les joueurs sont associés aux terminaisons (derniers noeuds) de l'arbre.
- Imperfect-Information Games = situations dans lesquelles un joueur qui doit prendre une décision ne connaît pas les choix effectués par les joueurs qui ont joué avant lui : il ne connaît pas parfaitement le noeud auquel il se situe
- Perfect-Information Games : échecs, jeu de Go
- En 1997, Deep Blue vainquait le maître des échecs Garry Kasparov.
- En 2016, AlphaGo venait à bout du meilleur joueur de go, Lee Sedol

"« Les jeux à informations complètes peuvent se résumer sous la forme d’un énorme arbre des décisions à parcourir. L’intelligence essaye de diminuer la taille de cet arbre en se focalisant sur les décisions les plus importantes », détaille Sébastien Konieczny, chargé de recherche au CNRS et spécialiste de la logique pour l’intelligence artificielle. De par son information incomplète, le poker implique des techniques de gestion de l’incertitude, de probabilité et de tirages aléatoires.  » Doté d’une énorme puissance de calcul, le programme Libratus utilise également l’apprentissage par renforcement pour « comprendre le fonctionnement de son adversaire et s’adapter à son jeu », conclut le chercheur."

- Nash equilibrum in Poker, Y a t il une stratégie optimale en Poker ? Oui


### 2. Historique

2019 : Pluribus
2017 : Libratus

- 20 jours d’affrontements dans un casino de Pittsburgh
- 120,000 mains jouées au no-limit Texas Hold'em
- a combattu contre 4 joueurs professionnels de Poker (Dong Kim, Jason Les, Jimmy Chou et Daniel McAulay), affrontés en duel dans des parties simultanées
- IA crée par 2 chercheurs de Carnegie Mellon University
- Brains vs. AI competition
- article cité par un des chercheurs Cernegie [site](https://www.engadget.com/2017-02-10-libratus-ai-poker-winner.html)

2015 : AI Claudico

University of Alberta Computer Poker Research Group [leur site](https://webdocs.cs.ualberta.ca/~games/poker/)
- DeepStackAI (2017)
- Cepheus (2015)
- ... Poki, PsOpt
- Polaris (2007) : s'est mesuré à deux joueurs de poker américains de renommée mondiale, Phil Laak et Ali Eslami, lors de la Conférence annuelle sur l'intelligence artificielle en 2007 à Vancouver. Les deux joueurs humains ont gagné de justesse après quatre parties, avec un match nul, une victoire pour le logiciel et deux victoires pour les hommes.


### 3. Poker en ligne & bots

- Pokerstars et Winamax reçoivent chaque mois plusieurs centaines de mails de la part de joueurs estimant avoir affronté un bot
Article [Usbek & Rica](https://usbeketrica.com/fr/article/poker-en-ligne-les-bots-finiront-ils-par-chasser-les-humains)
de nommbre


# III - Create a Poker Bot

### 1. Reinforcement learning

### 2. Counterfactual Regret Minimization (CFR) algorithm
- vanilla cfr
- monte carlo cfr 


### 3. Abstractions








