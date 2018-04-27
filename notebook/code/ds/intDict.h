
#ifndef INTDICTH
#define INTDICTH

typedef struct _node
{
	int key;
	int value;
	struct _node *next;
} Node;

typedef struct _hashtable
{ 
	int   numBuckets;
	Node **buckets; //the linked list stack 
} Hashtable;

// Create hash table
Hashtable *createHash(int numBuckets);

// free hash table
void *freeHash(Hashtable *hTable);

// hash function for int keys
int inthash(int key,int  numBuckets);

// Add Entry to table - keyed by int
void addEntry(Hashtable *hTable, int key,int value);

// Lookup  by int key
Node *searchEntry(Hashtable *hTable, int key);

// Get by int key
int getValue(Hashtable *hTable, int key);

#endif