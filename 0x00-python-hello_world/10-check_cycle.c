#include "lists.h"

/**
 * check_cycle - Checks if a linked list contains a cycle.
 *
 * @list: input linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *pev, *H;

	if (list == NULL || list->next == NULL)
		return (0);

	pev = list->next;
	H = list->next->next;

	while (pev && H && H->next)
	{
		if (pev == H)
			return (1);

		pev = pev->next;
		H = H->next->next;
	}
	return (0);
}
