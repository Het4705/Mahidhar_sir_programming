#include<stdio.h>
#include<string.h>
int main()
{
    char word[100];
    char sen[100];
    printf("Enter Word:");
    scanf("%s",word);
    printf("Enter Sentence:");  
    scanf("%[^\n]",sen);

    printf("word:%s\n",word);
    printf("sen:%s\n",sen);

    return 0;
}