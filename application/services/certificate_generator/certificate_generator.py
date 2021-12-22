# Imports Required Packages from PIL
from PIL import Image, ImageDraw, ImageFont
import os
import datetime
from firebase_admin import credentials, initialize_app, storage

# Init firebase with credentials
cred = credentials.Certificate("application/services/certificate_generator/ubademy-mobile-ae5a598939c9.json")
initialize_app(cred, {"storageBucket": "ubademy-mobile.appspot.com"})

# Defining pixels in template
START_NAME_POS = 1108
END_NAME_POS = 1824
START_Y_NAME_POS = 530

START_DATE_POS = 1531
END_DATE_POS = 1857
START_Y_DATE_POS = 1197

START_COURSE_POS = 1066
END_COURSE_POS = 1867
START_Y_COURSE_POS = 863


class CertificateGenerator:
    @classmethod
    def create_certificate(self, user_name: str, course_name: str, id: str):
        template = Image.open("application/services/certificate_generator/template-certificate.png")

        img_rgb = Image.new("RGB", template.size, (255, 255, 255))
        img_rgb.paste(template, mask=template.split()[3])
        draw = ImageDraw.Draw(img_rgb)

        text_color = (0, 0, 0)

        # NAME
        font = ImageFont.truetype("application/services/certificate_generator/CoreSansC-35Light.ttf", 50, encoding="unic")
        font_date = ImageFont.truetype("application/services/certificate_generator/CoreSansC-35Light.ttf", 50, encoding="unic")
        name_w, name_h = draw.textsize(user_name, font)

        location_name = (START_NAME_POS + ((END_NAME_POS - START_NAME_POS) - name_w) / 2, START_Y_NAME_POS - 60)
        draw.text(location_name, user_name, fill=text_color, font=font)

        # DATE
        date = datetime.datetime.now()
        date_str = date.strftime("%d/%m/%Y")
        date_w, date_h = draw.textsize(date_str, font)
        location_date = (START_DATE_POS + ((END_DATE_POS - START_DATE_POS) - date_w) / 2, START_Y_DATE_POS - 60)
        draw.text(location_date, date_str, fill=text_color, font=font_date)

        # COURSE
        course_w, course_h = draw.textsize(course_name, font)
        location_course = (START_COURSE_POS + ((END_COURSE_POS - START_COURSE_POS) - course_w) / 2, START_Y_COURSE_POS - 70)
        draw.text(location_course, course_name, fill=text_color, font=font)
        # SAVE
        path = "application/services/certificate_generator/output/" + user_name + "-" + str(id) + ".pdf"
        img_rgb.save(path)
        bucket = storage.bucket()
        blob = bucket.blob(path)
        blob.upload_from_filename(path)
        blob.make_public()

        # DELETE
        os.remove("application/services/certificate_generator/output/" + user_name + "-" + str(id) + ".pdf")
        return blob.public_url
