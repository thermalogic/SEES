#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct _node
{
	int val;
	struct _node *next;
} node;

void push(node **head, int val)
/* add a new item on the top of the linked list*/
{
	node *new_node=(node *)malloc(sizeof(node));
	new_node->val = val;
	new_node->next = *head;
	*head = new_node;
}

int pop(node **head)
{   if (*head==NULL)
        return INT_MIN;
    int popped = (*head)->val;
    node* temp = *head;  
    *head = (*head)->next;
    free(temp);
    return popped;
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
	node *stack = NULL;
  	push(&stack, 7);
	push(&stack, 9);
    push(&stack, 2);
	print_list(stack);
    printf("%d\n",pop(&stack));
    printf("%d\n",pop(&stack));
    printf("%d\n",pop(&stack));
    printf("%d\n",pop(&stack));
}
