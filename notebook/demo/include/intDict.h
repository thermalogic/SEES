#ifndef INTDICT_H
#define INTDICT_H

typedef struct _node
{
	int key;
	char value;
	struct _node *next;
} Node;

typedef struct _hashtable
{
	int numBuckets;
	Node **buckets; // the linked list
} Hashtable;

// Create hash table
Hashtable *createHash(int numBuckets);

// free hash table
void *freeHash(Hashtable *hTable);

// hash function for int keys
int inthash(int key, int numBuckets);

// Add Entry to table - keyed by int
void addEntry(Hashtable *hTable, int key, char value);

// Lookup  by int key
Node *searchEntry(Hashtable *hTable, int key);

// Get by int key
char getValue(Hashtable *hTable, int key);

#endif
