from datetime import date, timedelta

from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

from .models import Course, CourseRegistration, UserProfile


class CourseListTest(TestCase):
    """Tests for CourseList view"""

    def setUp(self):
        self.number_of_courses = 3
        for i in range(self.number_of_courses):
            self.course = Course.objects.create(
                title=f"Course {i}",
                slug=f"course-{i}",
                start_date=date.today(),
                end_date=date.today() + timedelta(days=1),
                registration_status=(0),
                course_fee=50,
            )

    def test_course_list_view(self):
        print("\ntest_course_list_view")
        courses = Course.objects.all()
        response = self.client.get("/courses/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "course_list.html")
        self.assertEqual(len(courses), self.number_of_courses)


class RegisterCourseTest(TestCase):
    """Tests for RegisterCourse view"""

    def setUp(self):
        self.course = Course.objects.create(
            title="Test course",
            slug="test-course",
            start_date=date.today(),
            end_date=date.today() + timedelta(days=1),
            registration_status=(1),
            course_fee=50,
        )
        # Test user login:
        # https://docs.djangoproject.com/en/3.2/topics/testing/tools
        # /#django.test.Client.force_login
        self.user = User.objects.create_user(
            username="test-user", password="testpassword"
        )
        self.client.force_login(self.user)

    def test_get_registration_form(self):
        print("\ntest_get_registration_form")
        response = self.client.get("/courses/register/test-course/")
        self.assertTemplateUsed(response, "register_course.html")
        self.assertEqual(response.status_code, 200)

    def test_user_is_registered_for_course(self):
        print("\ntest_user_is_registered_for_course")
        CourseRegistration.objects.create(
            user=self.user,
            course=self.course,
            final_fee=50,
            payment_status=0,
            accept_terms=True,
            exam=False,
            comment="Test comment",
        )
        # Test Redirect: https://stackoverflow.com/a/49353888
        response = self.client.get(f"/courses/register/{self.course.slug}/")
        self.assertRedirects(response, "/courses/", 302, 200)

    def test_post_valid_registration_form(self):
        print("\ntest_post_valid_registration_form")
        response = self.client.post(
            "/courses/register/test-course/",
            {
                "final_fee": 50,
                "accept_terms": True,
                "exam": False,
            },
        )
        self.assertRedirects(response, "/user/registrations/", 302, 200)
        course_registration = CourseRegistration.objects.all()
        self.assertEqual(len(course_registration), 1)

    def test_post_invalid_registration_form(self):
        print("\ntest_post_invalid_registration_form")
        response = self.client.post(f"/courses/register/{self.course.slug}/")
        self.assertRedirects(response, "/user/registrations/", 302, 200)
        registrations = CourseRegistration.objects.all()
        self.assertEqual(len(registrations), 0)


class CancelCourseRegistrationTest(TestCase):
    """Tests for CancelCouresRegistration view"""

    def setUp(self):
        self.course = Course.objects.create(
            title="Test course",
            slug="test-course",
            start_date=date.today(),
            end_date=date.today() + timedelta(days=1),
            registration_status=(1),
            course_fee=50,
        )
        self.user = User.objects.create_user(
            username="test-user", password="testpassword"
        )
        self.client.force_login(self.user)
        self.registration = CourseRegistration.objects.create(
            user=self.user,
            course=self.course,
            final_fee=50,
            payment_status=0,
            accept_terms=True,
            exam=False,
            comment="Test comment",
        )

    def test_cancel_course_registration(self):
        print("\ntest_cancel_course_registration")
        response = self.client.post(
            f"/user/registrations/cancel/{self.registration.pk}/"
        )
        self.assertRedirects(response, "/user/registrations/", 302, 200)
        registrations = CourseRegistration.objects.filter(
            pk=self.registration.pk
        )
        self.assertEqual(len(registrations), 0)

        # Test messages: https://stackoverflow.com/a/46865530
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            f"Your registration for {self.course.title} has been cancelled.",
            messages,
        )


class UpdateCourseRegistrationTest(TestCase):
    """Tests for UpdateCourseRegistration view"""

    def setUp(self):
        self.course = Course.objects.create(
            title="Test course",
            slug="test-course",
            start_date=date.today(),
            end_date=date.today() + timedelta(days=1),
            registration_status=(1),
            course_fee=50,
        )
        self.user = User.objects.create_user(
            username="test-user", password="testpassword"
        )
        self.client.force_login(self.user)
        self.registration = CourseRegistration.objects.create(
            user=self.user,
            course=self.course,
            final_fee=50,
            payment_status=0,
            accept_terms=True,
            exam=False,
            comment="Test comment",
        )

    def test_update_course_registration(self):
        print("\ntest_update_course_registration")
        response = self.client.post(
            f"/user/registrations/update/{self.registration.pk}/",
            {
                "exam": True,
                "final_fee": 50,
            },
        )

        self.assertRedirects(response, "/user/registrations/", 302, 200)
        registration = CourseRegistration.objects.get(pk=self.registration.pk)
        self.assertEqual(registration.exam, True)

        # Test messages: https://stackoverflow.com/a/46865530
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            f"Your registration for {self.course.title} has been updated.",
            messages,
        )


class UserProfileViewTest(TestCase):
    """Tests for UserProfileView view"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="test-user",
            password="testpassword",
        )
        self.client.force_login(self.user)

    def test_get_user_profile(self):
        print("\ntest_get_user_profile")
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            grade="ng",
        )
        response = self.client.get("/user/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "userprofile.html")

    def test_get_user_profile_form(self):
        print("\ntest_get_user_profile_form")
        response = self.client.get("/user/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "create_userprofile.html")

    def test_post_valid_user_profile_form(self):
        print("\ntest_post_valid_user_profile_form")
        response = self.client.post(
            "/user/profile/",
            {
                "username": "test_username",
                "first_name": "Test",
                "last_name": "User",
                "email": "test@mail.com",
                "grade": "ng",
            },
        )
        self.assertRedirects(response, "/user/profile/", 302, 200)

    def test_post_invalid_user_profile_form(self):
        print("\ntest_post_invalid_user_profile_form")
        response = self.client.post("/user/profile/")
        self.assertRedirects(response, "/user/profile/", 302, 200)


class UpdateUserProfileViewTest(TestCase):
    """Tests for UpdateUserProfile view"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="test-username",
            password="testpassword",
            first_name="Test",
            last_name="User",
            email="test@mail.com",
        )
        self.client.force_login(self.user)
        self.user_profile = UserProfile.objects.create(
            user=self.user, grade="ng"
        )

    def test_get_update_user_profile_form(self):
        print("\ntest_get_update_user_profile_form")
        response = self.client.get("/user/profile/update/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "update_userprofile.html")

    def test_post_valid_update_user_profile_form(self):
        print("\ntest_post_valid_update_user_profile_form")
        changed_data = {
            "username": "test_username_changed",
            "first_name": "Test_changed",
            "last_name": "User_changed",
            "email": "test_changed@mail.com",
            "grade": "6k",
        }
        response = self.client.post("/user/profile/update/", changed_data)
        user_profile = UserProfile.objects.get(user=self.user)
        user = user_profile.user

        self.assertRedirects(response, "/user/profile/", 302, 200)
        self.assertEqual(user_profile.user.username, changed_data["username"])
        self.assertEqual(user.first_name, changed_data["first_name"])
        self.assertEqual(user.last_name, changed_data["last_name"])
        self.assertEqual(user.email, changed_data["email"])
        self.assertEqual(user_profile.grade, changed_data["grade"])

    def test_post_invalid_user_profile_form(self):
        print("\ntest_post_invalid_user_update_profile_form")
        response = self.client.post("/user/profile/update/")
        self.assertRedirects(response, "/user/profile/", 302, 200)
