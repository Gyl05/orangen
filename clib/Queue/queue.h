#include <bool.h>

typedef struct _queue_node{
    int data;
    struct _queue_node* next; // 指向下一个队列元素
}QueueNode;


typedef struct _queue{
    QueueNode* head;
    QueueNode* tail;
    int size;
}Queue;


Queue* InitQueue(Queue* pq);

void EnQueue(Queue* pq, int elem);

void DeQueue(Queue* pq);

bool QueueEmpty(Queue* pq);

