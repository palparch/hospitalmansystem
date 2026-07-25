import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime

# add the functionality to handle the error if the csv doesnt exist

csvpath = "patient.csv"
csvpathdoc = "doctors.csv"
csvpathhospital = "hospital.csv"

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
print("8. Register/update Your Hospital Details ")
print("9. Register/update a Doctor")
print("="*57)

choice = int(input("Enter your choice: "))

def display_records():
	df = pd.read_csv(csvpath)
	print("\nPatient Records")
	print(df)

def add_patient():
	df = pd.read_csv(csvpath)

	try:
		pid = int(input("Patient ID: ")) # auto generate it, dont trust the user
	except:
		print("Please enter a valid value. PID can only be an integer value.")
	name = input("Name: ")
	age = int(input("Age: "))
	gender = input("Gender: ")
	diseases = input("Diseases: ") # maybe list diseases first 
	doctor = input("Doctor: ") # list the number of docs first, depending on the disease(s)
	# search doctor by name, get their ID, then:
	# doc_ID = 
	# and add it to the csv, for ease of calculating bill
	# for now, im asking the user
	doc_ID = int(input("Enter the doctor's ID: "))
	bill = int(input("Bill: ")) # leave it, delete it because we'll calc the bill
	date_of_reg = input("Enter the date of registration (DD-MM-YYY) (or leave empty for today's date): ")
	print("Does the patient require a stay at the hospital? ")
	room_req = input("Leave blank if not needed, or type in something")
	if room_req:
		room_req = True
	else:
		room_req = False

	if not date_of_reg:
		date_of_reg = datetime.now().strftime("%d-%m-%Y")

	new_patient = {
			"Patient_ID": pid, 
			"Name": name, 
			"Age": age, 
			"Gender": gender, 
			"Diseases": diseases, 
			"Doctor": doctor, 
			"Doctor_ID": doc_ID,
			"Room_Required": room_req
			}

	df.loc[len(df)] = new_patient
	df.to_csv(csvpath, index=False)
	print("\nPatient Successfully Added")

def search_patient(pid):
	df = pd.read_csv(csvpath)
	patient = df.loc[int(pid-101)]
	return patient

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

def register_hospital():
	print("Please enter the details as they are asked.")
	name = input("Enter the name of the hospital: ")
	addr = input("Enter the address of the hospital: ")
	contact_num = input("Enter the contact number of the hospital: ")
	room_charge = int(input("Enter the room charge for a single day: "))
	
	hospital_details = {
			"Name": name, 
			"Address": addr,
			"Contact_Number": contact_num,
			"Room_Charge": room_charge
			}

	df = pd.DataFrame([hospital_details])
	df.to_csv(csvpathhospital, index=False)


def register_doctor():
	df = pd.read_csv(csvpathdoc)

	print("Please enter the details as they are asked.")
	doc_id = int(len(df)+1)
	name = input("Enter the name: ")
	specialisation = input("Enter the specialisation: ")
	contact_num = int(input("Enter the contact number: "))
	consult_fee = int(input("Enter the consultation fee taken by this doctor: "))

	new_doctor = {
			"Doctor_ID": doc_id,
			"Name": name,
			"Specialisation": specialisation,
			"Contact_Number": contact_num,
			"Consultation_Fee": consult_fee
			}
	df.loc[len(df)] = new_doctor
	df.to_csv(csvpathdoc, index=False)


	
def calc_bill():
	docdf = pd.read_csv(csvpathdoc)
	pdf = pd.read_csv(csvpath)
	hospdf = pd.read_csv(csvpathhospital)

	pid = int(input("Enter the patient ID to calculate bill: "))
	patient = search_patient(pid)

	doc_ID = patient['Doctor_ID']
	consult_fee = docdf.loc[doc_ID]['Consultation_Fee']

	reg_date = datetime.strptime(patient['Registered_Date'], "%d-%m-%Y").date()
	today = datetime.today().date()

	if patient.loc['Room_Required']:
		room_charge = int(hospdf['Room_Charge'][0])
	else:
		room_charge = 0
	num_of_days = int((today - reg_date).days)
	total_room_charge = num_of_days*room_charge
	
	medicine_cost = int(input("Enter the medicine cost in integers only: "))
	total_bill = consult_fee + total_room_charge + medicine_cost
	print("days stayed is", num_of_days)
	print("room charge per day is", room_charge)
	print("so total room charge is", total_room_charge)
	print("medicine cost is", medicine_cost)
	print("so we have the total as ", total_bill)
# here, lets do bill = consultation fee + room charge (if serious disease) + medicine charge.
# medicine charge will be asked by the user, while consulation and room charge will be automatic.
# consultation fee will be taken from doctors.csv
# while room charge, keep it fixed for a hospital, so we'll take it from hospital.csv


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
	print(search_patient(pid))
elif choice == 4:
	delete_patient()
elif choice == 5:
	calc_bill()
elif choice == 6:
	display_graph()
elif choice == 7:
	exit_program()
elif choice == 8:
	# register part is done
	# need to add the part where it checks if the csv is empty or not
	# if empty, it writes new data
	# if not empty, it prompts to update only one value (or maybe more)
	register_hospital()
elif choice == 9:
	# register part is done, i just need to make update part
	# give straight up choice to the user, to either add a new entry or update old ones
	# also, if the csv is empty, dont let them update 
	register_doctor()
else:
	print("Please enter a valid choice.")
