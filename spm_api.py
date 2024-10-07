import requests

# إعدادات API
api_url = "https://hp-lvl-get-token-free-fire-python-json.tiiny.io/"

# إعدادات Telegram
telegram_token = "7731363478:AAHsVlMbi9XI5tzcdIg2NJAr_APna9kNmKE"  # ضع هنا توكن البوت الخاص بك
chat_id = "1933020265"  # ضع هنا معرف الشات الخاص بك

# عدّاد عدد المرات التي تم فيها التشغيل
attempt_count = 1

while True:
    try:
        # جلب البيانات من الـ API
        print(f"Attempting to fetch data, attempt {attempt_count}")
        response = requests.get(api_url)
        
        # طباعة حالة الاستجابة
        
        # تحقق من حالة الاستجابة
        if response.status_code == 200:
            # جلب البيانات
            data = response.json()
            
            # تحضير الرسالة التي سيتم إرسالها
            message = f"Attempt {attempt_count}: Data from API: Good"
            
            # إرسال الرسالة إلى بوت تلغرام
            telegram_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
            payload = {
                'chat_id': chat_id,
                'text': message
            }
            
            telegram_response = requests.post(telegram_url, data=payload)
        else:
            print(f"Response content good")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # زيادة العدّاد
    attempt_count += 1