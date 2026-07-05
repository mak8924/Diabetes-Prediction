from django.shortcuts import render
import pandas as pd
import joblib
import os
import numpy as np

# تحميل النموذج (يتم تحميله مرة واحدة عند تشغيل السيرفر)
# الخاص بك joblib تأكدي أن المسار يوجه لمكان ملف
# في المجلد الرئيسي models سنفترض أن الملف موجود داخل مجلد
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models', 'diabetes_v1_female.joblib')
model = joblib.load(model_path)

def predict_diabetes(request):
    result = None

    if request.method == 'POST':
        # (HTML) استقبال البيانات من الفورم
        # ملاحظة: الأسماء في الـ name في الـ HTML يجب أن تطابق الـ (... 'pregnancies', 'glucose')
        pregnancies = float(request.POST.get('pregnancies'))
        glucose = float(request.POST.get('glucose'))
        blood_pressure = float(request.POST.get('blood_pressure'))
        skin_thickness = float(request.POST.get('skin_thickness'))
        insulin = float(request.POST.get('insulin'))
        bmi = float(request.POST.get('bmi'))
        pedigree = float(request.POST.get('diabetes_pedigree'))
        age = float(request.POST.get('age'))

        # 🛠️  تجهيز البيانات في DataFrame بأسماء الأعمدة
        data_dict = {
            'Pregnancies': [pregnancies],
            'Glucose': [glucose],
            'BloodPressure': [blood_pressure],
            'SkinThickness': [skin_thickness],
            'Insulin': [insulin],
            'BMI': [bmi],
            'DiabetesPedigree': [pedigree],
            'Age': [age]
        }
        
        input_data = pd.DataFrame(data_dict)

        # إجراء التنبؤ باستخدام الـ DataFrame
        prediction = model.predict(input_data)

        # تفسير النتيجة
        if prediction[0] == 1:
            result = "إيجابي: يرجى استشارة الطبيب"
        else:
            result = "سلبي: لا توجد مخاطر ظاهرة"

    # عرض الصفحة (سواء كانت زيارة أولى أو بعد ظهور النتيجة)
    return render(request, 'predict.html', {'result': result})