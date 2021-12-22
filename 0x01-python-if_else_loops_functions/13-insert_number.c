#include "lists.h"
/**
* insert_node - inserts a node at first position.
*@head: adress of head node.
*@number: number to add
*Return: a pointer to the header.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *new_node = NULL;

	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	while (tmp)
	{
		if (tmp->n <= number)
		{
			if ((*head)->next)
			{
				tmp = tmp->next;
			}
			else
			{
				tmp->next = new_node, *head = new_node;
				return (new_node);
			}
		}
		if (tmp->n >= number)
		{
			new_node->next = tmp->next, tmp->next = new_node;
			return (new_node);
		}
	}
	return (new_node);
}
