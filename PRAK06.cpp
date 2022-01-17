#include <stdio.h>
#include <conio.h>
#include <string.h>

int main()
{
	int bulans, bulan;
	char nama [25];
	int tahuns, tahun;
	char alamat [75];
	int tanggals, tanggal;
	int umur;
	
	printf("\nMasukan nama anda        :");gets(nama);
	printf("\nMasukan alamat anda      :");gets(alamat);
	printf("\nMasukan tanggal lahir    :");scanf("%d",&tanggal);
	printf("\nmasukkan bulan lahir     :");scanf("%d",&bulan);
	printf("\nmasukkan tahun lahir     :");scanf("%d",&tahun);
	printf("\nmasukkan tahun sekarang  :");scanf("%d",&tahuns);
	
	umur=tahuns-tahun;
	
	printf("\n------------------------------");
	printf("\nNama                          :%s",nama);
	printf("\nAlamat                        :%s",alamat);
	printf("\nTanggal lahir	              :%d",tanggal);printf("-%d",bulan);printf("-%d",tahun);
	printf("\nUsia                          :%d",umur);
	
	return 0;
}
