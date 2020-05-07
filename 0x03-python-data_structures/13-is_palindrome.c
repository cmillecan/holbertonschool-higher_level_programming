#include "lists.h"
listint_t *reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next;
	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (*head);
}

int is_palindrome(listint_t **head)
{
	listint_t *first = *head;
	listint_t *last = *head;

	for (; first && first->next; last = last->next)
	{
		first = first->next->next;
	}
	first = *head;
	last = reverse(&last);

	while (first && last)
	{
		if (first->n == last->n)
		{
			first = first->next;
			last = last->next;
		}
		else
			return (0);
	}
	return (1);

}
