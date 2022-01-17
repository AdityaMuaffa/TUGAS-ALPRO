#include <stdio.h>
#include <conio.h>
#include <string.h>

int main()
{
	
	char nikah;
	char nama [10];
	int golongan;
	
	printf("\nMasukkanNamaPegawai    :");gets (nama);
	printf("Golongan Pegawai (1\2\3) :");scanf("%d",&golongan);
	
	printf("---------------------------------------------\n");
	printf("Nama          :%s",nama);
	printf("\nGolongan    :%d",golongan);
	int tgolongan = (golongan == 1 ? 2000000 :(golongan == 2 ? 2750000 : 35000000));
	printf("\nGajiPokok   : %d",tgolongan);
	
	int bonus = (golongan == 1 ? 150000 :(golongan == 2 ? 175000 : 2000000));
	printf("\nBonus       : Rp%d",bonus);
	
	printf ("\nTotal Gaji : Rp %d", tgolongan+bonus);
	
	return 0;
}
