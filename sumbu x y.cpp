#include <stdio.h>
#include <conio.h>
#include <string.h>

int main()
{
	int ao, bo;
	int aa, ba;
	
	printf("-----------------------\n");
	printf(" Mencari Titik Tengah\n\n");
	
	printf("Masukkan x Koordinat A :");scanf("%d",&aa);
	printf("Masukkan Y Koordinat A :");scanf("%d",&ao);
	printf("Masukkan X Koordinat B :");scanf("%d",&ba);
	printf("Masukkan Y Koordinat B :");scanf("%d",&bo);
	printf("\n\n");
	
	int absis, ordinat, pencerminan;
	
	absis=(aa+bo)/2;
	ordinat=(ao+bo)/2;
	
	printf("Absis     :%d",absis);printf("\n");
	printf("ordinat   :%d",ordinat);
	printf("\n\n");
	
	pencerminan=(absis+ordinat)/2;
	
	printf(" Pencerminan sumbu X dan Y :%d", pencerminan);printf("\n\n");
	
	return 0;
}
