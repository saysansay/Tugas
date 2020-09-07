program tugas4_1;

{$APPTYPE CONSOLE}

{$R *.res}

uses
  System.SysUtils;
var
  j1 : Integer; // Jam Awal
  m1 : Integer;//menit awal
  d1 : Integer;//Detik Awal
  j2 : Integer;//Jam berikutnya
  m2 : Integer;//menit berikutnya
  d2 : Integer;//detik berikutnya
  j3 :Integer;// Konversi Jam
  m3 :Integer;// Konversi Menit
  d3 :Integer;// Konversi Detik
  tot1,tot2 : Integer;//Konversi Jam menit kedetik
  t1,t2 : Integer;  //waktu
  v1,v2 : Double;//kecepatan karena penambahan 0.1
  s,s1 : Double;// Jarak Tempuh dipascal type data mengikuti type data lainnya
  tersalip : Boolean;

begin
  {Tugas 4 Looping}
  s:=0;
  s1 :=0;
  v1 := 2;//2 meter per detik naik 0.1 setiap 10 detik berikutnya
  v2 := 3;// 3 meter per detik;
  t1 :=0;
  t2 :=0;
  Write('Masukan Jam Ali Berangkat : ');Readln(j1);
  Write('Masukan Menit Ali Berangkat : ');Readln(m1);
  Write('Masukan Detik Ali Berangkat : ');Readln(d1);
  Write('Masukan Jam Dadu Berangkat : ');Readln(j2);
  Write('Masukan Menit Dadu Berangkat : ');Readln(m2);
  Write('Masukan Detik Dadu Berangkat : ');Readln(d2);

  tot1 :=(j1*3600)+(m1*60)+d1;// Konversi Jam keberangkatan ke detik
  tot2 :=(j2*3600)+(m2*60)+d2;//Konversi jam kedua untuk menetukan star
  while s < 1000 do // jarak tempuh 1000 m
  begin
    s := s + v1;
    t1 :=t1 + 1;
    tot1 := tot1 + 1;
    if (t1 MOD 10)=0 then // + 10 detik
       v1 := v1 + 0.1;

    if  tot1 >= tot2 then   // badu start
    begin
      s1 := s1 + v2;
      t2 := t2 + 1;
    end;
    if s1 > s then // logic tersalip
    begin
        tersalip := True; // tandai jika tersalip
        tot2 := tot2 + t2;
        j3 :=(tot2 DIV 3600);
        m3 :=(tot2 MOD 3600)DIV 60;
        d3 :=(tot2 MOD 3600)MOD 60;
        Writeln('Andi Kesalip Pada Jarak Tempuh dadu '+FloatToStr(s1)+' m');
        Writeln ('Jam : '+IntToStr(j3)+' Menit : '+IntToStr(m3)+' Detik : '+IntToStr(d3));
        Readln;
        Exit;//keluar procedure
    end
    else
        tersalip :=False;
  end;
    if tersalip = False then
    begin
           j3 :=(tot1 div 3600);
           m3 :=(tot1 MOD 3600) DIV 60;
           d3 :=(tot1 MOD 3600)MOD 60;
           Writeln ('Jarak tempuh Ali '+FloatToStr(s)+
                    ' Jam : '+IntToStr(j3)+
                    ' Menit : '+IntToStr(m3)+
                    ' Detik : '+IntToStr(m3));
           Writeln('Ali sudah sampai tujuan sebelum dadu dapat menyalip ali. Jarak tempuh dadu masih '+FloatToStr(s1)+' m');
           Writeln('Detik ke '+IntToStr(t1));
    end;
    Readln;
end.
