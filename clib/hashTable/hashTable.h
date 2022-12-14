#define HASH_TABLE_CAP 7

typedef struct hashTable
{
    int * data;
    int size;
    int capacity;
}hashTable;

void hashTableInit(hashTable* h);

int insert(hashTable* h, int num);

int hashFunc(int num, hashTable* h);

void printHashTable(hashTable* h);