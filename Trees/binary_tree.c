#include "binary_tree.h"

Tree	*new_tree(int x)
{
	Tree *tr;
	if(!(tr = malloc(sizeof(*tr))))
		return (NULL);
	tr->value = x;
	tr->tleft = NULL;
	tr->tright = NULL;
	tr->parent = NULL;
	printf("create tree for tr->value = %d\n", tr->value);

	return(tr);
}

void	print_tree_prefix(Tree *tr)
{
	if(tr == NULL)
		return;
	if(tr->parent)
		printf("(%d) -> %d, tr->parent->value, tr->value");
	else
		printf("(%d)\n", tr->value);
	if(tr->tleft)
		print_tree_prefix(tr->tleft);
	if(tr->tright)
		print_tree_prefix(tr->tright);
}

Tree *join_tree(Tree *left, Tree *right, int node) //je rattache un arbre de gauche avec un arbre de droite avec "node" qui est le noeud au dessus 
{
	Tree *tr;
	tr = new_tree(node);
	tr->tleft = left;
	tr->tright = right;
	if (left)
		left->parent = tr;
	if (right)
		right->parent = tr;
	return(tr);
}

void clean_tree(Tree *tr)
{
	if(tr == NULL)
		return;
	printf("tree free for tr->value = %d\n", tr->value);
	clean_tree(tr->tleft); //a chaque fois descend plus bas dans l'arbre de gauche, jusqua arriver au plus bas
	clean_tree(tr->tright);
	free(tr); //ici premier noeud qui est free est le plus bas
}

int		main()
{
	//Tree *arbre;
	//arbre = join_tree(new_tree(2), new_tree(4), 6);//la je crée un arbre avec racine 6 qui join un arbre 2 (y a que 2 dedans), et un arbre 4 (pareil y a pas denfants, que le 4)
	Tree *arbre2;
	arbre2 = join_tree(join_tree(new_tree(8), new_tree(3), 2), new_tree(4), 6);
	print_tree_prefix(arbre2);
	clean_tree(arbre2);
	//clean_tree(arbre);
}

