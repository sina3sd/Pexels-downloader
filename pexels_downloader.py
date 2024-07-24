import requests

# از کاربر لینک ویدئو را بگیرید
video_url = input("لطفاً لینک ویدئو از سایت Pexels را وارد کنید: ")

# استخراج شناسه ویدئو از لینک ورودی
video_id = video_url.split('-')[-1].strip('/')

# لینک دانلود مستقیم ویدئو
download_url = f'https://www.pexels.com/video/{video_id}/download'

# دانلود ویدئو
response = requests.get(download_url, stream=True)
if response.status_code == 200:
    # نام فایل خروجی بر اساس شناسه ویدئو
    output_file = f'{video_id}.mp4'
    with open(output_file, 'wb') as outfile:
        for chunk in response.iter_content(chunk_size=8192):
            outfile.write(chunk)
    print(f'ویدئو با موفقیت دانلود و در فایل {output_file} ذخیره شد.')
else:
    print('خطا در دانلود ویدئو.')
