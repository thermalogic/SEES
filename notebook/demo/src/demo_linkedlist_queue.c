#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct _node
{
	int val;
	struct _node *next;
} node;

void push(node **head, node **tail, int val)
/*Adding an item to the end of the list*/
{
	node *new_node  = (node *)malloc(sizeof(node));
	new_node->val = val;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
        *tail=new_node;
	}
	else
	{
        (*tail)->next = new_node;
        *tail = new_node;
    }		
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
	node *queue = NULL;
    node *tail = NULL;

    push(&queue, &tail,2);
    push(&queue, &tail,4);
    push(&queue, &tail,6);
    push(&queue, &tail,8);
    print_list(queue);
    printf("%d\n",pop(&queue));
    printf("%d\n",pop(&queue));
    printf("%d\n",pop(&queue));
    printf("%d\n",pop(&queue));
    printf("%d\n",pop(&queue));
    
}
