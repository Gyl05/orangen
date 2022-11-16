#include<stdio.h>
#include<stdbool.h>
#define INIT_SIZE 5

typedef struct _queue{
	int cap; //capacity
	int front;
	int rear;
	int* data; // store int elements
}_queue;

typedef _queue* Queue;

bool initQueue(Queue q);

bool qEmpty(Queue q);

bool qFull(Queue q);

bool enQueue(Queue q, int elem);

int deQueue(Queue q);
