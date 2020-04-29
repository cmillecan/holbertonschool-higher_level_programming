#include "lists.h"

/**
  * insert_node - inserts a number into a sorted singly linked list
  * @head: head
  * @number: number
  * Return: address of new node, or NULL if it fails
*/

listint_t *insert_node(listint_t **head, int number)
{
	listin_t *new_node = malloc(sizeof(listint_t));

	if (head == NULL)
		return (NULL);

	new_node->data = number;
	new_node->next = head;
	head = new_node;

	return (head);
}
