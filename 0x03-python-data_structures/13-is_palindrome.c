#include "lists.h"

/**
 * palindrome - check if this string is palindrome or not
 *
 * @top : input
 * @next : input
 *
 * Return: 0 or 1
*/

int palindrome(listint_t **top, listint_t *next)
{
	int result = 0;

	if (next == NULL)
		return (1);
	if (palindrome(top, next->next) && ((*top)->n == next->n))
		result = 1;

	*top = (*top)->next;
	return (result);
}

/**
 * is_palindrome - check if this string is palindrome or not
 *
 * @head : linked list.
 *
 * Return: 1 or 0
*/

int is_palindrome(listint_t **head)
{
	return (palindrome(head, *head));
}

