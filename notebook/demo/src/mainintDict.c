#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "intDict.h"

int main()
{
	int numBuckets = 5;
	int numEntries = 10;
	Hashtable *hTable;
	int *key;
	int *value;

	hTable = createHash(numBuckets);
	key = (int *)malloc(sizeof(int) * numEntries);
	value = (int *)malloc(sizeof(int) * numEntries);
    
	printf("The value of the intDict is:\n");
	printf("(key value)\n");
    srand(time(NULL));
	for (int i = 0; i < numEntries; i++)
	{
		key[i] = rand() % 100000;
		value[i] = i;

		addEntry(hTable, key[i], value[i]);
		printf("(%d %d)\n", key[i], value[i]);
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
				printf(" (%d %d) ", p->key, p->value);
			printf("\n");
		}
		else
			printf("\n");
	}

	printf("\nHash search(even):\n");
	printf("(key value) : key -> value:\n");
	for (int i = 0; i < numEntries; i++)
	{
		if (i % 2 == 0)
		{
			int val = getValue(hTable, key[i]);
			printf("(%d  %d): -> %d \n", key[i], value[i], val);
		}
	}

	free(key);
	free(value);

	freeHash(hTable);

	return 0;
}
