#include "lists.h"

/**
 * check_cycle - check list cycle
 * @t: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *t)
{
	listint_t *current;
	listint_t *fast;

	if (t == NULL || t->next == NULL)
		return (0);

	current = t;
	fast = t;

	while (current != NULL && fast != NULL && fast->next != NULL)
	{
		current = current->next;
		fast = fast->next->next;

		if (current == fast)
			return (1);
	}
	return (0);
}
