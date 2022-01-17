#include<stdio.h>
#include<conio.h>
#include<string.h>
#define set 0.5

int main ()
{
	int alas,tinggi,luas;
	
	printf("   Menghitung luas segitiga\n\n");
	printf("Masukan alas   :");scanf("%d",&alas);
	printf("\nMasukan tinggi :");scanf("%d",&tinggi);
	
	luas=set*(alas*tinggi);
	printf("\nLuas segitiga adalah :%d",luas);
	
	return 0;
}
