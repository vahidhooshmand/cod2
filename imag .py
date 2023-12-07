from PIL import Image
import os

def compress_image(input_path, output_path, quality=85):
    try:
        # باز کردن تصویر
        image = Image.open(input_path)

        # ایجاد دایرکتوری خروجی اگر وجود نداشته باشد
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # ذخیره تصویر با کیفیت فشرده
        image.save(output_path, quality=quality)

        print(f"تصویر با کیفیت فشرده در مسیر {output_path} ذخیره شد.")
    except FileNotFoundError:
        print(f"خطا: فایل {input_path} یافت نشد.")
    except Exception as e:
        print(f"خطا: {e}")

# مثال استفاده
input_image_path = 'C:\\Users\\Pezhvak\\Desktop\\3.jpg'
output_image_path = 'C:\\Users\\Pezhvak\\Desktop\\compressed_image.jpg'

# تنظیمات دلخواه (می‌توانید تغییر دهید)
compression_quality = 85

# اجرای برنامه
compress_image(input_image_path, output_image_path, quality=compression_quality)
