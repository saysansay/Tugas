program Sorting;

{$APPTYPE CONSOLE}

{$R *.res}

uses
  System.SysUtils;
{Refrensi Web : Damas Amirul Karim}
var Data:array[1 .. 5] of integer;
  i,j,t,Jumlah_data:integer; // variable t untuk temporary result
Begin
  writeln('Input Jumlah data Data Awal:');
  Readln(Jumlah_data);
  for i:=1 to Jumlah_data do
  begin
    write('Data[',i,'] =:');
    Readln(Data[i]);
  end;

  for i:=1 to Jumlah_data-1 do
    for j:=i+1 to Jumlah_data do
      //Bandingin Nilai Kiri dan Kanan
      if Data[i]>Data[j] then
      begin
        // Tukar Nilai Kiri Ke Kanan
        t:=Data[i];
        Data[i]:=Data[j];
        Data[j]:=t;
      end;

  writeln('Hasil:');
  for i:=1 to Jumlah_data do
  begin
    writeln('Data[',i,'] = ',Data[i]);
  end;
  Readln;
end.
