#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 0 if the list does not has a cycle, 1 if it does
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == null)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
                fast = fast->next->next;
		if (slow == fast)
			return (1)
	}

	return (0);
}
