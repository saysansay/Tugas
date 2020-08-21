using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tugas1
{
    class Program
    {
        static void Main(string[] args)
        {
            
            TimeSpan jamBerangkat,diffTime,result; int totalDetik = 0;string convertDetik;
 
            int inthour;int intMinute;int intSecond;

           
            Console.WriteLine("Console Calculator Menghitung Jam Tempuh C#\r");
            Console.WriteLine("------------------------\n");

           
            Console.WriteLine("Masukan Jam Keberangkatan dengan Format hh:mm:ss, Lalu tekan Enter ");
            jamBerangkat = TimeSpan.Parse(Console.ReadLine());

            Console.WriteLine("Masukan Total Detik, Lalu tekan enter");
            totalDetik = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Pilih opsi dibawah:");
            Console.WriteLine("\ta - Hitung");
          
            Console.Write("Pilihan Anda ? ");

           
            switch (Console.ReadLine())
            {
                case "a":
                      inthour = totalDetik / 3600;
                      intMinute = (totalDetik % 3600) / 60; // totalDetik MOD 3600 DIV 60
                      intSecond = (totalDetik % 3600) % 60; // totalDetik MOD 3600 MOD 60
                      convertDetik = inthour.ToString()+ ':' + intMinute.ToString() + ':' + intSecond.ToString();
                      diffTime = TimeSpan.Parse(convertDetik);
                      result = jamBerangkat.Add(diffTime);
                    ;

                   Console.WriteLine($" Durasi : {diffTime.Hours} " + "Jam : " + ( diffTime.Minutes)+" Menit : "+(diffTime.Seconds) +" Detik"+
                       " Waktu Sampai Jam :"+(result.Hours)+ ":" + (result.Minutes) + ":" + (result.Seconds) +"");
                    break;
            }
          
            Console.Write("Silahkan tekan apa saja untuk menutup aplikasi");
            Console.ReadKey();
        } }

    }
 
