#include "lists.h"
/**
*
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nNode;
	
	if (head == NULL)
		return (NULL);

	nNode = malloc(sizeof(listint_t));
	if (nNode == NULL)
		return (NULL);

	nNode->n = number;

	nNode->next = *head;
	*head = nNode;

	return (nNode);
}
