
#include <stdio.h>
#include <stdlib.h>
#include "intDict.h"


// Create hash table
Hashtable *createHash(int numBuckets)
{
    Hashtable *table=(Hashtable*)malloc(sizeof(Hashtable*));
    if(!table) {
		return NULL;
	}
    
    table->buckets=(Node**)malloc(sizeof(Node)*numBuckets);
    if(!table->buckets) {
		free(table);
		return NULL;
	}
	
    table->numBuckets=numBuckets;
	// initialize the head pointer of the bucket stack to NULL
	for(int i=0;i<table->numBuckets;i++)
		table->buckets[i] = NULL;
   
    return table;
}

void *freeHash(Hashtable *hTable)
{
   	Node *b,*p;
	for(int i=0;i<hTable->numBuckets;i++)
	{
       b = hTable->buckets[i];
	   while(b!=NULL)
	   { 
         p=b->next;
	     free(b);
		 b=p;
	   }	 
	}
	free(hTable->buckets);
	free(hTable);
}

// hash function for int keys
int inthash(int key,int  numBuckets)
{
    return key % numBuckets;
}

// Lookup  by int key
Node *searchEntry(Hashtable *hTable, int key)
{
	Node *p;
	int addr = inthash(key, hTable->numBuckets);
	p = hTable->buckets[addr];

	while(p && p->key !=key)
		p = p->next;

	return p;
}

// Add Entry to table - keyed by int
void addEntry(Hashtable *hTable, int key,int value)
{
	int addr;
	Node *p,*entry;
	p = searchEntry(hTable,key);
	if(p)
	{
		return;
	}
	else
	{   /*
          add a new item on the top of the linked list stack 
          and a pointer to the top element.  
       */
		addr =  inthash(key, hTable->numBuckets);
		entry=(Node*)malloc(sizeof(Node));
	  	entry->key = key;
		entry->value=value;
		entry->next =hTable->buckets[addr];
		hTable->buckets[addr] = entry;
	}
}

// Get by int
int getValue(Hashtable *hTable, int key)
{   
	Node *p;
	p = searchEntry(hTable,key);
	if (p)
	{
      return p->value;
	}
}