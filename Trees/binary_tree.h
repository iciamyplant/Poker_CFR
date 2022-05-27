#ifndef __LEARN_TREES_
#define __LEARN_TREES_

/*feuilles = derniers noeuds
racine
noeuds
branches
a chaque neoud y a des sous-ensmebles de graphs*/

#include <stdio.h>
#include <stdlib.h>

typedef struct	Tree
{
	int     value;
	struct	Tree *tleft; //l'arbre de gauche du noeud ou jss
	struct	Tree *tright; //l'arbre de droite du noeud ou jss
	struct	Tree *parent; //racine
	
}		        Tree;

Tree *new_tree(int x);
void clean_tree(Tree *tr);
Tree *join_tree(Tree *left, Tree *right, int node);

#endif