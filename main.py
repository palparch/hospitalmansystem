import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime

csvpath = "patient.csv"
csvpathdoc = "doctors.csv"
csvpathhospital = "hospital.csv"
csvpathdisease = "diseases.csv"

hospdf = pd.read_csv(csvpathhospital)

# print the menu
print("="*10, (hospdf['Name'][0]).upper(), "MANAGEMENT SYSTEM", "="*10)
print("~ please select an option ~")
print("1. Display All Records")
print("2. Add/Update/Delete a Patient Record")
print("3. Search Patient with ID")
print("4. Calculate Bill")
print("5. Display Graph")
print("6. Register/Update Your Hospital Details")
print("7. Register/Update/Delete a Doctor Record")
print("8. Exit Program")
print("="*57)


try:
	choice = int(input("Enter your choice: "))
except:
	print("Please enter a valid integer value. Kindly try again.")

def display_records():
	df = pd.read_csv(csvpath)
	print("\nPatient Records")
	print(df)

def add_patient():
	df = pd.read_csv(csvpath)
	diseasesdf = pd.read_csv(csvpathdisease)
	docdf = pd.read_csv(csvpathdoc)

	pid = int(len(df)+101)
	name = input("Name: ")
	try:
		age = int(input("Age: "))
	except:
		print("Age can only be integers. Please try again with the correct value.")
	gender = input("Gender: ")
	print(diseasesdf)
	doc_ID = None

	disease = input("Diseases (enter the name only): ")
	for i in range(len(diseasesdf)):
		if diseasesdf.loc[i, "Disease"].lower() == disease.lower():
			doc_ID = "Doctor ID:", diseasesdf.loc[i, "Doctor_ID"]
	if doc_ID is None:
		print("Disease not found.")

	date_of_reg = input("Enter the date of registration (DD-MM-YYY) (or leave empty for today's date): ")
	print("Does the patient require a stay at the hospital? ")
	room_req = input("Leave blank if not needed, or type in something")
	if room_req:
		room_req = True
	else:
		room_req = False

	if not date_of_reg:
		date_of_reg = datetime.now().strftime("%d-%m-%Y")

	try:
		datetime.strptime(date_of_reg, "%d-%m-%Y")
	except ValueError:
		print("Invalid date format.")

	new_patient = {
			"Patient_ID": pid, 
			"Name": name, 
			"Age": age, 
			"Gender": gender, 
			"Diseases": disease, 
			"Doctor_ID": doc_ID,
			"Registered_Date": date_of_reg,
			"Room_Required": room_req,
			}

	df.loc[len(df)] = new_patient
	df.to_csv(csvpath, index=False)
	print("\nPatient Successfully Added")

	exit_program()


def search_patient(pid):
	df = pd.read_csv(csvpath)

	try:
		patient = df.loc[int(pid-101)]

		if patient.empty:
			print("No patient exists with this patient ID. Please try again.")

		patient = df[df["Patient_ID"] == pid]
		return patient

	except:
		print("Patient ID does not exist")

def delete_patient():
	df = pd.read_csv(csvpath)
	try:
		pid = int(input("Enter the patient ID for the patient that you want to delete: "))
	except:
		print("Patient ID can only be an integer. Please try again with the correct value.")
	print("Are you sure you want to delete patient", pid, "?")
	response = input("Enter yes or no to continue: ")

	if response == "no":
		return True

	try:
		newdf = df.drop(pid-100, axis=0)
		newdf.to_csv(csvpath, index=False)
		print("Successfully deleted patient", pid)
	except:
		print("This patient ID doesn't exist. Please try again.")


def register_hospital():
	print("Please enter the details as they are asked.")
	name = input("Enter the name of the hospital: ")
	addr = input("Enter the address of the hospital: ")
	contact_num = input("Enter the contact number of the hospital: ")
	try:
		room_charge = float(input("Enter the room charge for a single day: "))
	except:
		print("Room charge can only be a numerical value. Please try again with the correct value.")

	hospital_details = {
			"Name": name, 
			"Address": addr,
			"Contact_Number": contact_num,
			"Room_Charge": room_charge
			}

	df = pd.DataFrame([hospital_details])
	df.to_csv(csvpathhospital, index=False)

def update_hospital(hospdf):
	print("What do you want to update?")
	print("Enter the corresponding number to continue.")
	print("1. Name")
	print("2. Address")
	print("3. Contact Number")
	print("4. Room Charge Per Day")

	try:
		choice = int(input("Enter your choice number: "))
	except:
		print("The value can only be an integer. Please try again with the correct value.")

	if choice == 1:
		hospdf['Name'] = input("Enter new name: ")
	elif choice == 2:
		hospdf['Address'] = input("Enter new address: ")
	elif choice == 3:
		try:
			hospdf['Contact_Number'] = int(input("Enter new contact number: "))
		except:
			print("Contact number can only be an integer value. Please try again with a valid contact number.")
	elif choice == 4:
		try:
			hospdf['Room_Charge'] = float(input("Enter new room charge: "))
		except:
			print("Room charge can only be a numerical value. Please try again with a valid value.")
	else:
		print("Please enter a valid choice.")

	hospdf.to_csv(csvpathhospital, index=False)
	

def register_doctor():
	df = pd.read_csv(csvpathdoc)

	print("Please enter the details as they are asked.")
	doc_id = int(len(df)+1)
	name = input("Enter the name: ")
	specialisation = input("Enter the specialisation: ")
	try:
		contact_num = int(input("Enter the contact number: "))
	except:
		print("Contact number can only be an integer value. Please try again with the correct value.")
	try:
		consult_fee = float(input("Enter the consultation fee taken by this doctor: "))
	except:
		print("Consultation fee can only be a numerical value. Please try again with the correct value.")

	new_doctor = {
			"Doctor_ID": doc_id,
			"Name": name,
			"Specialisation": specialisation,
			"Contact_Number": contact_num,
			"Consultation_Fee": consult_fee
			}
	df.loc[len(df)] = new_doctor
	df.to_csv(csvpathdoc, index=False)


def update_patient():
	df = pd.read_csv(csvpath)
	try:
		pid = int(input("Enter the Patient ID to Update: "))
	except:
		print("Patient ID can only be an integer value. Please try again with the correct value.")
	
	try:
		row = df[df["Patient_ID"] == pid].index[0]
	except:
		print("This patient ID doesn't exist. Please try again with a valid patient ID.")

	print("What do you want to update?")
	print("Enter the corresponding number to continue.")
	print("1. Name")
	print("2. Age")
	print("3. Gender")
	print("4. Diseases")
	print("5. Doctor ID")
	print("6. Registered Date")
	print("7. Whether a Room is Required or Not")

	try:
		choice = int(input("Enter your choice number: "))
	except:
		print("The value can only be an integer. Please try again with the correct value.")

	if choice == 1:
		df.loc[row, "Name"] = input("Enter new name: ")

	elif choice == 2:
		df.loc[row, "Age"] = int(input("Enter new age: "))

	elif choice == 3:
		df.loc[row, "Gender"] = input("Enter new gender: ")

	elif choice == 4:
		df.loc[row, "Diseases"] = input("Enter new disease: ")

	elif choice == 5:
		df.loc[row, "Doctor_ID"] = int(input("Enter new Doctor ID: "))

	elif choice == 6:
		print("Please enter a new date in (DD-MM-YYYY) format.")
		df.loc[row, "Registered_Date"] = input("Enter new date: ")

	elif choice == 7:
		df.loc[row, "Room_Required"] = input("Enter True or False: ")

	else:
		print("Please enter a valid choice.")

	df.to_csv(csvpath, index=False)


def update_doctor():
	docdf = pd.read_csv(csvpathdoc)

	doc_ID = int(input("Enter the Doctor ID to update: "))

	print("What do you want to update?")
	print("1. Name")
	print("2. Specialisation")
	print("3. Contact Number")
	print("4. Consultation Fee")

	try:
		choice = int(input("Enter your choice number: "))
	except:
		print("The value can only be an integer. Please try again with the correct value.")

	try:
		row = docdf[docdf["Doctor_ID"] == doc_ID].index[0]
	except:
		print("This doctor ID doesn't exist. Please try again with a valid doctor ID.")

	if choice == 1:
		docdf.loc[row, "Name"] = input("Enter new name: ")

	elif choice == 2:
		docdf.loc[row, "Specialisation"] = input("Enter new value: ")

	elif choice == 3:
		docdf.loc[row, "Contact_Number"] = int(input("Enter new contact number: "))

	elif choice == 4:
		docdf.loc[row, "Consultation_Fee"] = int(input("Enter new consultation fee: "))

	else:
		print("Please enter a valid choice.")

	docdf.to_csv(csvpathdoc, index=False)


def delete_doctor():
	df = pd.read_csv(csvpathdoc)
	try:
		doc_ID = int(input("Enter the doctor ID for the patient that you want to delete: "))
	except:
		print("Doctor ID can only be an integer value. Please try again with the correct value.")
	print("Are you sure you want to delete doctor", doc_ID, "?")
	response = input("Enter yes or no to continue: ")

	if response == "no":
		return True
	try:
		newdf = df.drop(doc_ID, axis=0)
		newdf.to_csv(csvpathdoc, index=False)	
		print("Successfully deleted the doctor record,", doc_ID)
	except:
		print("This doctor ID doesn't exist. Please try again.")

def calc_bill():
	docdf = pd.read_csv(csvpathdoc)
	pdf = pd.read_csv(csvpath)
	hospdf = pd.read_csv(csvpathhospital)

	try:
		pid = int(input("Enter the patient ID to calculate bill: "))
	except:
		print("Please enter a valid integer value as patient ID.")

	try:
		patient = search_patient(pid)
	except:
		print("This patient ID doesn't exist. Please try again with a valid patient ID.")
	
	try:
		doc_ID = patient['Doctor_ID']
		consult_fee = list(docdf.loc[doc_ID]["Consultation_Fee"])[0]
	
		reg_date = datetime.strptime(patient['Registered_Date'][1], "%d-%m-%Y").date()
		today = datetime.today().date()

		patient_name = list(patient["Name"])[0]
		doc_name = list(docdf.loc[doc_ID]["Name"])[0]
		doc_specialisation = list(docdf.loc[doc_ID]["Specialisation"])[0]

		hosp_name = hospdf.loc[0]["Name"]
		hosp_addr = hospdf.loc[0]["Address"]
		hosp_contact = hospdf.loc[0]["Contact_Number"]

		if patient['Room_Required'][1]:
			room_charge = int(hospdf['Room_Charge'][0])
		else:
			room_charge = 0
	except:
		print("An error occurred. Please try again with the valid values.")


	num_of_days = int((today - reg_date).days)
	total_room_charge = num_of_days*room_charge

	try:
		medicine_cost = int(input("Enter the medicine cost in numbers only: "))
	except:
		print("Please enter a valid numerical value as medicine cost.")

	total_bill = consult_fee + total_room_charge + medicine_cost

	# printing the bill
	print()
	print()
	print()
	print("\n" + "="*50)
	print(" "*20, hosp_name.upper())
	print(" "*20, "HOSPITAL BILL")
	print("="*50)

	print("Address		   :", hosp_addr)
	print("Contact Number  :", hosp_contact)

	print("-"*50)

	print("Patient ID	   :", pid)
	print("Patient Name    :", patient_name)
	print("Doctor Name	   :", doc_name)
	print("Specialisation  :", doc_specialisation)

	print("-"*50)

	print("Consultation Fee:", consult_fee)
	print("Days Stayed	   :", num_of_days)
	print("Room Charge/day :", room_charge)
	print("Room Charges    :", total_room_charge)
	print("Medicine Cost   :", medicine_cost)

	print("-"*50)

	print("TOTAL BILL	   :", total_bill)

	print("="*50)



def display_graph():
	df = pd.read_csv(csvpath)
	docdf = pd.read_csv(csvpathdoc)
	diseases_count = df["Diseases"].value_counts()
	
	plt.figure(figsize=(8,5))
	plt.bar(diseases_count.index, diseases_count.values)
	
	plt.title("Number of Patient for Each Diseases")
	plt.xlabel("Diseases")
	plt.ylabel("Number of patients")

	plt.show()


	df = df.merge(docdf[["Doctor_ID", "Name"]], on="Doctor_ID")
	
	doctor_list = []

	for i in range(len(df)):
		for j in range(len(docdf)):
			if df.loc[i, "Doctor_ID"] == docdf.loc[j, "Doctor_ID"]:
				doctor_list.append(docdf.loc[j, "Name"])

	doctor_count = pd.Series(doctor_list).value_counts()

	plt.figure(figsize=(8,5))
	plt.bar(doctor_count.index, doctor_count.values)

	plt.title("Number of Patient Treated by Each Doctor")
	plt.xlabel("Doctor")
	plt.ylabel("Number of Patients")

	plt.show()


def exit_program():
	print("Thanks for using", hospdf['Name'][0], "Hospital System, Have a Nice Day ")


if choice == 1:
	display_records()
	exit_program()
elif choice == 2:
	print("Please enter a choice as prompted below.")
	print("1. Register a new patient.")
	print("2. Update a patient's details.")
	print("3. Delete a patient record.")

	try:
		response = int(input("Enter your choice: "))
	except:
		print("Please enter a valid integer value. Kindly try again.")

	if response == 1:
		add_patient()
	elif response == 2:
		update_patient()
	elif response == 3:
		delete_patient()
	else:
		print("Please enter a valid choice.")
	exit_program()
elif choice == 3:
	try:
		pid = int(input("Enter the patient ID to search: "))
	except:
		print("Please enter a valid integer value. Kindly try again.")
	print(search_patient(pid))
	exit_program()
elif choice == 4:
	calc_bill()
	exit_program()
elif choice == 5:
	display_graph()
	exit_program()
elif choice == 8:
	exit_program()
elif choice == 6:
	hospdf = pd.read_csv(csvpathhospital)
	if hospdf.empty:
		register_hospital()
	else:
		print("The hospital is already registered.")
		print("You can update the details here.")
		update_hospital(hospdf)
	exit_program()
elif choice == 7:
	print("Please enter a choice as prompted below.")
	print("1. Register a new doctor.")
	print("2. Update a doctor's details.")
	print("3. Delete a doctor record.")

	try:
		response = int(input("Enter your choice: "))
	except:
		print("Please enter a valid integer value. Kindly try again.")

	if response == 1:
		register_doctor()
	elif response == 2:
		update_doctor()
	elif response == 3:
		delete_doctor()
	else:
		print("Please enter a valid choice.")
	exit_program()
else:
	print("Please enter a valid choice.")
