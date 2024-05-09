from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class Info(models.Model):
    username = models.CharField(
        max_length=50,
        help_text="Username",
        unique=True
    )
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    instagram_name = models.CharField(max_length=255, blank=True, null=True)
    telegram_name = models.CharField(max_length=255, blank=True, null=True)
    facebook_name = models.CharField(max_length=255, blank=True, null=True)
    tiktok_name = models.CharField(max_length=255, blank=True, null=True)
    website_name = models.CharField(max_length=255, blank=True, null=True)
    instagram_link = models.CharField(max_length=255, blank=True, null=True)
    telegram_link = models.CharField(max_length=255, blank=True, null=True)
    facebook_link = models.CharField(max_length=255, blank=True, null=True)
    contanct_number = models.CharField(max_length=255, blank=True, null=True)
    tiktok_link = models.CharField(max_length=255, blank=True, null=True)
    website_link = models.CharField(max_length=255, blank=True, null=True)

    qr_code = models.ImageField(upload_to="qr_code/", blank=True)

    def save(self, *args, **kwargs):
        url = f"http://10.40.0.88:8000/{self.username}/"

        qrcode_img = qrcode.make(url)
        canvas = Image.new("RGB", (350,350), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.username}' + '.png'
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.username



