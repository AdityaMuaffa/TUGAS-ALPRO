#include <iostream> //TUGAS ALGORITMA
#include <cstring> //Muh. Fathul Aditya Muaffa
#include <conio.h>
using namespace std;


int main () {
	int a;
	char u;
	string b;
	
	
	
	cout << "======NAMA-NAMA BULAN======" << endl;
	int x;
	cout << "Tekan 'k' untuk keluar \n Tekan 'L' untuk lanjut \n\n";
	cout << "Pilihan anda :";
	cin >> u;
	cout << endl<<endl;
	
		
		while (1) {
			if (u == 'l' ) {
				int a;
				string b;
				cout << endl;
				int x;
				cout << "Masukan urutan :";
				cin >> a;
				cout << endl;
				
		switch (a) {
		case 1 :
			b = "Januari";
			break;
		case 2 :
			b = "Februari";
			break;
		case 3 :
			b = "Maret";
			break;
		case 4 :
			b = "April";
			break;
		case 5 :
			b = "Mei";
			break;
		case 6 :
			b = "Juni";
			break;
		case 7 :
			b = "Juli";
			break;
		case 8 :
			b = "Agustus";
			break;
		case 9 :
			b = "September";
			break;
		case 10 :
			b = "oktober";
			break;
		case 11 :
			b = "November";
			break;
		case 12 :
			b = "Desember";
			break;
		default :
			cout << endl << endl;
			cout << "      ERROR!!\n\n";
			exit (0);
		}
		
	
	
	
	cout << "Urutan '" << a << "' adalah " << b << endl <<endl;

	}
			else if (u == 'k') {
				cout << endl << endl;
				cout << "      Maturnuwun\n\n";
				exit (0);
			}
			
			else if (u != '\n') {
				cout << "Maaf '" << u << "' Tidak ada dimenu!!\n\n\n";
				cout << "(k/L) :";
				cin >> u;
			}
		}
		
		
		
		
return (0);
	
}
