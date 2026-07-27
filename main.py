import pandas as pd
import matplotlib.pyplot as plt

#print menu
print("="*10, "NOVACARE HOSPITAL MANAGEMENT SYSTEM", "="*10)
print("~ please select an option ~")
print("1. Display All Records ")
print("2. Add a New Patient Record ")
print("3. Search Patient with ID")
print("4. Delete Patient Record ")
print("5. Calculate Bill ")
print("6. Display Graphs ")
print("7. Exit Program ")
print("="*57)

choice = int(input("Enter your choice: "))

def display_records():
	df = pd.read_csv("patient.csv")
	print("\nPatient Records")
	print("\n" + "-"*70)
	print(df)
	print("-"*70)

def add_patient():
	df = pd.read_csv("patient.csv")

	pid = int(input("Patient ID: "))
	name = input("Name: ")
	age = int(input("Age: "))
	gender = input("Gender: ")
	diseases = input("Diseases: ")
	doctor = input("Doctor: ")
	bill = int(input("Bill: "))

	new_patient = {"Patient_ID": pid, "Name": name, "Age": age, "Gender": gender, "Diseases": diseases, "Doctor": doctor, "Bill": bill}

	df.loc[len(df)] = new_patient
	df.to_csv("patient.csv", index=False)
	print("\nPatient Successfully Added.")

def search_patient():
	df = pd.read_csv("patient.csv")
	pid = int(input("Enter the patient ID to search: "))

	patient = df.loc[int(pid-101)]

	print()
	print("Found Patient Successfully.")
	print("-"*25)
	print(patient)
	print("-"*25)


def delete_patient():
	df = pd.read_csv("patient.csv")
	
	print()
	pid = int(input("Enter the Patient ID for the Patient That You Want to Delete: "))
	print("Are You Sure You Want to Delete Patient", pid, "?")
	response = input("Enter Yes or No to Continue: ")

	if response == "no":
		return True

	
	newdf = df.drop(pid-101, axis=0)
	newdf.to_csv("patient.csv", index=False)
	print("Successfully Deleted the Patient", pid)


def calc_bill():
	df = pd.read_csv("patient.csv")
	pid = int(input("Enter the Patient ID: "))

	print("The Bill to Pay for This Patient Is:", df['Bill'][pid-101], "/-")


def display_graph():
	df = pd.read_csv("patient.csv")
	diseases_count = df["Diseases"].value_counts()
	
	plt.figure(figsize=(8,5))
	plt.bar(diseases_count.index, diseases_count.values)
	
	plt.title("Number of Patient for Each Disease")
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
	print("Please Enter a Valid Choice.")
