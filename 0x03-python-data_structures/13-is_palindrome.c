#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if singly-linked list is palindrome
 * @head: head of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	unsigned int len = 1;
	listint_t *tmp;

	if (head == NULL || *head == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		tmp = tmp->next;
		len++;
	}
	return (0);
}
