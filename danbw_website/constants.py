from django.utils.translation import gettext_lazy as _

# Documentation for defining choices for CharFields:
# https://docs.djangoproject.com/en/4.2/ref/models/fields/#choices
# Assign increasing integer values to a list of variables:
# https://stackoverflow.com/a/64485228
(
    RED_BELT,
    SIXTH_KYU,
    FIFTH_KYU,
    FOURTH_KYU,
    THIRD_KYU,
    SECOND_KYU,
    FIRST_KYU,
    SHODAN,
    NIDAN,
    SANDAN,
    YONDAN,
    GODAN,
    ROKUDAN,
) = range(13)

(
    BANK,
    CASH,
) = range(2)

PAYMENT_STATUS = ((0, _("Unpaid")), (1, _("Paid")))

PAYMENT_METHODS = (
    (BANK, _("Bank Transfer")),
    (CASH, _("Cash")),
)

EXAM_GRADE_CHOICES = (
    (SIXTH_KYU, _("6th Kyu ⚪️")),
    (FIFTH_KYU, _("5th Kyu 🟡")),
    (FOURTH_KYU, _("4th Kyu 🟠")),
    (THIRD_KYU, _("3rd Kyu 🟢")),
    (SECOND_KYU, _("2nd Kyu 🔵")),
    (FIRST_KYU, _("1st Kyu 🟤")),
)

GRADE_CHOICES = (
    (RED_BELT, _("Red Belt 🔴")),
    (SIXTH_KYU, _("6th Kyu ⚪️")),
    (FIFTH_KYU, _("5th Kyu 🟡")),
    (FOURTH_KYU, _("4th Kyu 🟠")),
    (THIRD_KYU, _("3rd Kyu 🟢")),
    (SECOND_KYU, _("2nd Kyu 🔵")),
    (FIRST_KYU, _("1st Kyu 🟤")),
    (SHODAN, _("1st Dan ⚫️")),
    (NIDAN, _("2nd  Dan ⚫️")),
    (SANDAN, _("3rd Dan ⚫️")),
    (YONDAN, _("4th Dan ⚫️")),
    (GODAN, _("5th Dan ⚫️")),
    (ROKUDAN, _("6th Dan ⚫️")),
)

DOJO_CHOICES = (
    ("", _("Select your Dojo")),
    ("AAR", "Aikido am Rhein"),
    ("AVE", "Aikido Verein Emmendingen"),
    ("AVF", "Aikido Verein Freiburg"),
    ("TVD", "Turnverein Denzlingen"),
    ("other", _("Other Dojo")),
)

WEEKDAYS = (
    (0, _("Monday")),
    (1, _("Tuesday")),
    (2, _("Wednesday")),
    (3, _("Thursday")),
    (4, _("Friday")),
    (5, _("Saturday")),
    (6, _("Sunday")),
)

MEMBERSHIP_TYPES = (
    ("dan_international", _("D.A.N. International Membership")),
    ("childrens_passport", _("Childrens Passport")),
    ("danbw", _("D.A.N. BW Membership")),
)

MEMBERSHIP_FEES = (
    ("dan_international", 35),
    ("dan_int_2nd_quarter", 31),
    ("dan_int_3rd_quarter", 27),
    ("dan_int_4th_quarter", 23),
    ("childrens_passport", 15),
    ("danbw", 5),
)

COURSE_TYPES = (
    ("sensei_emmerson", _("Sensei Emmerson")),
    ("hombu_dojo", _("Hombu Dojo Instructor")),
    ("external_teacher", _("External Teacher")),
    ("dan_bw_teacher", _("D.A.N. BW Teacher")),
    ("children", _("Children")),
)

INTERNATIONAL_COURSES = [
    "sensei_emmerson",
    "hombu_dojo",
    "external_teacher",
]

EXAM_COURSES = [
    "sensei_emmerson",
    "external_teacher",
    "dan_bw_teacher",
]

DAN_PREPARATION_COURSES = [
    "sensei_emmerson",
    "external_teacher",
]

FEE_CATEGORIES = (
    ("regular", _("Regular Course")),
    ("dan_seminar", _("Dan Seminar")),
)
