#include <stdio.h>
#include <stdlib.h>

typedef struct _node
{
	int val;
	struct _node *next;
} node;

void push(node **head, int val)
/*Adding an item to the end of the list*/
{
	node *new_node  = (node *)malloc(sizeof(node));
	new_node->val = val;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
	}
	else
	{
		node *current=*head;
		while (current->next != NULL)
		{
			current = current->next;
		}
		current->next = new_node;
	}		
}

void print_list(node *head)
{
	node *current = head;
	while (current != NULL)
	{
		printf("%d\n", current->val);
		current = current->next;
	}
}

int main()
{
	node *test_list = NULL;
	push(&test_list, 8);
    push(&test_list, 88);
	print_list(test_list);
}
