program CompositeSorting;

{$APPTYPE CONSOLE}

{$R *.res}

uses
  System.SysUtils;
  type
  // di C++ STRUCT
  TKaryawan = record
     NIP : string[10];
     Nama : string [50];
     Gol  : Integer;
  end;
var dtKaryawan:array[1 .. 100] of TKaryawan;

    t :TKaryawan; // Temporary
    i,j,Jumlah_data:integer;
begin
  write('Input Jumlah data Data Awal:');
  Readln(Jumlah_data);
  for i:=1 to Jumlah_data do
  begin
    write('NIP[',i,'] =:');
    Readln(dtKaryawan[i].NIP);
    write('NAMA[',i,'] =:');
    Readln(dtKaryawan[i].Nama);
    write('GOL[',i,'] =:');
    Readln(dtKaryawan[i].Gol);
    Writeln;
  end;

  for i:=1 to Jumlah_data-1 do
    for j:=i+1 to Jumlah_data do
      //Bandingin Nilai Kiri dan Kanan
      if dtKaryawan[i].NIP>dtKaryawan[j].NIP then
      begin
        // Tukar Nilai Kiri Ke Kanan Sorting By NIP
        t.NIP:=dtKaryawan[i].NIP;
        dtKaryawan[i].NIP:=dtKaryawan[j].NIP;
        dtKaryawan[j].NIP:=t.NIP;
      end;

  writeln('Result Sorting :');
  for i:=1 to Jumlah_data do
  begin
    writeln('Data[',i,'] = ',dtKaryawan[i].NIP+' '+' '+ dtKaryawan[i].Nama +' '+IntToStr(dtKaryawan[i].Gol));
  end;
  Readln;
  
end.
