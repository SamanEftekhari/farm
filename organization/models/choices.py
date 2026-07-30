from django.db import models


class OrganizationType(models.TextChoices):
    PRIVATE = "PRIVATE", "خصوصی"
    GOVERNMENT = "GOVERNMENT", "دولتی"
    COOPERATIVE = "COOPERATIVE", "تعاونی"
    UNIVERSITY = "UNIVERSITY", "دانشگاه"
    RESEARCH = "RESEARCH", "پژوهشی"