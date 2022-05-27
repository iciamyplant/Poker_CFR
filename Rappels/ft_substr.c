#include <stdio.h>
#include <stdlib.h>

char *ft_substr(char const *s, unsigned int start, size_t len)
{
    char *s2;
    s2 = NULL;
    int i = start;
    int j = 0;

    if (!(s2 = malloc(sizeof(char) * len +1)))
        return(NULL);
    while (s[i + j])
    {
        s2[j] = s[i + j];
        if (j == len)
            break;
        j++;
    }
    s2[j] = '\0';
    return (s2);
}


int main()
{
    printf("result = %s\n", ft_substr("hello", 1, 3));
    //printf("i = %d", i);
}