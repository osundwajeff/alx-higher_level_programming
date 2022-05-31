#include "lists.h"
/**
 * insert_node - inserts a node into a sorted singly linked list
 * @head: head of the list
 * @number: integer
 * Return: address of new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *a;
	listint_t *bef;

	a = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	while (a != NULL)
	{
		if (a->n > number)
			break;
		bef = a;
		a = a->next;
	}

	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = a;
		if (a == *head)
			*head = new;
		else
			bef->next = new;
	}

	return (new);
}
