#include<stdio.h>
#include<conio.h>
void main()
{
char a,e,i,o,u,tmp;
clrscr();
printf("enter the details:");
scanf("%c",&tmp);
if(tmp=='a'||tmp=='e'||tmp=='i'||tmp=='o'||tmp=='u')
{
printf("the %c is vowel:");
}
else
printf("the %c is consonant:");
getch();
}
