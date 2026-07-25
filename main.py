import pandas as pd
import matplotlib.pyplot as plt
import csv

csvpath = "patient.csv"

#print menu
print("="*10, "NOVACARE HOSPITAL MANAGEMENT SYSTEM", "="*10)
print("~ please select an option ~")
print("1. Display All Records ")
print("2. Add a New Patient Record ")
print("3. Search Patient with ID")
print("4. Delete Patient Record ")
print("5. Calculate Bill ")
print("6. Display Graph ")
print("7. Exit Program ")
print("8. Register/update your hospital details ")
print("="*57)

choice = int(input("Enter your choice: "))

def display_records():
	df = pd.read_csv(csvpath)
	print("\nPatient Records")
	print(df)

def add_patient():
	df = pd.read_csv(csvpath)

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
	df.to_csv(csvpath, index=False)
	print("\nPatient Successfully Added")

def search_patient(pid):
	df = pd.read_csv(csvpath)
	print(df.loc[int(pid-100)].to_string())

def delete_patient():
	df = pd.read_csv(csvpath)
	pid = int(input("Enter the patient ID for the patient that you want to delete: "))
	print("Are you sure you want to delete patient", pid, "?")
	response = input("Enter yes or no to continue: ")

	if response == "no":
		return True
	
	newdf = df.drop(pid-100, axis=0)
	print("Successfully deleted patient", pid)
	newdf.to_csv(csvpath, index=False)
	
	
#def calc_bill():
# here, lets do bill = consultation fee + room charge (if serious disease) + medicine charge.
# medicine charge will be asked by the user, while consulation and room charge will be automatic.


def display_graph():
	df = pd.read_csv(csvpath)
	diseases_count = df["Diseases"].value_counts()
	
	plt.figure(figsize=(8,5))
	plt.bar(diseases_count.index, diseases_count.values)
	
	plt.title("Number of Patient for Each Diseases")
	plt.xlabel("Diseases")
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
	print("Thanks for using NovaCare Hospital System, Have a Nice Day ")


if choice == 1:
	display_records()
elif choice == 2:
	add_patient()
elif choice == 3:
	# later, also add the ability to search by name
	pid = int(input("Enter the patient ID to search: "))
	search_patient(pid)
elif choice == 4:
	delete_patient()
elif choice == 5:
	calc_bill()
elif choice == 6:
	display_graph()
elif choice == 7:
	exit_program()
elif choice == 8:
	print("work in progress, will prolly be done by morning, i hope.")
else:
	print("Please enter a valid choice.")
