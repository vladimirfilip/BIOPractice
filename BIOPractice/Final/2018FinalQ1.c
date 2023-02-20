#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAXLINES 1000
#define MAXLEN 1000

char** split(char *s);
int strcount(char *s);
char* getsegment(char* s, int start, int end);

int getline(char s[], int lim)
{
    int i, c;
    for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; i++)
    {
        s[i] = c;
    }
    s[i] = '\0';
    return i;
}

int* getedgedata(char* s)
{
    int* result = (int*) malloc(3 * sizeof(int));
    char d[MAXLEN];
    int i, j;
    for (i = 0, j = 0; i < strlen(s); i++, j++)
    {
        if (s[i] == ' ')
        {
            d[j] = '\0';
            *result++ = atoi(d);
            j = -1;
            continue;
        }
        d[j] = s[i];
    }
    d[j] = '\0';
    *result++ = atoi(d);
    return result - 2;

}

int main(int argc, char const *argv[])
{
    char line[MAXLEN];
    getline(line, MAXLEN);
    int v = atoi(line);
    while (true)
    {
        getline(line, MAXLEN);
        if (strcmp(line, "-1 -1 -1") == 0)
            break;
        int* data = getedgedata(line);
        int i = 0;
        while (i++ < 3)
            printf("%d ", *data++);
        printf("\n");
    }
}
