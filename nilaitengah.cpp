#include <iostream>
#include <conio.h>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */


int main(int argc, char** argv) {
	int b1,b2,b3,max,min,median;
	cout<<"masukan  bilangan bulat pertama= ";cin>>b1;   
	cout<<"masukan  bilangan bulat kedua= ";cin>>b2;
	cout<<"masukan  bilangan bulat ketiga= ";cin>>b3;
	if((b1>b2)&&(b1>b3))
	{
      max = b1;
	}else
		if((b2>b1)&&(b2>b3))
	{
      max = b2;
	}else
		if((b3>b1)&&(b3>b2))
	{
      max = b3;
	}
		
	if((b1<b2)&&(b1<b3))
	{
      min = b1;
	}else
		if((b2<b1)&&(b2<b3))
	{
      min = b2;
	}else
		if((b3<b1)&&(b3<b2))
	{
      min = b3;
	}
	// Coba Cari nilai tengah dengan membanding bilangan dengan nilaimax dan nilaimin	
	if ((b1>min)&&(b1<<max)){
		median = b1;
	}  else
	if ((b2>min)&&(b2<<max)){
		median = b2;
		
	}else
	   if ((b3>min)&&(b3<<max)){
	   	 median = b3;
	   }
	
	cout<<"Nilai Terkecil = "<<min <<endl;
	cout<<"Nilai Tengah = "<<median <<endl;
	cout<<"Nilai Terbesar =  "<<max<<endl;
	return 0;
}
