Dept_A = {'Name': 'Shivi', 'Age': 23}
Dept_B = {'Height': 165}
Dept_C = {'BloodType': 'B+'}

# patient_profile = Dept_A | Dept_B | Dept_C
patient_profile = {}
patient_profile.update(Dept_A)
patient_profile.update(Dept_B)
patient_profile.update(Dept_C)

print(patient_profile)