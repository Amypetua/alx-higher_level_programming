#include <stdio.h>
#include <stdlib>
#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 0 if the list does not has a cycle, 1 if it does
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == nullptr)
		return (0);
	
	slow = list;
	fast = list->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
                fast = fast->next->next;
	}

	return (0);
}
