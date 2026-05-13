from django.db import models

class Register(models.Model):

    ROLE_CHOICES = (

        ('Donor','Donor'),
        ('Patient','Patient'),

    )

    BLOOD_GROUPS = (

        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-'),

    )

    name=models.CharField(max_length=100)

    email=models.EmailField(unique=True)

    phone=models.CharField(max_length=15)

    age=models.IntegerField()

    blood_group=models.CharField(max_length=5,choices=BLOOD_GROUPS)

    role=models.CharField(max_length=20,choices=ROLE_CHOICES)

    password=models.CharField(max_length=100)

    def __str__(self):

        return self.name


class BloodDonation(models.Model):

    donor_name=models.CharField(max_length=100)

    blood_group=models.CharField(max_length=5)

    hospital=models.CharField(max_length=100)

    city=models.CharField(max_length=100)

    donation_date=models.DateField()

    def __str__(self):

        return self.donor_name


class BloodRequest(models.Model):

    patient_name=models.CharField(max_length=100)

    blood_group=models.CharField(max_length=5)

    hospital=models.CharField(max_length=100)

    city=models.CharField(max_length=100)

    contact=models.CharField(max_length=15)

    status=models.CharField(max_length=20,default='Pending')

    def __str__(self):

        return self.patient_name