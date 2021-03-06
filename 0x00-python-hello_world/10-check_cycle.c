#include "lists.h"
/**
* check_cycle - checks if a singly linked list has a cycle in it.
*@list: header node.
*Return: 1 in case there's a cycle, 0 if not.
*/
int check_cycle(listint_t *list)
{
	listint_t *a1 = list;
	listint_t *a2 = list;
	
	if (!list)
		return (0);

	while (a2->next && a2->next->next)
	{
			a1 = a1->next;
			a2 = a2->next->next;
		if (a1 == a2)
			return (1);
	}

	return (0);
}
