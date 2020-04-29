#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
  * insert_node - inserts a number into a sorted singly linked list
  * @head: head
  * @number: number
  * Return: address of new node, or NULL if it fails
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current_node = *head;

	if (head == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = current_node;
	*head = new_node;

	return (new_node);
}
