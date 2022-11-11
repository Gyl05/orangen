#include<stdio.h>
#include<stdlib.h>
#define TYPE int


typedef struct treenode{
    TYPE val;
    struct treenode *left;
    struct treenode *right;
}treeNode;

void printNode(treeNode* root);

void addChildren(treeNode* root, TYPE lv, TYPE rv);
