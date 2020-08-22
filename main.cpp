#include <iostream>
#include <conio.h>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int jamAwal,menitAwal,detikAwal,totalDetik,totalDetikAwal,hasiltotalDetik,konvJam,konvMenit,konvDetik;
	string result; 
    cout<<"MASUKAN JAM KEBERANGKATAN : "<<endl;
    cout<<"Jam   = ";
    cin>>jamAwal;
    cout<<"Menit = ";
    cin>>menitAwal;
    cout<<"Detik = ";
    cin>>detikAwal;
	cout<<"Masukan Lama perjalanan dalam Detik : ";
	cin>>totalDetik;
	totalDetikAwal =(jamAwal*3600)+(menitAwal*60)+detikAwal;	
	hasiltotalDetik = totalDetikAwal + totalDetik;
	konvJam = hasiltotalDetik / 3600;
	konvMenit = (hasiltotalDetik % 3600)/60;
	konvDetik = (hasiltotalDetik % 3600)%60;
	cout<<"SAMPAI TUJUAN "<<" JAM :"<<konvJam<<" MENIT : "<<konvMenit<<" DETIK : "<<konvDetik;
	return 0;
}
