import csv




test_array = []
test_y = []

truenum = 0
falsenum = 0
totalcount = 0

X = []
with open("Loan_Training.csv") as in_file:
	reader = csv.DictReader(in_file)
	for fields in reader:		
		totalcount += 1
		#print(fields)
		x_a = []			
		x_a.append(fields["Loan Length"])	
		x_a.append(fields["CREDIT Grade"][0])
		x_a.append(fields["Loan Purpose"])
		x_a.append(fields["Home Ownership"])
		x_a.append(fields["FICO Range"][:2])
		x_a.append(fields["Inquiries in the Last 6 Months"])
		x_a.append(fields["Accounts Now Delinquent"])
		if (len(fields["Education"]) != 0):
			x_a.append(1)
		else:
			x_a.append(0)
		x_a.append(fields["Status (Fully Paid=1, Not Paid=0)"])

		X.append(x_a)


def knn(allx, x_test):
	truetotal = 0
	falsetotal = 0
	for x_train in allx:
		cornum = 0
		for i in range(len(x_test)):
			#print("hello owrld")
			if (x_train[i] == x_test[i]):
				cornum += 1
		# print(x_train)
		# print(x_test)
		# print(cornum)

		if (cornum > 3):
			if (x_train[len(x_train) - 1] == "1"):
				truetotal += 1
			else:
				falsetotal += 1

		if (cornum > 4):
			if (x_train[len(x_train) - 1] == "1"):
				truetotal += 1 * 2
			else:
				falsetotal += 1 * 2

		if (cornum > 5):
			if (x_train[len(x_train) - 1] == "1"):
				truetotal += 1 * 4
			else:
				falsetotal += 1 * 4

		if (cornum > 6):
			if (x_train[len(x_train) - 1] == "1"):
				truetotal += 1 * 8
			else:
				falsetotal += 1 * 8
		#print(cornum)
		#print("hello world")
		# print(truetotal)
		# print(falsetotal)


	if (truetotal > falsetotal):
		return 1
	else:
		return 0




totalcorrect = 0
count = 0
with open("Loan_Training.csv") as in_file:
	reader = csv.DictReader(in_file)
	for fields in reader:
		truenum = 0
		falsenum = 0
		x_a = []
		x_a.append(fields["Loan Length"])	
		x_a.append(fields["CREDIT Grade"][0])
		x_a.append(fields["Loan Purpose"])
		x_a.append(fields["Home Ownership"])
		x_a.append(fields["FICO Range"])
		x_a.append(fields["Inquiries in the Last 6 Months"])
		x_a.append(fields["Accounts Now Delinquent"])
		if (len(fields["Education"]) != 0):
			x_a.append(1)
		else:
			x_a.append(0)
		#x_a.append(fields["Status (Fully Paid=1, Not Paid=0)"])

		km = knn(X, x_a)
		count+= 1
		#print(count)


		if (km == int(fields["Status (Fully Paid=1, Not Paid=0)"])):
			totalcorrect += 1

		print(totalcorrect / count)


# print(truecorrectclass)
# print(falsecorrectclass)

print(totalcorrect/totalcount)


# ally = []
# allid = []
# with open("Loan_ToPredict.csv") as in_file:
# 	reader = csv.DictReader(in_file)
# 	for fields in reader:
# 		trueprob = truenum / totalcount
# 		falseprob = falsenum / totalcount
# 		for i in fields:
# 			if (i == "Loan ID"):
# 				allid.append(fields[i])
# 			# if (i == "CREDIT Grade"):
# 			# 	if (fields[i] in CreditGrade):
# 			# 		k = (CreditGrade[fields[i]] + 1) / (len(CreditGrade) + truenum)
# 			# 	else:
# 			# 		k = 1 / (len(CreditGrade) + truenum)
# 			# 	trueprob = trueprob * k

# 			# 	if (fields[i] in CreditGradef):
# 			# 		k = (CreditGradef[fields[i]] + 1) / (len(CreditGradef) + falsenum)
# 			# 	else:
# 			# 		k = 1 / (len(CreditGradef) + falsenum)
# 			# 	falseprob = falseprob * k

# 			if (i == "Loan Purpose"):
# 				if (fields[i] in LoanPurpose):
# 					k = (LoanPurpose[fields[i]] + 1) / (len(LoanPurpose) + truenum)
# 				else:
# 					k = 1 / (len(LoanPurpose) + truenum)
# 				trueprob = trueprob * k

# 				if (fields[i] in LoanPurposef):
# 					k = (LoanPurposef[fields[i]] + 1) / (len(LoanPurposef) + falsenum)
# 				else:
# 					k = 1 / (len(LoanPurposef) + falsenum)
# 				falseprob = falseprob * k



# 			elif (i == "State"):
# 				if (fields[i] in State):
# 					k = (State[fields[i]] + 1) / (len(State) + truenum)
# 				else:
# 					k = 1 / (len(State) + truenum)
# 				trueprob = trueprob * k

# 				if (fields[i] in Statef):
# 					k = (Statef[fields[i]] + 1) / (len(Statef) + falsenum)
# 				else:
# 					k = 1 / (len(Statef) + falsenum)
# 				falseprob = falseprob * k

# 			elif (i == "Debt-To-Income Ratio"):
# 				v = float(fields[i].strip('%'))
# 				m = int(v / 5)
# 				if (m in Debt_To_Income):
# 					k = (Debt_To_Income[m] + 1) / (len(Debt_To_Income) + truenum)
# 				else:
# 					k = 1 / (len(Debt_To_Income) + truenum)
# 				trueprob = trueprob * k

# 				if (m in Debt_To_Incomef):
# 					k = (Debt_To_Incomef[m] + 1) / (len(Debt_To_Incomef) + falsenum)
# 				else:
# 					k = 1 / (len(Debt_To_Incomef) + falsenum)
# 				falseprob = falseprob * k

# 			elif (i == "Interest Rate"):
# 				v = float(fields[i].strip('%'))
# 				m = int(v)
# 				if (m in Interest):
# 					k = (Interest[m] + 1) / (len(Interest) + truenum)
# 				else:
# 					k = 1 / (len(Interest) + truenum)
# 				trueprob = trueprob * k

# 				if (m in Interestf):
# 					k = (Interestf[m] + 1) / (len(Interestf) + falsenum)
# 				else:
# 					k = 1 / (len(Interestf) + falsenum)

# 				#print(k)
# 				falseprob = falseprob * k

# 			elif (i == "Accounts Now Delinquent"):
# 				if (fields[i] in AccountsNowDelinquent):
# 					k = (AccountsNowDelinquent[fields[i]] + 1) / (len(AccountsNowDelinquent) + truenum)
# 				else:
# 					k = 1 / (len(AccountsNowDelinquent) + truenum)
# 				trueprob = trueprob * k

# 				if (fields[i] in AccountsNowDelinquentf):
# 					k = (AccountsNowDelinquentf[fields[i]] + 1) / (len(AccountsNowDelinquentf) + falsenum)
# 				else:
# 					k = 1 / (len(AccountsNowDelinquentf) + falsenum)
# 				falseprob = falseprob * k


# 			# elif (i == "Revolving Line Utilization"):
# 			# 	if (len(fields[i]) != 0):
# 			# 		v = float(fields[i].strip('%'))
# 			# 		m = int(v / 5)
# 			# 	else:
# 			# 		m = "NA"
# 			# 	if (m in Revolving_Line_Utilization):
# 			# 		k = (Revolving_Line_Utilization[m] + 1) / (len(Revolving_Line_Utilization) + truenum)
# 			# 	else:
# 			# 		k = 1 / (len(Revolving_Line_Utilization) + truenum)
# 			# 	trueprob = trueprob * k

# 			# 	if (m in Revolving_Line_Utilizationf):
# 			# 		k = (Revolving_Line_Utilizationf[m] + 1) / (len(Revolving_Line_Utilizationf) + falsenum)
# 			# 	else:
# 			# 		k = 1 / (len(Revolving_Line_Utilizationf) + falsenum)
# 			# 	falseprob = falseprob * k

# 			elif (i == "FICO Range"):
# 				if (fields[i] in FicoRange):
# 					k = (FicoRange[fields[i]] + 1) / (len(FicoRange) + truenum)
# 				else:
# 					k = 1 / (len(FicoRange) + truenum)
# 				trueprob = trueprob * k

# 				if (fields[i] in FicoRangef):
# 					k = (FicoRangef[fields[i]] + 1) / (len(FicoRangef) + falsenum)
# 				else:
# 					k = 1 / (len(FicoRangef) + falsenum)
# 				falseprob = falseprob * k

# 			elif (i == "Home Ownership"):
# 				if (fields[i] in HomeOwned):
# 					k = (HomeOwned[fields[i]] + 1) / (len(HomeOwned) + truenum)
# 				else:
# 					k = 1 / (len(HomeOwned) + truenum)
# 				trueprob = trueprob * k

# 				if (fields[i] in HomeOwnedf):
# 					k = (HomeOwnedf[fields[i]] + 1) / (len(HomeOwnedf) + falsenum)
# 				else:
# 					k = 1 / (len(HomeOwnedf) + falsenum)
# 				falseprob = falseprob * k

			

# 			elif (i == "Inquiries in the Last 6 Months"):
# 				if (fields[i] in Inquries):
# 					k = (Inquries[fields[i]] + 1) / (len(Inquries) + truenum)
# 				else:
# 					k = 1 / (len(Inquries) + truenum)
# 				trueprob = trueprob * k

# 				if (fields[i] in Inquriesf):
# 					k = (Inquriesf[fields[i]] + 1) / (len(Inquriesf) + falsenum)
# 				else:
# 					k = 1 / (len(Inquriesf) + falsenum)
# 				falseprob = falseprob * k

# 			elif (i == "Delinquencies (Last 2 yrs)"):
# 				if (fields[i] in Delinquencies):
# 					k = (Delinquencies[fields[i]] + 1) / (len(Delinquencies) + truenum)
# 				else:
# 					k = 1 / (len(Delinquencies) + truenum)
# 				trueprob = trueprob * k

# 				if (fields[i] in Delinquenciesf):
# 					k = (Delinquenciesf[fields[i]] + 1) / (len(Delinquenciesf) + falsenum)
# 				else:
# 					k = 1 / (len(Delinquenciesf) + falsenum)
# 				falseprob = falseprob * k

# 			# elif (i == "Public Records On File"):
# 			# 	if (fields[i] in Records):
# 			# 		k = (Records[fields[i]] + 1) / (len(Records) + truenum)
# 			# 	else:
# 			# 		k = 1 / (len(Records) + truenum)
# 			# 	trueprob = trueprob * k

# 			# 	if (fields[i] in Recordsf):
# 			# 		k = (Recordsf[fields[i]] + 1) / (len(Recordsf) + falsenum)
# 			# 	else:
# 			# 		k = 1 / (len(Recordsf) + falsenum)
# 			# 	falseprob = falseprob * k

# 			elif (i == "Education"):
# 				if (len(fields[i]) != 0):
# 					m = 1
# 				else:
# 					m = 0

# 				if (m in Education):
# 					k = (Education[m] + 1) / (len(Education) + truenum)
# 				else:
# 					k = 1 / (len(Education) + truenum)
# 				trueprob = trueprob * k
# 				#print(k)

# 				if (m in Educationf):
# 					k = (Educationf[m] + 1) / (len(Educationf) + falsenum)
# 				else:
# 					k = 1 / (len(Educationf) + falsenum)
# 				falseprob = falseprob * k

# 			elif (i == "Employment Length"):
# 				if (fields[i] in Working):
# 					k = (Working[fields[i]] + 1) / (len(Working) + truenum)
# 				else:
# 					k = 1 / (len(Working) + truenum)
# 				trueprob = trueprob * k

# 				if (fields[i] in Workingf):
# 					k = (Workingf[fields[i]] + 1) / (len(Workingf) + falsenum)
# 				else:
# 					k = 1 / (len(Workingf) + falsenum)
# 				falseprob = falseprob * k

# 			elif (i == "Months Since Last Delinquency"):
# 				if (fields[i] in LastDelinquency):
# 					k = (LastDelinquency[fields[i]] + 1) / (len(LastDelinquency) + truenum)
# 				else:
# 					k = 1 / (len(LastDelinquency) + truenum)
# 				trueprob = trueprob * k

# 				if (fields[i] in LastDelinquencyf):
# 					k = (LastDelinquencyf[fields[i]] + 1) / (len(LastDelinquencyf) + falsenum)
# 				else:
# 					k = 1 / (len(LastDelinquencyf) + falsenum)
# 				falseprob = falseprob * k

# 			# elif (i == "Earliest CREDIT Line"):
# 			# 	m = fields[i].split('/')
# 			# 	if (len(m) == 3):
# 			# 		v = 10 - int(m[2][0])

# 			# 		if (v in Earliest):
# 			# 			k = (Earliest[v] + 1) / (len(Earliest) + truenum)
# 			# 		else:
# 			# 			k = 1 / (len(Earliest) + truenum)
# 			# 		trueprob = trueprob * k

# 			# 		if (v in Earliestf):
# 			# 			k = (Earliestf[v] + 1) / (len(Earliestf) + falsenum)
# 			# 		else:
# 			# 			k = 1 / (len(Earliestf) + falsenum)
# 			# 		falseprob = falseprob * k
# 			# 		#print(k)

# 		if (trueprob > falseprob):
# 			ally.append(1)
# 		else:
# 			ally.append(0)

# with open('output.csv', 'w') as csvfile:
#     fieldnames = ['Loan ID', 'Status (Fully Paid=1, Not Paid=0)']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     for i in range (len(ally)):
#     	writer.writerow({'Loan ID': allid[i], 'Status (Fully Paid=1, Not Paid=0)': ally[i]})

