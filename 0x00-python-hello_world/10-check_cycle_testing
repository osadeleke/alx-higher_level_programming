#include "lists.h"

/**
 * check_cycle - check list cycle
 * @t: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *t)
{
	listint_t *current;
	listint_t *cycle;

	cycle = t;
	current = t;
	while (cycle != NULL && !t->next)
	{
		if (cycle->next == cycle)
		{
			cycle = cycle->next;
			continue;
		}

		if (current->next == cycle)
			return (0);
		else if (current->next == NULL)
			return(1);
		else
			current = current->next;
	}

	return (1);






	/**if (t == NULL || t->next == NULL)
		return (0);

	current = t->next;

	while (current != t)
	{
		if (current->next == NULL)
			return (0);

		current = current->next;
	}
	return (1);**/
}
