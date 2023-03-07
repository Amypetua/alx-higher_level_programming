#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 0 if the list does not has a cycle, 0 if it does
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *faster = list;

	if (!list)
		return (0);

	while (slow && faster && faster->next)
	{
		slow = slow->next;
		faster = faster->next->next;
		if (slow == faster)
			return (1);
	}

	return (0);
}
