from django.db import models

# Create your models here.
class BankLone(models.Model):

    gender_choices = [('Male', 'Male'), ('Female', 'Female')]
    marride_choices = [('Yes', 'Yes'), ('No', 'No')]
    selfemployed_choices = [('Yes', 'Yes'), ('No', 'No')]
    education_choices = [('Graduate', 'Graduate'), ('Not Graduate', 'Not Graduate')]
    property_choices = [('Urban', 'Urban'), ('Rural', 'Rural'), ('Semiurban', 'Semiurban')]

    Loan_ID = models.CharField(max_length=20, null=True)
    Dependents = models.IntegerField(null=True, blank=True)
    Gender = models.CharField(max_length=6,null=True, choices=gender_choices)
    Married = models.CharField(max_length=3,null=True, choices=marride_choices)
    Education = models.CharField(max_length=15, choices=education_choices)
    Self_Employed = models.CharField(max_length=3, choices=selfemployed_choices,null=True, blank=True)
    ApplicantIncome = models.IntegerField(null=True)
    CoapplicantIncome = models.IntegerField(null=True)
    LoanAmount = models.IntegerField(null=True, blank=True)
    Loan_Amount_Term = models.IntegerField(null=True, blank=True)
    Credit_History = models.IntegerField(null=True, blank=True)
    Property_Area = models.CharField(max_length=10, choices=property_choices)
    Loan_Status = models.IntegerField(null=True, blank=True)
    
    def to_dict(self):
        return {
            "Loan_ID":self.Loan_ID,
            "Gender":self.Gender,
            "Married":self.Married,
            "Dependents":self.Dependents,
            "Education":self.Education,
            "Self_Employed":self.Self_Employed,
            "ApplicantIncome":self.ApplicantIncome,
            "CoapplicantIncome":self.CoapplicantIncome,
            "LoanAmount":self.LoanAmount,
            "Loan_Amount_Term":self.Loan_Amount_Term,
            "Credit_History":self.Credit_History,
            "Property_Area":self.Property_Area,
            "Loan_Status":self.Loan_Status
        }

