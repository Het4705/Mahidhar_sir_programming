#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node *left;
    struct node *right;
} node;

node *create();
void printTreeStructure(node *root, int level);
void preOrderTraverse(node *root);
int deleteNode(int target, node *root);

int max(int a, int b)
{
    return a > b ? a : b;
}

int height(node *root)
{
    if (!root)
    {
        return 0;
    }
    else
    {
        return 1 + max(height(root->left), height(root->right));
    }
}

void printCurrentLevel(node *root, int level)
{
    if (!root)
    {
        return;
    }
    else
    {
        if (level == 1)
        {
            printf("%d ", root->data);
        }
        else
        {
            printCurrentLevel(root->left, level - 1);
            printCurrentLevel(root->right, level - 1);
        }
    }
}

void helpFindDiameter(node *root,int *diameter)
{
    if (!root)
    {
        return ;
    }
    else{
        int lsh=(height(root->left));
        int rsh=(height(root->right));
        int temp=lsh+rsh+1;
        if (temp>*diameter)
        {
            *diameter=temp;
        }
        helpFindDiameter(root->left,diameter);
        helpFindDiameter(root->right,diameter);
    }

}

int findDiameter(node *tree)
{
    int d = 0;
    helpFindDiameter(tree,&d);
    return d;
}
int levelOrder(node *root)
{
    int h = height(root);
    for (int i = 1; i <= h; i++)
    {
        printf("Level %d:", i);
        printCurrentLevel(root, i);
        printf("\n");
    }
}

// main
int main()
{
    node *tree = create();
    printf("\n");
    printTreeStructure(tree, 0);
    printf("\ndiameter:%d\n",findDiameter(tree));

    // printf("max height:%d ", height(tree));
    levelOrder(tree);

    // if (deleteNode(2, tree) == 1)
    // {
    //     printf("Node Deleted SuccessFully");
    // }
    // else
    // {
    //     printf("Node is not Found");
    // }
    // printTreeStructure(tree, 0);

    return 0;
}

node *create()
{
    node *new1 = (node *)malloc(sizeof(node));
    if (!new1)
    {
        printf("No Enough Space");
        return NULL;
    }
    else
    {
        int data;
        int option;

        printf("Enter Data:");
        scanf("%d", &data);
        new1->data = data;

        printf("Enter 1 to insert left child of %d else -1: ", data);
        scanf("%d", &option);
        if (option == 1)
        {
            new1->left = create();
        }
        else
        {
            new1->left = NULL;
        }

        printf("Enter 1 to insert right child of %d else -1: ", data);
        scanf("%d", &option);
        if (option == 1)
        {
            new1->right = create();
        }
        else
        {
            new1->right = NULL;
        }
        return new1;
    }
}

//& we can similary do search operation too ..

int deleteNode(int target, node *root)
{
    if (!root)
    {
        return -1; //^ Node not found
    }

    //^ Check if the current node has the target value
    if (root->data == target)
    {
        //& Check and delete the left child
        if (root->left)
        {
            deleteNode(root->left->data, root->left);
        }

        //^ Check and delete the right child
        if (root->right)
        {
            deleteNode(root->right->data, root->right);
        }

        free(root);
        return 1; //& Node deleted successfully
    }
    else
    {
        //* Check if the left child has the target value
        if (root->left && root->left->data == target)
        {
            //^ Check and delete the left child's left child
            if (root->left->left)
            {
                deleteNode(root->left->left->data, root->left->left);
            }

            //^ Check and delete the left child's right child
            if (root->left->right)
            {
                deleteNode(root->left->right->data, root->left->right);
            }

            //! Free the memory of the left child
            free(root->left);
            root->left = NULL;

            return 1; //* Node deleted successfully
        }

        // Check if the right child has the target value
        if (root->right && root->right->data == target)
        {
            // Check and delete the right child's left child
            if (root->right->left)
            {
                deleteNode(root->right->left->data, root->right->left);
            }

            // Check and delete the right child's right child
            if (root->right->right)
            {
                deleteNode(root->right->right->data, root->right->right);
            }

            // Free the memory of the right child
            free(root->right);
            root->right = NULL;

            return 1; // Node deleted successfully
        }

        // Recursively search in the left and right subtrees
        int leftResult = deleteNode(target, root->left);
        int rightResult = deleteNode(target, root->right);

        // Return 1 if the target was found in either subtree
        return (leftResult == 1 || rightResult == 1) ? 1 : -1;
    }
}

void printTreeStructure(node *root, int level)
{
    if (root == NULL)
    {
        return;
    }

    //! Print right subtree with increased level
    printTreeStructure(root->right, level + 1);

    //& Print current node with appropriate indentation
    for (int i = 0; i < level; i++)
    {
        printf("    ");
    }
    printf("%d\n", root->data);

    //* Print left subtree with increased level
    printTreeStructure(root->left, level + 1);
}

void preOrderTraverse(node *root)
{
    if (!root)
    {
        printf("Null");
        return;
    }
    printf("%d ", root->data);

    preOrderTraverse(root->left);
    preOrderTraverse(root->right);
}
