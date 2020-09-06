/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.xb.tugas4_2;

/**
 *
 * @author saysansay
 */
public class Papasan {
    public static void main(String[] args) {    
    int jam1,menit1,detik1,jam2,menit2,detik2;
    int jam3,menit3,detik3;
    int konvdet1,konvdet2;
    int t1,t2;
    double v1,v2,s1,s2,s3;
    int ispapasan=0;
// jam berangkat ali 
    jam1 = 8;
    menit1 =0;
    detik1=0;
    // Jam dadu berangkat dari titik B
    jam2 = 8;
    menit2 = 0;
    detik2 = 10;
    
    konvdet1 = (jam1*3600)+(menit1*60)+detik1;
    konvdet2 =(jam2*3600)+(menit2*60)+detik2;

    s2 = 1000;
    s3 = 1000;//jarak papasan
    s1 = 0;
    
    v1 = 2;
    v2 = 3;
    
    t1 = 0;
    t2 = 0;
        while (s1 < 1000) {
            s1 = s1 + v1;
            t1 = t1 + 1; //increment detik
            konvdet1 = konvdet1 + 1;
            if (t1>1){
                v1 = v1 + 0.1;//Setelah detik pertama kecepatan bertambah 0.1            
        }
        // dadu start dari titik B
        if (konvdet1>=konvdet2)
        {
            s2 = s2 - v2;//pengurangan jarak dari titik B
            t2 = t2 + 1;
            
                    
        }
        if (s2<=s1){
            ispapasan = 1;//Ali dan dadu berpapasan
            konvdet2 = konvdet2 + t2 ;// hitung detik papasan
            jam3 = (konvdet2/3600);
            menit3 = (konvdet2 % 3600)/60;
            detik3 = (konvdet2 % 3600)%60;
            s3 = s3 - s2;
            System.out.println("Ali berpapasan dengan dadu pada jark tempuh dadu "+s3);
            System.out.println("Jam "+jam3 +" Menit "+menit3 +" Detik "+detik3);
            System.exit(0);//keluar procedure
        }
           System.out.println("Detik "+t1 +" Jarak Ali "+s1 +" Jarak ");
            
    }
        if (ispapasan==0){
            jam3 = (konvdet1/3600);
            menit3 = (konvdet1 % 3600)/60;
            detik3 = (konvdet1 % 3600)%60;
            System.out.println("Ali Sudah sampai tujuan sebelum berpapasan ddengan dadu pada jark tempuh dadu "+s1);
            System.out.println("Jam "+jam3 +" Menit "+menit3 +" Detik "+detik3);
            System.exit(0);//keluar procedure
        }
 }
}
