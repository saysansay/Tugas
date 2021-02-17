#include <iostream>
#include <conio.h>
using namespace std;
/* Syarat dan Ketentuan Menggunakan Source Ini Jika Anda Menggunakan Source ini bearti anda setuju untuk masuk kelas TI */

int main(int argc, char** argv) {
	int jamA,menitA,detikA,totalDetikA;
	int jamB,menitB,detikB,totalDetikB;
	int resultPapasan,resultJarak,PapasanAli,PapasanBadu,resultJam,resultMenit,resultDetik;
	
	
	int t1,t2 ;//Waktu A dan B
	int s1,s2;// Jarak Tempuh
	int v1,v2 ; //kecepatan
	int start,papasan =0;// Start ali dan Papasan
	string result; 
	
    cout<<"MASUKAN JAM KEBERANGKATAN ALI : "<<endl;
    cout<<"Jam   = ";
    cin>>jamA;
    cout<<"Menit = ";
    cin>>menitA;
    cout<<"Detik = ";
    cin>>detikA;
    cout<<"MASUKAN JAM KEBERANGKATAN BADU : "<<endl;
    cout<<"Jam   = ";
    cin>>jamB;
    cout<<"Menit = ";
    cin>>menitB;
    cout<<"Detik = ";
    cin>>detikB;
   // s=0;
    s1=0; //const jarak tempuh ali
    s2 =0;//const jarak tempuh badu
    t1 =0; //waktu awal ali
    t2 =0;//waktu awal badu
    v1 =3;//kecepatan rata-rata /permeter ali
    v2 =2;//kecepatan rata-rata /permeter badu;
	totalDetikA =(jamA*3600)+(menitA*60)+detikA;
	totalDetikB =(jamB*3600)+(menitB*60)+detikB;
	
	for (s1;s1<900;s1++)
	{
		s1= s1 + v1;
		t1=t1+1;
		totalDetikA = totalDetikA + 1;
		if (totalDetikA==totalDetikB)
		{
			start =1;
		}
		
		if(start==1)
		{
			s2 = s2 + v2;
			t2=t2+1;
			totalDetikB = totalDetikB + 1;
			resultJarak = s1+s2;
			if (resultJarak>=900)
			{
			papasan=1;
			PapasanAli = s1;
			PapasanBadu = s2;
			break;
			}
			else
			{
				papasan=0;
			}
		}	
	}
	
		if (papasan==1)
		{
			resultJam = totalDetikB / 3600;
			resultMenit = (totalDetikB % 3600)/60;
			resultDetik = (totalDetikB % 3600)%60;		
			cout<<"Ali dan Badu Papasan Jam : "<< resultJam <<" Menit : "<< resultMenit <<" Detik : "<< resultDetik <<" Dengan Jarak Tempuh Ali : "<< PapasanAli <<" Dan Jarak Tempuh Badu :"<< PapasanBadu << endl;
		}
		else
		{
			cout<<" Ali dan Badu tidak Berpapasan, Silahkan Cek inputan!"<<endl;
		}
		

	return 0;
}
