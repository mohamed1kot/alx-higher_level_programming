#include "lists.h"

/**
 * insert_node -  inserts a number into a sorted singly linked list.
 *
 * @head : input linked list.
 * @number : number will be insert it.
 *
 * Return: the address of the new node, or NULL if it failed.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;

	new = malloc(sizeof(listint_t));
	if (!new || !head)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else if (number < current->n)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		while (current->next)
		{
			if (number > current->next->n)
			{
				current = current->next;
			}
			else
				break;
		}
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
