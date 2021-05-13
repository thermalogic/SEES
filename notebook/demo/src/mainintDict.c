#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "intDict.h"

int main()
{
	int key[8]={36,18,72,43,6,10,5,15};
	char value[8]={'A','B','C','D','E','F','G','H'};

   	int numBuckets = 8;
	int numEntries = 8;
	Hashtable *hTable;

	hTable = createHash(numBuckets);
	for (int i = 0; i < numEntries; i++)
	{
		addEntry(hTable, key[i], value[i]);
		printf("(%d %c)\n", key[i], value[i]);
	}

	printf("\nThe buckets(the linked list stack) are: \n");
	for (int i = 0; i < hTable->numBuckets; i++)
	{
		Node *b, *p;
		b = hTable->buckets[i];
		printf("bucket %d :", i);
		if (b)
		{
			for (p = b; p != NULL; p = p->next)
				printf(" (%d %c) ", p->key, p->value);
			printf("\n");
		}
		else
			printf("\n");
	}

	printf("\nHash search:");
    int curkey=18;
    char curval = getValue(hTable,curkey);
	printf("%d -> %c \n", curkey,curval);

	freeHash(hTable);
	return 0;
}
