import pandas as pd
import matplotlib.pyplot as plt
import csv

#print menu
print("-"*10, "HOSPITAL MANAGEMENT SYSTEM", "-"*10)
print("~ please select an option ~")
print("1. Display All Records ")
print("2. Add a New Patient Record ")
print("3. Search Patient with ID")
print("4. Delete Patient Record ")
print("5. Cialculate Bill ")
print("6. Display Graph ")
print("7. Exit Program ")
print("-"*20)

choice = int(input("Enter your choice: "))

def display_records():
	df = pd.read_csv("patient.csv")
	print("\nPatient Records")
	print(df)

def add_patient():
	try:
		pid = int(input("Patient ID: "))
	except:
		print("Please enter a valid value. PID can only be an integer value.")
	name = input("Name: ")
	age = int(input("Age: "))
	gender = input("Gender: ")
	diseases = input("Diseases: ")
	doctor = input("Doctor: ")
	bill = int(input("Bill: "))

	new_patient = {"Patient_ID": pid, "Name": name, "Age": age, "Gender": gender, "Diseases": diseases, "Doctor": doctor, "Bill": bill}

	df.loc[len(df)] = new_patient
	df.to_csv("patient.csv", index=False)
	print("\nPatient Successfully Added")

#def search_patient():					#ye tu karegi tulip
#def delete_patient():					#ye tu karegi tulip
#def calc_bill():						#ye tu karegi tulip
def display_graph():
	df = pd.read_csv("patient.csv")
	diseases_count = df["Diseases"].value_counts()
	
	plt.figure(figure=(8,5))
	plt.bar(diseases_count.index, diseases_count.values)
	
	plt.title("Number of Patient for Each Diseases")
	plt.xlabel("Dieases")
	plt.ylabel("Number of patients")

	plt.show()


	doctor_count = df["Doctor"].value_counts()
	plt.figure(figsize=(8,5))
	plt.bar(doctor_count.index, doctor_count.values)

	plt.title("Number of Patient Treated by Each Doctor")
	plt.xlabel("Doctor")
	plt.ylabel("Number of Patients")

	plt.show()


def exit_program():
	print("Thank You")


if choice == 1:
	display_records()
elif choice == 2:
	add_patient()
elif choice == 3:
	search_patient()
elif choice == 4:
	delete_patient()
elif choice == 5:
	calc_bill()
elif choice == 6:
	display_graph()
elif choice == 7:
	exit_program()
else:
	print("Please enter a valid choice.")
