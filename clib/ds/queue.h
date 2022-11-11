#define TYPE int
#define INIT_CAP = 2

typedef struct _queue {
    int size = 0;
    int capacity = INIT_CAP;
    TYPE *pipe;
}Queue;

Queue* initQueue(void);

int queuesize(Queue* q);

int lput(Queue* q);

int rpop(Queue* q);

int addCapacity(Queue* q);