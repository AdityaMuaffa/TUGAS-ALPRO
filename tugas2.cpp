#include <iostream> //TUGAS ALGORITMA
using namespace std; //Muh. Fathul Aditya Muaffa



int main() {
	int a;
	char u;
	string b;
	cout << "======MENU======\n";
	cout << "1.BACA DATA\n";
	cout << "2.CETAK DATA \n";
	cout << "3.UBAH DATA \n";
	cout << "4.HAPUS DATA \n";
	cout << "5.KELUAR PROGRAM\n";
	cout << "=================\n";


	cout << "Lanjutkan Tekan (Ya(Y)/Tidak(T)) :";
	cin >> u;
	cout << endl <<endl;
	
	
	while(1) {
		if(u == 'y') {
			int a;
			string b;
			
			cout << "Pilihan anda :";
			cin >> a;
			switch (a) {
				case 1 :
					b = "Anda memilih CETAK DATA!";
					break;
					case 2:
						b = "Anda memilih CETAK DATA!";
						break;
						case 3:
							b = "Anda memilih UBAH DATA!";
							break;
							case 4 :
								b = "Anda memilih HAPUS DATA!";
								break;
								case 5:
									cout <<endl<<endl<<endl;
									cout << "     Program selesai";
									exit(0);
									default:
										cout << endl << endl;
										cout << "      ERROR!!\n\n";
										exit (0);
			}


			cout << b;
			cout << endl << endl;
		}
		
		
	else if (u == 't') {
			cout <<endl<<endl<<endl;
			cout << "=====Maturnuwun=====\n\n";
			exit (0);
		}
			else if (u != '\n') {
			cout << "Ya (y) / Tidak (t) :";
			cin >> u;
			cout <<endl<<endl;
		}
		
	}

	return 0;

 }
