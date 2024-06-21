# Импорт моделей Django
from your_app_name.models import Driver, Penalty, Officer

# Функционал для водителя
def view_driver_violations(driver_license_number):
    # Получение списка нарушений для конкретного водителя
    violations = Penalty.objects.filter(driver__license_number=driver_license_number)
    return violations

def edit_driver_profile(driver_license_number, new_address, new_phone):
    # Редактирование профиля водителя
    driver = Driver.objects.get(license_number=driver_license_number)
    driver.address = new_address
    driver.phone = new_phone
    driver.save()

# Функционал для офицера
def view_all_violations():
    # Получение всех нарушений
    violations = Penalty.objects.all()
    return violations

def issue_penalty(driver_license_number, violation_code, violation_date, violation_time, area, fine_amount, fine_paid, license_suspension, base_amount, officer_id):
    # Выдача нового нарушения водителю
    officer = Officer.objects.get(id=officer_id)
    driver = Driver.objects.get(license_number=driver_license_number)
    penalty = Penalty.objects.create(
        driver=driver,
        violation_code=violation_code,
        violation_date=violation_date,
        violation_time=violation_time,
        area=area,
        fine_amount=fine_amount,
        fine_paid=fine_paid,
        license_suspension=license_suspension,
        base_amount=base_amount,
        officer=officer
    )
    return penalty

# Функционал для администратора
def add_officer(first_name, last_name, badge_number):
    # Добавление нового офицера
    officer = Officer.objects.create(first_name=first_name, last_name=last_name, badge_number=badge_number)
    return officer

def delete_officer(officer_id):
    # Удаление офицера по ID
    Officer.objects.filter(id=officer_id).delete()

def view_all_drivers():
    # Получение списка всех водителей
    drivers = Driver.objects.all()
    return drivers
