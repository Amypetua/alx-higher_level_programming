#include "lists.h"

/**
 * @insert_node: insert a number into a sorted singly linked list.
 * @n: integer number to insert.
 * @h: a pointer to the head of sorted singly linked list.
 *
 * Description: singly linked list node structure.
 * @Return: return the address of the new node if successful, or NULL if failed.
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)

	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;
	
	return (new);
}
