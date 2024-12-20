from django.db import models


class Bicycle(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    brand = models.CharField(max_length=30)  # eg Trek
    line = models.CharField(max_length=100)  # eg Slash
    model = models.CharField(max_length=30)  # eg 9.9 or SE
    generation = models.CharField(max_length=30, blank=True, null=True)  # eg gen 6
    description = models.CharField(max_length=1000)
    year_production = models.IntegerField()
    color_primary = models.CharField(max_length=30)
    color_secondary = models.CharField(max_length=30, blank=True, null=True)
    FRAME_SIZE_CHOICES = [
        ("XS", "XS"),
        ("S", "S"),
        ("S/M", "S/M"),
        ("M", "M"),
        ("M/L", "M/L"),
        ("L", "L"),
        ("XL", "XL"),
    ]
    frame_size = models.CharField(max_length=3, choices=FRAME_SIZE_CHOICES)
    FRAME_MATERIAL = [
        ("carbon", "Carbon"),
        ("steel", "Steel"),
        ("aluminium", "Aluminium"),
        ("titanium", "Titanium"),
    ]
    frame_material = models.CharField(max_length=9, choices=FRAME_MATERIAL)
    WHEEL_SIZE_CHOICES = [
        (24.0, "24"),
        (26.0, "26"),
        (27.5, "27.5"),
        (29.0, "29"),
    ]
    wheel_size = models.FloatField(choices=WHEEL_SIZE_CHOICES)
    tire_size_width = models.FloatField()
    BICYCLE_PURPOSE_CHOICES = [
        ("mtb", "Mountain"),
        ("road", "Road"),
        ("gravel", "Gravel"),
        ("city", "City"),
    ]
    purpose = models.CharField(max_length=30, choices=BICYCLE_PURPOSE_CHOICES)
    # BICYCLE_CATEGORIES = []
    # category = models.CharField(max_length=30)
    suspension_front = models.BooleanField(default=True)
    suspension_back = models.BooleanField(default=True)
    weight = models.FloatField()

    is_available = models.BooleanField(default=True)
    is_serviceable = models.BooleanField(default=False)
    is_electric = models.BooleanField(default=False)
    prize_buy = models.FloatField()
    prize_rent = models.FloatField()

    # TODO: autoedit added images
    image_main = models.ImageField(default="default.png", upload_to="main_bike_image")

    def __str__(self) -> str:
        return f"{self.brand} {self.line} {self.model}"
