
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct node
{
	int key;
	int value;
	struct node *next;
} Renode;

typedef struct hashtable
{
	Renode **buckets;
} Rehashtable;

int inthash(int k,int  numBuckets)
{

    return k % numBuckets;
}

Renode *searchEntry(Rehashtable *HT, int k,int  numBuckets)
{
	Renode *p;
	int addr = inthash(k, numBuckets);
	p = HT->buckets[addr];

	while(p && p->key !=k)
		p = p->next;

	return p;
}

void addEntry(Rehashtable *HT, Renode *entry,int numBuckets)
{
	int addr;
	Renode *p;
	p = searchEntry(HT,entry->key,numBuckets);
	if(p)
	{
		free(entry);
	}
	else
	{
		addr =  inthash(entry->key, numBuckets);
		entry->next = HT->buckets[addr];
		HT->buckets[addr] = entry;
	}
}

int getValue(Rehashtable *HT, int key,int numBuckets)
{   
	Renode *p;
	p = searchEntry(HT,key,numBuckets);
	if (p)
	{
      return p->value;
	}
}

int main()
{
	int numBuckets=29;
    int numEntries=20;
    Rehashtable *HT;
	Renode **Entry;
	
    HT=(Rehashtable*)malloc(sizeof(Rehashtable*));
    HT->buckets=(Renode**)malloc(sizeof(Renode)*numBuckets);

	Entry=(Renode**)malloc(sizeof(Renode*)*20);

	for(int i=0;i<numBuckets;i++)
		HT->buckets[i] = NULL;
    
    printf("The value of the intDict is:\n");
    printf("(key value)\n");
    srand(time(NULL));
	for(int i=0;i<numEntries;i++)
	{
		Entry[i]=(Renode*)malloc(sizeof(Renode));
	  	Entry[i]->key = rand() % 100000;
		Entry[i]->value=i;
		addEntry(HT,Entry[i], numBuckets);
		printf("(%d %d)\n",Entry[i]->key,Entry[i]->value);
	}

    printf("The buckets are: \n");
	for(int i=0;i<numBuckets;i++)
	{
       Renode *s,*p;
	   s = HT->buckets[i];
	   printf("bucket %d :",i);
	   if (s)
	   {
	     for(p=s; p!=NULL; p=p->next)
	        printf(" (%d %d) ",p->key,p->value);
	     printf("\n"); 		
	   }
	   else
	    	printf("\n"); 	   
	}

    printf("Hash search(even):\n");
    printf("(key value) : key -> value:\n");
	for(int i=0;i< numEntries;i++)
	{
      if (i%2==0)
      {
        int value=getValue(HT, Entry[i]->key,numBuckets);
        printf("(%d  %d): -> %d \n",Entry[i]->key,Entry[i]->value,value);
      } 
	}
    
    for(int i=0;i<numEntries;i++)
		free(Entry[i]);
    free(Entry);
    free(HT->buckets);
    free(HT);
  	return 0;
}