#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: the pointer to head oflinked list
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *hall = list;
	listint_t *oats = list;

	if (!list)
		return (0);

	while (hall && oats && oats->next)
	{
		hall = hall->next;
		oats = oats->next->next;
		if (hall == oats)
			return (1);
	}

	return (0);
}
