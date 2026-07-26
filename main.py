import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime

# add the functionality to handle the error if the csv doesnt exist

csvpath = "patient.csv"
csvpathdoc = "doctors.csv"
csvpathhospital = "hospital.csv"

# print menu
print("="*10, "NOVACARE HOSPITAL MANAGEMENT SYSTEM", "="*10)
print("~ please select an option ~")
print("1. Display All Records ")
print("2. Add/Update a Patient Record ")
print("3. Search Patient with ID")
print("4. Delete Patient Record ")
print("5. Calculate Bill ")
print("6. Display Graph ")
print("7. Exit Program ")
print("8. Register/Update Your Hospital Details ")
print("9. Register/Update a Doctor Record ")
print("="*57)

choice = int(input("Enter your choice: "))

def display_records():
	df = pd.read_csv(csvpath)
	print("\nPatient Records")
	print(df)

def add_patient():
	df = pd.read_csv(csvpath)

	pid = int(len(df)+101)
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
			"Registered_Date": date_of_reg,
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

def update_hospital(hospdf):
	print("What do you want to update?")
	print("Enter the corresponding number to continue.")
	print("1. Name")
	print("2. Address")
	print("3. Contact Number")
	print("4. Room Charge Per Day")

	choice = int(input("Enter your choice number: "))

	if choice == 1:
		hospdf['Name'] = input("Enter new name: ")
	elif choice == 2:
		hospdf['Address'] = input("Enter new address: ")
	elif choice == 3:
		hospdf['Contact_Number'] = int(input("Enter new contact number: "))
	elif choice == 4:
		hospdf['Room_Charge'] = int(input("Enter new room charge: "))
	else:
		print("Please enter a valid choice.")

	hospdf.to_csv(csvpathhospital, index=False)
	

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


def update_patient():


	print("WORK IN PROGRESS!!! CONTINUE AHEAD WITH CAUTION!!!")
    df = pd.read_csv(csvpath)

    pid = int(input("Enter the Patient ID to Update: "))

    print("What do you want to update?")
    print("Enter the corresponding number to continue.")
    print("1. Name")
    print("2. Age")
    print("3. Gender")
    print("4. Diseases")
	print("5. Doctor")
	print("6. Registered Date")
	print("7. Whether a Room is Required or Not")

    choice = int(input("Enter your choice number: "))

    #if choice == 1:
    #    docdf.loc[doc_ID, 'Name'] = input("Enter new name: ")
    #elif choice == 2:
    #    docdf.loc[doc_ID, 'Specialisation'] = input("Enter new value: ")
    #elif choice == 3:
    #    print(docdf.loc[doc_ID, 'Contact_Number'])
    #    docdf.loc[doc_ID, 'Contact_Number'] = int(input("Enter new contact number: "))
    #elif choice == 4:
    #    docdf.loc[doc_ID, 'Consultation_Fee'] = int(input("Enter new consultation fee: "))
    #else:
    #    print("Please enter a valid choice.")

    #docdf.to_csv(csvpathdoc, index=False)


def update_doctor():
	docdf = pd.read_csv(csvpathdoc)

	doc_ID = int(input("Enter the Doctor ID to update: "))

	print("What do you want to update?")
	print("Enter the corresponding number to continue.")
	print("1. Name")
	print("2. Specialisation")
	print("3. Contact Number")
	print("4. Consultation Fee")

	choice = int(input("Enter your choice number: "))

	if choice == 1:
		docdf.loc[doc_ID, 'Name'] = input("Enter new name: ")
	elif choice == 2:
		docdf.loc[doc_ID, 'Specialisation'] = input("Enter new value: ")
	elif choice == 3:
		print(docdf.loc[doc_ID, 'Contact_Number'])
		docdf.loc[doc_ID, 'Contact_Number'] = int(input("Enter new contact number: "))
	elif choice == 4:
		docdf.loc[doc_ID, 'Consultation_Fee'] = int(input("Enter new consultation fee: "))
	else:
		print("Please enter a valid choice.")

	docdf.to_csv(csvpathdoc, index=False)

	
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



# things left to do (things that palparch has to do):
# 1.  def discharge_patient():
# uses existing fucntions to first print the bill, mark the patient as discharged on the csv file
# 2. also,
# i'll add data validation to all the inputs
# 3. the update patient function is work in progress but yeah it'll be done too
# 4. in the patient.csv file, let's add another field for status of the patient, whether admitted, discharged because hospitals are rquired to keep data as old as 3 years, atleast in india, and that is mandatory by law.
# 5. another thing left to do is,
# 	using the actual registered hospital name everywhere
# 6. yet another thing left,
# 	printing the bill in an organised manner, rn it just prints very messy
# 7. for update functions, check if the given id exists and then only proceed. same with the delete ones
# 8. make a function to delete a doctor record
# 9. when registering a patient, do it so that the doctor id is taken care of by itself, idk how but ill try.
# 10. and yeah last but not the least
# 	ill add error management for the cases where the csv has yet to be initialised, which means the csv is empty.
# all that i did so far, took me like 4 hours lmao so yeah im gonna take a rest for a while and come back again to attack this shii
# also alsoooo, if you have any recommendations, like any at all, feel free to add here! byeee!


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

	print("Please enter a choice as prompted below.")
    print("1. Register a new patient.")
    print("2. Update a patient's details.")

    response = int(input("Enter your choice: "))

    if response == 1:
        add_patient()
    elif response == 2:
        update_patient()
    else:
        print("Please enter a valid choice.")
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
	hospdf = pd.read_csv(csvpathhospital)
	if hospdf.empty:
		register_hospital()
	else:
		print("The hospital is already registered.")
		print("You can update the details here.")
		update_hospital(hospdf)
elif choice == 9:
	print("Please enter a choice as prompted below.")
	print("1. Register a new doctor.")
	print("2. Update a doctor's details.")

	response = int(input("Enter your choice: "))

	if response == 1:
		register_doctor()
	elif response == 2:
		update_doctor()
	else:
		print("Please enter a valid choice.")
else:
	print("Please enter a valid choice.")



	# for the update functions, add error management for when the given id doesnt exist in the csv
