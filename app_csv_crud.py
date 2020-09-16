import csv
import os

csv_filename = 'contacts.csv'
temp_filename = 'tempcontacts.csv'
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== APLIKASI KONTAK ===")
    print("[1] Lihat Daftar Kotak")
    print("[2] Buat Kontak Baru")
    print("[3] Edit Kontak")
    print("[4] Hapus Kontak")
    print("[5] Cari Kontak")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    
    if(selected_menu == "1"):
        show_contact()
    elif(selected_menu == "2"):
        create_contact()
    elif(selected_menu == "3"):
        edit_contact()
    elif(selected_menu == "4"):
        delete_contact()
    elif(selected_menu == "5"):
        search_concat()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


def show_contact():
    clear_screen()
    line_count=0
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        print(f'\t{"NO"}\t\t{"NAMA"}\t\t\t{"NO TELPON"}')
        for row in csv_reader:               
            print(f'\t{row[0]}\t\t{row[1]}\t\t\t{row[2]}')
            line_count +=1
            
    back_to_menu()
from csv import writer
def append_row(file_name, list):
    with open(file_name, 'a+', newline='') as csv_file:
        csv_writer = writer(csv_file)        
        csv_writer.writerow(list)
def create_contact():
    clear_screen()
    no = input("No urut: ")
    nama = input("Nama lengkap: ")
    telepon = input("No. Telepon: ") 
    data = [no,nama,telepon];
    append_row(csv_filename,data)
    back_to_menu()


def search_concat():
    clear_screen()
    no = input("Cari berdasrakan nomer urut> ")
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0]==no :
               print("DATA DITEMUKAN: ")
               print(f"Nama: {row[1]}")
               print(f"Telepon: {row[2]}")
                      
    back_to_menu()
    


def edit_contact():
    clear_screen()
    tempdata = [];
    no = input("Cari berdasrakan nomer urut> ")    
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        nama = input("nama baru: ")
        telepon = input("nomer telepon baru: ")        
        for row in csv_reader:
          tempdata.append(row)
  
    for data in tempdata :
        if data[0]==no :
          data[1]=nama
          data[2]=telepon
        
    with open(csv_filename, mode="w",newline='') as csv_file:        
        for newdata in tempdata:
            csv_writer = writer(csv_file)
            csv_writer.writerow(newdata)
            
    print([data])       
    back_to_menu()



def delete_contact():
    clear_screen()
    no = input("Cari berdasrakan nomer urut> ")
    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        with open(temp_filename, mode="w") as temp_file:
            temp_writer = csv.writer(temp_file)
            for row in csv_reader:
                if row[0]!=no :
                    temp_writer.writerow(row)
    os.remove(csv_filename)
    os.rename(temp_filename,csv_filename)          
    print("Data sudah terhapus")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()
