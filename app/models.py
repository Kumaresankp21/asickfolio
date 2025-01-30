from django.db import models

class About(models.Model):
    name = models.CharField(max_length=100)  # Full name
    age = models.PositiveIntegerField()  # Age
    height = models.CharField(max_length=10)  # Example: '5\'5"'
    weight = models.CharField(max_length=10)  # Example: '60kg'
    nationality = models.CharField(max_length=50)  # Nationality
    languages = models.CharField(max_length=100)  # Comma-separated languages
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # Profile picture
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)  # Optional resume

    def __str__(self):
        return f"About {self.name}"

# Model for Education Section
class Education(models.Model):
    degree = models.CharField(max_length=255)  # Example: "B.E. in Computer Science"
    institution = models.CharField(max_length=255)  # Example: "Kings College of Engineering"
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)  # CGPA/Percentage
    start_year = models.PositiveIntegerField()  # Start year of education
    end_year = models.PositiveIntegerField()  # Expected/actual end year
    description = models.TextField(blank=True, null=True)  # Any additional information about the degree (optional)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

# Model for School Education Details (like 12th, 10th grade, etc.)
class SchoolEducation(models.Model):
    grade = models.CharField(max_length=50)  # Example: "12th Grade"
    school = models.CharField(max_length=255)  # Example: "St. Marcina's Hr. Sec. School"
    percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Percentage achieved
    year = models.PositiveIntegerField()  # Year of completion

    def __str__(self):
        return f"{self.grade} at {self.school}"
    
class Skill(models.Model):
    name = models.CharField(max_length=100)  # Name of the skill (e.g., HTML, CSS, etc.)
    image = models.ImageField(upload_to='skills_images/')  # Image for the skill icon

    def __str__(self):
        return self.name
    
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)  # Title of the project
    description = models.TextField()  # Detailed description of the project
    technologies = models.TextField(blank=True, null=True)  # Technologies used (optional)
    link = models.URLField(blank=True, null=True)  # URL to the project or platform (optional)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)  # Image for the project (optional)
    
    def __str__(self):
        return self.title
    

class CertificateCategory(models.Model):
    name = models.CharField(max_length=100)  # Category name (e.g., MongoDB, Infosys, DevOps)
    description = models.TextField(blank=True, null=True)  # Optional description for the category

    def __str__(self):
        return self.name

class Certificate(models.Model):
    category = models.ForeignKey(
        CertificateCategory, 
        related_name="certificates",  # This allows access to related certificates via category.certificates
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)  # Title of the certificate
    description = models.TextField()  # Description of the certificate (e.g., "Introduction to MongoDB")
    image = models.ImageField(upload_to='certificates/')  # The certificate image (uploaded to 'certificates/' folder)

    def __str__(self):
        return self.title
