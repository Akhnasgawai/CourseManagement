from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Course, CourseContent


class UserRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES, widget=forms.Select, initial="student"
    )
    email = forms.EmailField(max_length=255, label="Email")
    username = forms.CharField(max_length=50, label="Username")

    class Meta:
        model = User
        fields = ["email", "username", "role"]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        role = cleaned_data.get("role")

        # Check if the email is already registered with a student or teacher role
        if User.objects.filter(email=email, role__in=["student", "teacher"]).exists():
            existing_roles = User.objects.filter(email=email).values_list(
                "role", flat=True
            )

            # If the email is already registered as a student, only allow registration as a teacher
            if "student" in existing_roles and role == "student":
                raise forms.ValidationError(
                    "This email is already registered as a student."
                )

            # If the email is already registered as a teacher, only allow registration as a student
            if "teacher" in existing_roles and role == "teacher":
                raise forms.ValidationError(
                    "This email is already registered as a teacher."
                )
        
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes to input fields
        self.fields["email"].widget.attrs["placeholder"] = " "
        self.fields["username"].widget.attrs["placeholder"] = " "
        self.fields["password1"].widget.attrs["placeholder"] = " "
        self.fields["password2"].widget.attrs["placeholder"] = " "
        self.fields["role"].widget.attrs["placeholder"] = " "

class UserLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        widget=forms.Select,
        initial="student",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes to input fields
        self.fields["email"].widget.attrs["class"] = "login_username"
        self.fields["email"].widget.attrs["placeholder"] = " "
        self.fields["password"].widget.attrs["class"] = "login_password"
        self.fields["password"].widget.attrs["placeholder"] = " "
        self.fields["role"].widget.attrs["class"] = "login_role"
        self.fields["role"].widget.attrs["placeholder"] = " "


class AddCourseForm(forms.Form):
    title = forms.CharField(max_length=50, label="Title")
    description = forms.CharField(max_length=200, label="Description")
    price = forms.IntegerField(label="Price")

    class Meta:
        model = Course
        fields = ("title", "description", "price")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes to input fields
        self.fields["title"].widget.attrs["class"] = "course_title"
        self.fields["title"].widget.attrs["placeholder"] = " "
        self.fields["description"].widget.attrs["class"] = "course_description"
        self.fields["description"].widget.attrs["placeholder"] = " "
        self.fields["price"].widget.attrs["class"] = "course_price"
        self.fields["price"].widget.attrs["placeholder"] = " "

class AddCourseContentForm(forms.Form):
    content_title = forms.CharField(max_length=200, label="Content Title")
    content = forms.CharField(max_length=500, label="Content Description")
    content_link = forms.CharField(max_length=500, label="Content Link")
    course_id = forms.CharField(max_length=500, label="Course")

    class Meta:
        model = CourseContent
        fields = ("content_title", "content", "course_id", "content_link")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes to input fields
        self.fields["content_title"].widget.attrs["class"] = "course_title"
        self.fields["content_title"].widget.attrs["placeholder"] = " "
        self.fields["content"].widget.attrs["class"] = "content_description"
        self.fields["content"].widget.attrs["placeholder"] = " "
        self.fields["course_id"].widget.attrs["class"] = "course_price"
        self.fields["course_id"].widget.attrs["placeholder"] = " "
        self.fields['course_id'].widget.attrs['disabled'] = True

class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        password = self.data.get("password")
        confirm_password = self.data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password must match.")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom classes to input fields
        self.fields["password"].widget.attrs["placeholder"] = " "
        self.fields["confirm_password"].widget.attrs["placeholder"] = " "
