import csv

CreditGrade = {}
LoanPurpose = {}
Debt_To_Income = {}
HomeOwned = {}
FicoRange = {}
TotalCredit = {}
Inquries = {}
Delinquencies = {}
Records = {}
Education = {}
Revolving_Line_Utilization = {}
Working = {}
State = {}
AccountsNowDelinquent = {}
Earliest = {}
Interest = {}

LastDelinquency = {}
truearray = [CreditGrade, LoanPurpose, Debt_To_Income, HomeOwned, FicoRange, TotalCredit, Inquries, Delinquencies, Records, Education]

CreditGradef = {}
LoanPurposef = {}
Debt_To_Incomef = {}
HomeOwnedf = {}
FicoRangef = {}
TotalCreditf = {}
Inquriesf = {}
Delinquenciesf = {}
Recordsf = {}
Educationf = {}
Workingf = {}
LastDelinquencyf= {}
Earliestf = {}
Interestf = {}
AccountsNowDelinquentf = {}

Revolving_Line_Utilizationf = {}
Statef = {}

falsearray = [CreditGradef, LoanPurposef, Debt_To_Incomef, HomeOwnedf, FicoRangef, TotalCreditf, Inquriesf, Delinquenciesf, Recordsf, Educationf]


test_array = []
test_y = []

truenum = 0
falsenum = 0
totalcount = 0


with open("Loan_Training.csv") as in_file:
	reader = csv.DictReader(in_file)
	for fields in reader:		
		totalcount += 1
		#print(fields)
		if (int(fields["Status (Fully Paid=1, Not Paid=0)"]) == 1):
			for i in fields:
				if (i == "CREDIT Grade"):
					if (fields[i] in CreditGrade):
						CreditGrade[fields[i]] += 1
					else:
						CreditGrade[fields[i]] = 1
				elif (i == "Loan Purpose"):
					if (fields[i] in LoanPurpose):
						LoanPurpose[fields[i]] += 1
					else:
						LoanPurpose[fields[i]] = 1

				elif (i == "State"):
					if (fields[i] in State):
						State[fields[i]] += 1
					else:
						State[fields[i]] = 1

				elif (i == "Debt-To-Income Ratio"):
					v = float(fields[i].strip('%'))
					m = int(v / 5)
					if (m in Debt_To_Income):
						Debt_To_Income[m] += 1
					else:
						Debt_To_Income[m] = 1

				elif (i == "Revolving Line Utilization"):
					if (len(fields[i]) != 0):
						v = float(fields[i].strip('%'))
						m = int(v / 5)
					else:
						m = "NA"
					if (m in Revolving_Line_Utilization):
						Revolving_Line_Utilization[m] += 1
					else:
						Revolving_Line_Utilization[m] = 1

				elif (i == "Interest Rate"):
					if (len(fields[i]) != 0):
						v = float(fields[i].strip('%'))
						m = int(v)
					else:
						m = "NA"
					if (m in Interest):
						Interest[m] += 1
					else:
						Interest[m] = 1

				elif (i == "FICO Range"):
					if (fields[i] in FicoRange):
						FicoRange[fields[i]] += 1
					else:
						FicoRange[fields[i]] = 1

				elif (i == "Home Ownership"):
					if (fields[i] in HomeOwned):
						HomeOwned[fields[i]] += 1
					else:
						HomeOwned[fields[i]] = 1
				

				elif (i == "Inquiries in the Last 6 Months"):
					if (fields[i] in Inquries):
						Inquries[fields[i]] += 1
					else:
						Inquries[fields[i]] = 1

				elif (i == "Delinquencies (Last 2 yrs)"):
					if (fields[i] in Delinquencies):
						Delinquencies[fields[i]] += 1
					else:
						Delinquencies[fields[i]] = 1

				elif (i == "Public Records On File"):
					if (fields[i] in Records):
						Records[fields[i]] += 1
					else:
						Records[fields[i]] = 1

				elif (i == "Education"):
					if (len(fields[i]) != 0):
						m = 1
					else:
						m = 0
					if (m in Education):
						Education[m] += 1
					else:
						Education[m] = 1

				elif (i == "Employment Length"):
					if (fields[i] in Working):
						Working[fields[i]] += 1
					else:
						Working[fields[i]] = 1


				elif (i == "Months Since Last Delinquency"):
					if (len(fields[i]) != 0):
						m = int(int(fields[i]) / 5)
						if (m in LastDelinquency):
							LastDelinquency[m] += 1
						else:
							LastDelinquency[m] = 1
					else:
						if (0 in LastDelinquency):
							LastDelinquency[0] += 1
						else:
							LastDelinquency[0] = 1

				elif (i == "Accounts Now Delinquent"):
					if (fields[i] in AccountsNowDelinquent):
						AccountsNowDelinquent[fields[i]] += 1
					else:
						AccountsNowDelinquent[fields[i]] = 1


				elif (i == "Earliest CREDIT Line"):

					m = fields[i].split('/')
					if (len(m) == 3):
						v = 10 - int(m[2][0])
						if (v in Earliest):
							Earliest[v] += 1
						else:
							Earliest[v] = 1

					

			truenum += 1
		else:
			for i in fields:
				if (i == "CREDIT Grade"):
					if (fields[i] in CreditGradef):
						CreditGradef[fields[i]] += 1
					else:
						CreditGradef[fields[i]] = 1
				elif (i == "Loan Purpose"):
					if (fields[i] in LoanPurposef):
						LoanPurposef[fields[i]] += 1
					else:
						LoanPurposef[fields[i]] = 1

				elif (i == "State"):
					if (fields[i] in Statef):
						Statef[fields[i]] += 1
					else:
						Statef[fields[i]] = 1

				elif (i == "Debt-To-Income Ratio"):
					v = float(fields[i].strip('%'))
					m = int(v / 5)
					if (m in Debt_To_Incomef):
						Debt_To_Incomef[m] += 1
					else:
						Debt_To_Incomef[m] = 1

				elif (i == "Revolving Line Utilization"):
					if (len(fields[i]) != 0):
						v = float(fields[i].strip('%'))
						m = int(v / 5)
					else:
						m = "NA"
					if (m in Revolving_Line_Utilizationf):
						Revolving_Line_Utilizationf[m] += 1
					else:
						Revolving_Line_Utilizationf[m] = 1

				elif (i == "Interest Rate"):
					if (len(fields[i]) != 0):
						v = float(fields[i].strip('%'))
						m = int(v)
					else:
						m = "NA"
					if (m in Interestf):
						Interestf[m] += 1
					else:
						Interestf[m] = 1

				elif (i == "FICO Range"):
					if (fields[i] in FicoRangef):
						FicoRangef[fields[i]] += 1
					else:
						FicoRangef[fields[i]] = 1

				elif (i == "Home Ownership"):
					if (fields[i] in HomeOwnedf):
						HomeOwnedf[fields[i]] += 1
					else:
						HomeOwnedf[fields[i]] = 1

				

				elif (i == "Inquiries in the Last 6 Months"):
					if (fields[i] in Inquriesf):
						Inquriesf[fields[i]] += 1
					else:
						Inquriesf[fields[i]] = 1

				elif (i == "Delinquencies (Last 2 yrs)"):
					if (fields[i] in Delinquenciesf):
						Delinquenciesf[fields[i]] += 1
					else:
						Delinquenciesf[fields[i]] = 1

				elif (i == "Public Records On File"):
					if (fields[i] in Recordsf):
						Recordsf[fields[i]] += 1
					else:
						Recordsf[fields[i]] = 1

				elif (i == "Education"):
					if (len(fields[i]) != 0):
						m = 1
					else:
						m = 0
					if (m in Educationf):
						Educationf[m] += 1
					else:
						Educationf[m] = 1

				elif (i == "Employment Length"):
					if (fields[i] in Workingf):
						Workingf[fields[i]] += 1
					else:
						Workingf[fields[i]] = 1

				elif (i == "Months Since Last Delinquency"):
					if (len(fields[i]) != 0):
						m = int(int(fields[i]) / 5)
						if (m in LastDelinquencyf):
							LastDelinquencyf[m] += 1
						else:
							LastDelinquencyf[m] = 1
					else:
						if (0 in LastDelinquencyf):
							LastDelinquencyf[0] += 1
						else:
							LastDelinquencyf[0] = 1

				elif (i == "Accounts Now Delinquent"):
					if (fields[i] in AccountsNowDelinquentf):
						AccountsNowDelinquentf[fields[i]] += 1
					else:
						AccountsNowDelinquentf[fields[i]] = 1

				elif (i == "Earliest CREDIT Line"):
					m = fields[i].split('/')
					if (len(m) == 3):
						v = 10 - int(m[2][0])
						if (v in Earliestf):
							Earliestf[v] += 1
						else:
							Earliestf[v] = 1


			falsenum += 1


truecorrectclass = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
falsecorrectclass = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

totalcorrect = 0
with open("Loan_Training.csv") as in_file:
	reader = csv.DictReader(in_file)
	for fields in reader:
		trueprob = truenum / totalcount
		falseprob = falsenum / totalcount
		for i in fields:
			# if (i == "CREDIT Grade"):
			# 	if (fields[i] in CreditGrade):
			# 		k = (CreditGrade[fields[i]] + 1) / (len(CreditGrade) + truenum)
			# 	else:
			# 		k = 1 / (len(CreditGrade) + truenum)
			# 	trueprob = trueprob * k

			# 	if (fields[i] in CreditGradef):
			# 		k = (CreditGradef[fields[i]] + 1) / (len(CreditGradef) + falsenum)
			# 	else:
			# 		k = 1 / (len(CreditGradef) + falsenum)
			# 	falseprob = falseprob * k

			pm = int(fields["Status (Fully Paid=1, Not Paid=0)"])

			if (i == "Loan Purpose"):
				if (fields[i] in LoanPurpose):
					k1 = (LoanPurpose[fields[i]] + 1) / (len(LoanPurpose) + truenum)
				else:
					k1 = 1 / (len(LoanPurpose) + truenum)
				trueprob = trueprob * k1

				if (fields[i] in LoanPurposef):
					k2 = (LoanPurposef[fields[i]] + 1) / (len(LoanPurposef) + falsenum)
				else:
					k2 = 1 / (len(LoanPurposef) + falsenum)
				falseprob = falseprob * k2

				if (((k1 > k2) and pm == 1)):
					truecorrectclass[0] += 1
				elif (((k2 > k1) and pm == 0)):
					falsecorrectclass[0] += 1 



			elif (i == "State"):
				if (fields[i] in State):
					k1 = (State[fields[i]] + 1) / (len(State) + truenum)
				else:
					k1 = 1 / (len(State) + truenum)
				trueprob = trueprob * k1

				if (fields[i] in Statef):
					k2 = (Statef[fields[i]] + 1) / (len(Statef) + falsenum)
				else:
					k2 = 1 / (len(Statef) + falsenum)
				falseprob = falseprob * k2

				if (((k1 > k2) and pm == 1)):
					truecorrectclass[1] += 1
				elif (((k2 > k1) and pm == 0)):
					falsecorrectclass[1] += 1 

			elif (i == "Debt-To-Income Ratio"):
				v = float(fields[i].strip('%'))
				m = int(v / 5)
				if (m in Debt_To_Income):
					k1 = (Debt_To_Income[m] + 1) / (len(Debt_To_Income) + truenum)
				else:
					k1 = 1 / (len(Debt_To_Income) + truenum)
				trueprob = trueprob * k1

				if (m in Debt_To_Incomef):
					k2 = (Debt_To_Incomef[m] + 1) / (len(Debt_To_Incomef) + falsenum)
				else:
					k2 = 1 / (len(Debt_To_Incomef) + falsenum)
				falseprob = falseprob * k2

				if (((k1 > k2) and pm == 1)):
					truecorrectclass[2] += 1
				elif (((k2 > k1) and pm == 0)):
					falsecorrectclass[2] += 1 

			elif (i == "Interest Rate"):
				v = float(fields[i].strip('%'))
				m = int(v)
				if (m in Interest):
					k1 = (Interest[m] + 1) / (len(Interest) + truenum)
				else:
					k1 = 1 / (len(Interest) + truenum)
				trueprob = trueprob * k1

				if (m in Interestf):
					k2 = (Interestf[m] + 1) / (len(Interestf) + falsenum)
				else:
					k2 = 1 / (len(Interestf) + falsenum)

				#print(k)
				falseprob = falseprob * k2

				if (((k1 > k2) and pm == 1)):
					truecorrectclass[3] += 1
				elif (((k2 > k1) and pm == 0)):
					falsecorrectclass[3] += 1 

			elif (i == "Accounts Now Delinquent"):
				if (fields[i] in AccountsNowDelinquent):
					k1 = (AccountsNowDelinquent[fields[i]] + 1) / (len(AccountsNowDelinquent) + truenum)
				else:
					k1 = 1 / (len(AccountsNowDelinquent) + truenum)
				trueprob = trueprob * k1

				if (fields[i] in AccountsNowDelinquentf):
					k2 = (AccountsNowDelinquentf[fields[i]] + 1) / (len(AccountsNowDelinquentf) + falsenum)
				else:
					k2 = 1 / (len(AccountsNowDelinquentf) + falsenum)
				falseprob = falseprob * k2

				if (((k1 > k2) and pm == 1)):
					truecorrectclass[4] += 1
				elif (((k2 > k1) and pm == 0)):
					falsecorrectclass[4] += 1 


			# elif (i == "Revolving Line Utilization"):
			# 	if (len(fields[i]) != 0):
			# 		v = float(fields[i].strip('%'))
			# 		m = int(v / 5)
			# 	else:
			# 		m = "NA"
			# 	if (m in Revolving_Line_Utilization):
			# 		k = (Revolving_Line_Utilization[m] + 1) / (len(Revolving_Line_Utilization) + truenum)
			# 	else:
			# 		k = 1 / (len(Revolving_Line_Utilization) + truenum)
			# 	trueprob = trueprob * k

			# 	if (m in Revolving_Line_Utilizationf):
			# 		k = (Revolving_Line_Utilizationf[m] + 1) / (len(Revolving_Line_Utilizationf) + falsenum)
			# 	else:
			# 		k = 1 / (len(Revolving_Line_Utilizationf) + falsenum)
			# 	falseprob = falseprob * k

			elif (i == "FICO Range"):
				if (fields[i] in FicoRange):
					k1 = (FicoRange[fields[i]] + 1) / (len(FicoRange) + truenum)
				else:
					k1 = 1 / (len(FicoRange) + truenum)
				trueprob = trueprob * k1

				if (fields[i] in FicoRangef):
					k2 = (FicoRangef[fields[i]] + 1) / (len(FicoRangef) + falsenum)
				else:
					k2 = 1 / (len(FicoRangef) + falsenum)
				falseprob = falseprob * k2

				if (((k1 > k2) and pm == 1)):
					truecorrectclass[5] += 1
				elif (((k2 > k1) and pm == 0)):
					falsecorrectclass[5] += 1 

			elif (i == "Home Ownership"):
				if (fields[i] in HomeOwned):
					k1 = (HomeOwned[fields[i]] + 1) / (len(HomeOwned) + truenum)
				else:
					k1 = 1 / (len(HomeOwned) + truenum)
				trueprob = trueprob * k1

				if (fields[i] in HomeOwnedf):
					k2 = (HomeOwnedf[fields[i]] + 1) / (len(HomeOwnedf) + falsenum)
				else:
					k2 = 1 / (len(HomeOwnedf) + falsenum)
				falseprob = falseprob * k2

				if (((k1 > k2) and pm == 1)):
					truecorrectclass[6] += 1
				elif (((k2 > k1) and pm == 0)):
					falsecorrectclass[6] += 1 

			

			elif (i == "Inquiries in the Last 6 Months"):
				if (fields[i] in Inquries):
					k1 = (Inquries[fields[i]] + 1) / (len(Inquries) + truenum)
				else:
					k1 = 1 / (len(Inquries) + truenum)
				trueprob = trueprob * k1

				if (fields[i] in Inquriesf):
					k2 = (Inquriesf[fields[i]] + 1) / (len(Inquriesf) + falsenum)
				else:
					k2 = 1 / (len(Inquriesf) + falsenum)
				falseprob = falseprob * k2

				if (((k1 > k2) and pm == 1)):
					truecorrectclass[7] += 1
				elif (((k2 > k1) and pm == 0)):
					falsecorrectclass[7] += 1 

			elif (i == "Delinquencies (Last 2 yrs)"):
				if (fields[i] in Delinquencies):
					k1 = (Delinquencies[fields[i]] + 1) / (len(Delinquencies) + truenum)
				else:
					k1 = 1 / (len(Delinquencies) + truenum)
				trueprob = trueprob * k1

				if (fields[i] in Delinquenciesf):
					k2 = (Delinquenciesf[fields[i]] + 1) / (len(Delinquenciesf) + falsenum)
				else:
					k2 = 1 / (len(Delinquenciesf) + falsenum)
				falseprob = falseprob * k2

				if (((k1 > k2) and pm == 1)):
					truecorrectclass[8] += 1
				elif (((k2 > k1) and pm == 0)):
					falsecorrectclass[8] += 1 

			# elif (i == "Public Records On File"):
			# 	if (fields[i] in Records):
			# 		k = (Records[fields[i]] + 1) / (len(Records) + truenum)
			# 	else:
			# 		k = 1 / (len(Records) + truenum)
			# 	trueprob = trueprob * k

			# 	if (fields[i] in Recordsf):
			# 		k = (Recordsf[fields[i]] + 1) / (len(Recordsf) + falsenum)
			# 	else:
			# 		k = 1 / (len(Recordsf) + falsenum)
			# 	falseprob = falseprob * k

			elif (i == "Education"):
				if (len(fields[i]) != 0):
					m = 1
				else:
					m = 0

				if (m in Education):
					k1 = (Education[m] + 1) / (len(Education) + truenum)
				else:
					k1 = 1 / (len(Education) + truenum)
				trueprob = trueprob * k1
				#print(k)

				if (m in Educationf):
					k2 = (Educationf[m] + 1) / (len(Educationf) + falsenum)
				else:
					k2 = 1 / (len(Educationf) + falsenum)
				falseprob = falseprob * k2

				if (((k1 > k2) and pm == 1)):
					truecorrectclass[9] += 1
				elif (((k2 > k1) and pm == 0)):
					falsecorrectclass[9] += 1 

			elif (i == "Employment Length"):
				if (fields[i] in Working):
					k1 = (Working[fields[i]] + 1) / (len(Working) + truenum)
				else:
					k1 = 1 / (len(Working) + truenum)
				trueprob = trueprob * k1

				if (fields[i] in Workingf):
					k2 = (Workingf[fields[i]] + 1) / (len(Workingf) + falsenum)
				else:
					k2 = 1 / (len(Workingf) + falsenum)
				falseprob = falseprob * k2

				if (((k1 > k2) and pm == 1)):
					truecorrectclass[10] += 1
				elif (((k2 > k1) and pm == 0)):
					falsecorrectclass[10] += 1 

			elif (i == "Months Since Last Delinquency"):
				if (fields[i] in LastDelinquency):
					k1 = (LastDelinquency[fields[i]] + 1) / (len(LastDelinquency) + truenum)
				else:
					k1 = 1 / (len(LastDelinquency) + truenum)
				trueprob = trueprob * k1

				if (fields[i] in LastDelinquencyf):
					k2 = (LastDelinquencyf[fields[i]] + 1) / (len(LastDelinquencyf) + falsenum)
				else:
					k2 = 1 / (len(LastDelinquencyf) + falsenum)
				falseprob = falseprob * k2

				if (((k1 > k2) and pm == 1)):
					truecorrectclass[11] += 1
				elif (((k2 > k1) and pm == 0)):
					falsecorrectclass[11] += 1 

			# elif (i == "Earliest CREDIT Line"):
			# 	m = fields[i].split('/')
			# 	if (len(m) == 3):
			# 		v = 10 - int(m[2][0])

			# 		if (v in Earliest):
			# 			k = (Earliest[v] + 1) / (len(Earliest) + truenum)
			# 		else:
			# 			k = 1 / (len(Earliest) + truenum)
			# 		trueprob = trueprob * k

			# 		if (v in Earliestf):
			# 			k = (Earliestf[v] + 1) / (len(Earliestf) + falsenum)
			# 		else:
			# 			k = 1 / (len(Earliestf) + falsenum)
			# 		falseprob = falseprob * k
			# 		#print(k)


		#print(trueprob)
		#print(falseprob)
		if (trueprob > falseprob):
			if (int(fields["Status (Fully Paid=1, Not Paid=0)"]) == 1):
				totalcorrect += 1
		else:
			if (int(fields["Status (Fully Paid=1, Not Paid=0)"]) == 0):
				totalcorrect += 1

# print(truecorrectclass)
# print(falsecorrectclass)

# print(totalcorrect/totalcount)


ally = []
allid = []
with open("Loan_ToPredict.csv") as in_file:
	reader = csv.DictReader(in_file)
	for fields in reader:
		trueprob = truenum / totalcount
		falseprob = falsenum / totalcount
		for i in fields:
			if (i == "Loan ID"):
				allid.append(fields[i])
			# if (i == "CREDIT Grade"):
			# 	if (fields[i] in CreditGrade):
			# 		k = (CreditGrade[fields[i]] + 1) / (len(CreditGrade) + truenum)
			# 	else:
			# 		k = 1 / (len(CreditGrade) + truenum)
			# 	trueprob = trueprob * k

			# 	if (fields[i] in CreditGradef):
			# 		k = (CreditGradef[fields[i]] + 1) / (len(CreditGradef) + falsenum)
			# 	else:
			# 		k = 1 / (len(CreditGradef) + falsenum)
			# 	falseprob = falseprob * k

			if (i == "Loan Purpose"):
				if (fields[i] in LoanPurpose):
					k = (LoanPurpose[fields[i]] + 1) / (len(LoanPurpose) + truenum)
				else:
					k = 1 / (len(LoanPurpose) + truenum)
				trueprob = trueprob * k

				if (fields[i] in LoanPurposef):
					k = (LoanPurposef[fields[i]] + 1) / (len(LoanPurposef) + falsenum)
				else:
					k = 1 / (len(LoanPurposef) + falsenum)
				falseprob = falseprob * k



			elif (i == "State"):
				if (fields[i] in State):
					k = (State[fields[i]] + 1) / (len(State) + truenum)
				else:
					k = 1 / (len(State) + truenum)
				trueprob = trueprob * k

				if (fields[i] in Statef):
					k = (Statef[fields[i]] + 1) / (len(Statef) + falsenum)
				else:
					k = 1 / (len(Statef) + falsenum)
				falseprob = falseprob * k

			elif (i == "Debt-To-Income Ratio"):
				v = float(fields[i].strip('%'))
				m = int(v / 5)
				if (m in Debt_To_Income):
					k = (Debt_To_Income[m] + 1) / (len(Debt_To_Income) + truenum)
				else:
					k = 1 / (len(Debt_To_Income) + truenum)
				trueprob = trueprob * k

				if (m in Debt_To_Incomef):
					k = (Debt_To_Incomef[m] + 1) / (len(Debt_To_Incomef) + falsenum)
				else:
					k = 1 / (len(Debt_To_Incomef) + falsenum)
				falseprob = falseprob * k

			elif (i == "Interest Rate"):
				v = float(fields[i].strip('%'))
				m = int(v)
				if (m in Interest):
					k = (Interest[m] + 1) / (len(Interest) + truenum)
				else:
					k = 1 / (len(Interest) + truenum)
				trueprob = trueprob * k

				if (m in Interestf):
					k = (Interestf[m] + 1) / (len(Interestf) + falsenum)
				else:
					k = 1 / (len(Interestf) + falsenum)

				#print(k)
				falseprob = falseprob * k

			elif (i == "Accounts Now Delinquent"):
				if (fields[i] in AccountsNowDelinquent):
					k = (AccountsNowDelinquent[fields[i]] + 1) / (len(AccountsNowDelinquent) + truenum)
				else:
					k = 1 / (len(AccountsNowDelinquent) + truenum)
				trueprob = trueprob * k

				if (fields[i] in AccountsNowDelinquentf):
					k = (AccountsNowDelinquentf[fields[i]] + 1) / (len(AccountsNowDelinquentf) + falsenum)
				else:
					k = 1 / (len(AccountsNowDelinquentf) + falsenum)
				falseprob = falseprob * k


			# elif (i == "Revolving Line Utilization"):
			# 	if (len(fields[i]) != 0):
			# 		v = float(fields[i].strip('%'))
			# 		m = int(v / 5)
			# 	else:
			# 		m = "NA"
			# 	if (m in Revolving_Line_Utilization):
			# 		k = (Revolving_Line_Utilization[m] + 1) / (len(Revolving_Line_Utilization) + truenum)
			# 	else:
			# 		k = 1 / (len(Revolving_Line_Utilization) + truenum)
			# 	trueprob = trueprob * k

			# 	if (m in Revolving_Line_Utilizationf):
			# 		k = (Revolving_Line_Utilizationf[m] + 1) / (len(Revolving_Line_Utilizationf) + falsenum)
			# 	else:
			# 		k = 1 / (len(Revolving_Line_Utilizationf) + falsenum)
			# 	falseprob = falseprob * k

			elif (i == "FICO Range"):
				if (fields[i] in FicoRange):
					k = (FicoRange[fields[i]] + 1) / (len(FicoRange) + truenum)
				else:
					k = 1 / (len(FicoRange) + truenum)
				trueprob = trueprob * k

				if (fields[i] in FicoRangef):
					k = (FicoRangef[fields[i]] + 1) / (len(FicoRangef) + falsenum)
				else:
					k = 1 / (len(FicoRangef) + falsenum)
				falseprob = falseprob * k

			elif (i == "Home Ownership"):
				if (fields[i] in HomeOwned):
					k = (HomeOwned[fields[i]] + 1) / (len(HomeOwned) + truenum)
				else:
					k = 1 / (len(HomeOwned) + truenum)
				trueprob = trueprob * k

				if (fields[i] in HomeOwnedf):
					k = (HomeOwnedf[fields[i]] + 1) / (len(HomeOwnedf) + falsenum)
				else:
					k = 1 / (len(HomeOwnedf) + falsenum)
				falseprob = falseprob * k

			

			elif (i == "Inquiries in the Last 6 Months"):
				if (fields[i] in Inquries):
					k = (Inquries[fields[i]] + 1) / (len(Inquries) + truenum)
				else:
					k = 1 / (len(Inquries) + truenum)
				trueprob = trueprob * k

				if (fields[i] in Inquriesf):
					k = (Inquriesf[fields[i]] + 1) / (len(Inquriesf) + falsenum)
				else:
					k = 1 / (len(Inquriesf) + falsenum)
				falseprob = falseprob * k

			elif (i == "Delinquencies (Last 2 yrs)"):
				if (fields[i] in Delinquencies):
					k = (Delinquencies[fields[i]] + 1) / (len(Delinquencies) + truenum)
				else:
					k = 1 / (len(Delinquencies) + truenum)
				trueprob = trueprob * k

				if (fields[i] in Delinquenciesf):
					k = (Delinquenciesf[fields[i]] + 1) / (len(Delinquenciesf) + falsenum)
				else:
					k = 1 / (len(Delinquenciesf) + falsenum)
				falseprob = falseprob * k

			# elif (i == "Public Records On File"):
			# 	if (fields[i] in Records):
			# 		k = (Records[fields[i]] + 1) / (len(Records) + truenum)
			# 	else:
			# 		k = 1 / (len(Records) + truenum)
			# 	trueprob = trueprob * k

			# 	if (fields[i] in Recordsf):
			# 		k = (Recordsf[fields[i]] + 1) / (len(Recordsf) + falsenum)
			# 	else:
			# 		k = 1 / (len(Recordsf) + falsenum)
			# 	falseprob = falseprob * k

			elif (i == "Education"):
				if (len(fields[i]) != 0):
					m = 1
				else:
					m = 0

				if (m in Education):
					k = (Education[m] + 1) / (len(Education) + truenum)
				else:
					k = 1 / (len(Education) + truenum)
				trueprob = trueprob * k
				#print(k)

				if (m in Educationf):
					k = (Educationf[m] + 1) / (len(Educationf) + falsenum)
				else:
					k = 1 / (len(Educationf) + falsenum)
				falseprob = falseprob * k

			elif (i == "Employment Length"):
				if (fields[i] in Working):
					k = (Working[fields[i]] + 1) / (len(Working) + truenum)
				else:
					k = 1 / (len(Working) + truenum)
				trueprob = trueprob * k

				if (fields[i] in Workingf):
					k = (Workingf[fields[i]] + 1) / (len(Workingf) + falsenum)
				else:
					k = 1 / (len(Workingf) + falsenum)
				falseprob = falseprob * k

			elif (i == "Months Since Last Delinquency"):
				if (fields[i] in LastDelinquency):
					k = (LastDelinquency[fields[i]] + 1) / (len(LastDelinquency) + truenum)
				else:
					k = 1 / (len(LastDelinquency) + truenum)
				trueprob = trueprob * k

				if (fields[i] in LastDelinquencyf):
					k = (LastDelinquencyf[fields[i]] + 1) / (len(LastDelinquencyf) + falsenum)
				else:
					k = 1 / (len(LastDelinquencyf) + falsenum)
				falseprob = falseprob * k

			# elif (i == "Earliest CREDIT Line"):
			# 	m = fields[i].split('/')
			# 	if (len(m) == 3):
			# 		v = 10 - int(m[2][0])

			# 		if (v in Earliest):
			# 			k = (Earliest[v] + 1) / (len(Earliest) + truenum)
			# 		else:
			# 			k = 1 / (len(Earliest) + truenum)
			# 		trueprob = trueprob * k

			# 		if (v in Earliestf):
			# 			k = (Earliestf[v] + 1) / (len(Earliestf) + falsenum)
			# 		else:
			# 			k = 1 / (len(Earliestf) + falsenum)
			# 		falseprob = falseprob * k
			# 		#print(k)

		if (trueprob > falseprob):
			ally.append(1)
		else:
			ally.append(0)

with open('output.csv', 'w') as csvfile:
    fieldnames = ['Loan ID', 'Status (Fully Paid=1, Not Paid=0)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range (len(ally)):
    	writer.writerow({'Loan ID': allid[i], 'Status (Fully Paid=1, Not Paid=0)': ally[i]})

