from django.db import models

# Create your models here.
from django.urls import reverse

class Season(models.Model):
    Season_id = models.AutoField(primary_key=True)
    Season_name = models.CharField(max_length = 45, unique = True)

    # def __str__(self):
    #     return '%s-%s' % (self.year.year, self.period.period_name)
    #
    # def get_absolute_url(self):
    #     return reverse('courseinfo_semester_detail_urlpattern', kwargs={"pk": self.pk})
    #
    # def get_update_url(self):
    #     return reverse('courseinfo_semester_update_urlpattern', kwargs={'pk': self.pk})
    #
    # def get_delete_url(self):
    #     return reverse('courseinfo_semester_delete_urlpattern', kwargs={'pk': self.pk})

    # class Meta:
    #     ordering = ['year__year','period__period_sequence']
    #     unique_together = ('year','period')




class Department(models.Model):
    Department_id = models.AutoField(primary_key=True)
    Department_number = models.CharField(max_length=20)
    Department_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s-%s' % (self.Department_number, self.Department_name)

    # def get_absolute_url(self):
    #     return reverse('hospitalinfo_department_detail_urlpattern', kwargs={"pk": self.pk})
    #
    # def get_update_url(self):
    #     return reverse('hospitalinfo_department_update_urlpattern', kwargs={'pk': self.pk})
    #
    # def get_delete_url(self):
    #     return reverse('hospitalinfo_department_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['Department_number', 'Department_name']
        unique_together = (('Department_number', 'Department_name'),)


class Doctor(models.Model):
    Doctor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    def __str__(self):
        return '%s-%s' % (self.last_name, self.first_name)

    # def get_absolute_url(self):
    #     return reverse('courseinfo_instructor_detail_urlpattern', kwargs={'pk': self.pk})
    #
    # def get_update_url(self):
    #     return reverse('courseinfo_instructor_update_urlpattern', kwargs={'pk': self.pk})
    #
    # def get_delete_url(self):
    #     return reverse('courseinfo_instructor_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['last_name', 'first_name']
        unique_together = (('last_name', 'first_name'),)



class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    nickname = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.nickname == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s, (%s)' % (self.last_name, self.first_name, self.nickname)
        return result

    # def get_absolute_url(self):
    #     return reverse('courseinfo_student_detail_urlpattern', kwargs={"pk": self.pk})
    #
    # def get_update_url(self):
    #     return reverse('courseinfo_student_update_urlpattern', kwargs={'pk': self.pk})
    #
    # def get_delete_url(self):
    #     return reverse('courseinfo_student_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['last_name', 'first_name', 'nickname']
        unique_together = (('last_name', 'first_name', 'nickname'),)



class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=10)
    season = models.ForeignKey(Season, related_name='sections', on_delete=models.PROTECT)
    department = models.ForeignKey(Department, related_name='sections', on_delete=models.PROTECT)
    doctor = models.ForeignKey(Doctor, related_name='sections', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s (%s)' % (self.department.Department_number, self.section_name, self.season.__str__())

    # def get_absolute_url(self):
    #     return reverse('courseinfo_section_detail_urlpattern', kwargs={"pk": self.pk})
    #
    # def get_update_url(self):
    #     return reverse('courseinfo_section_update_urlpattern', kwargs={'pk': self.pk})
    #
    # def get_delete_url(self):
    #     return reverse('courseinfo_section_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['department__department_number', 'section_name', 'season__season_name']
        unique_together = (('season', 'department', 'section_name'),)

class Registration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, related_name='registrations', on_delete=models.PROTECT)
    section = models.ForeignKey(Section, related_name='registrations', on_delete=models.PROTECT)


    def __str__(self):
        return '%s / %s' % (self.section, self.patient)

    # def get_absolute_url(self):
    #     return reverse('hospitalinfo_registration_detail_urlpattern', kwargs={"pk": self.pk})
    #
    # def get_update_url(self):
    #     return reverse('hospitalinfo_registration_update_urlpattern', kwargs={'pk': self.pk})
    #
    # def get_delete_url(self):
    #     return reverse('hospitalinfo_registration_delete_urlpattern', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['section', 'patient']
        unique_together = (('section', 'patient'),)





