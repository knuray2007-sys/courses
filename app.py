from database import create_tables
from models import register_user, add_course, enroll_user_in_course

create_tables()

def main():
     while True:
         print("\n---Onlsyn Oyrenme Platformasi ---")
         print("1.Qeydiyyat")
         print("2.Kurs elave et")
         print("3.Kurs qosul")
         print("4.Cixis")

         choice = input("Secim: ")

         if choice == "1":
             username = input("Istifadeci adi: ")
             password = input("Sifre: ")
             if register_user(username, password ):
                 print("Qeydiyyat ugurludur!")
             else:
                 print('Qeydiyyat alinmadi!')

         elif choice == "2":
             name = input("Kurs adi:")
             description = input("Tesvir: ")
             if add_course(name, decription ):
                 print("Kurs elave olundu!")
             else:
                  print("Kurs elave olundu!")
         elif choice == "3":
             try:
                 user_id = int(input("Istifadeci ID: "))
                 course_id = int(input("Kurs ID:"))
                 if enroll_user_in_course(user_id, course_id):
                     print("Kursa qosuldunuz!")
                 else:
                     print("Qosulmaq alinmadi!")
             except ValueError:
                 print("ID- ler yalniz reqem ola biler!")
         elif choice =="0":
             print("Cixilir...")
         else:
             print("Yanlis secim!")
if __name__ == "__main__":
    main()
