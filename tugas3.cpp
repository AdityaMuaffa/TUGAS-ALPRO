#include <iostream> //TUGAS ALGORITMA
#include <cmath> //Muh. Fathul Aditya Muaffa
using namespace std;



int main() {
	int a;
	char u;
	
	
	cout << "================MENU===============\n";
	cout << "1.Luas Persegi panjang\n";
	cout << "2.Keliling persegi panjang\n";
	cout << "3.Panjang diagonal persegi panjang\n";
	cout << "4.Keluar program\n";
	cout << "==================================\n";
	cout << "\n";
	
	cout << "Lanjutkan Tekan (Ya(Y)/Tidak(T)) :";
	cin >>u;
	cout <<endl;
	
	
	while (1) {
		int p, l;
		int sum;
		
		if(u == 'y') {
			cout << "Pilih menu :";
			cin >> a;
			
			switch (a) {
				case 1 :
				cout << "Panjang :";
				cin >> p;
				cout << "Lebar :";
				cin >> l;
				sum = p*l;
				cout << "Luas Persegi Panjang :" << sum;
				cout << endl<<endl;
				break;
				
				case 2  :
					cout << "Panjang :";
					cin >> p;
					cout << "lebar :";
					cin >> l;
					sum = 2*p + 2*l;
					cout << "Keliling perseegi panjang :" << sum;
					cout <<endl<<endl;
					break;
					
					case 3 :
						cout << "Panjang :";
						cin >> p;
						cout << "Lebar :";
						cin >> l;
						sum = sqrt(p*p + l*l);
						cout << "Panjang diagonal :" << sum;
						cout << endl<<endl;
						break;
						
						case 4 :
							cout << "\n\n\n";
							cout << "        program selesai      ";
							exit (0);
							default :
								cout << endl << endl;
								cout << "ERROR!!\n\n";
								exit (0);
			}
			
			

			
		} 
		else if (u == 't') {
			cout <<endl<<endl<<endl;
			cout << "=====Maturnuwun=====\n\n";
			exit (0);
		}
		
		
	
		else if(u != '\n') {
			cout << "Maaf '" << u << "' tidak terdeteksi\n\n";
			cout << "ya (y) / tidak (t) :";
			cin >> u;
		}
		
	}
	return 0;
	}
	
