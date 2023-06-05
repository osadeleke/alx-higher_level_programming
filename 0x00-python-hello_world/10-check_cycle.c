#include "lists.h"

/**
 * check_cycle - check list cycle
 * @t: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *t)
{
	listint_t *current;

	if (t->next == NULL)
		return (0);

	current = t->next;

	while (current != t)
	{
		if (current->next == NULL)
			return (0);

		current = current->next;
	}

	return (1);
}
