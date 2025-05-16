import queue  # Модуль для роботи з чергами
import time   # Модуль для роботи з часом (для імітації затримки)
import random # Модуль для генерування випадкових значень
import uuid   # Модуль для створення унікальних ідентифікаторів

def generate_request(request_queue):
    """Генерує нову заявку та додає її до черги"""
    # Створюємо унікальний ідентифікатор заявки (8 символів)
    request_id = str(uuid.uuid4())[:8]
    
    # Створюємо заявку як словник з різними даними
    request = {
        "id": request_id,                     # Унікальний ідентифікатор
        "timestamp": time.time(),             # Час створення заявки
        "description": f"Заявка #{request_id}", # Опис заявки
        "priority": random.choice(["Низький", "Середній", "Високий"])  # Випадковий пріоритет
    }
    
    # Додаємо заявку до черги
    request_queue.put(request)
    
    # Виводимо інформацію про створену заявку
    print(f"Створено заявку: {request['id']} (пріоритет: {request['priority']})")
    return request

def process_request(request_queue):
    """Обробляє заявку з черги"""
    # Перевіряємо, чи є заявки в черзі
    if not request_queue.empty():
        # Видаляємо (отримуємо) заявку з початку черги
        request = request_queue.get()
        
        # Симулюємо випадковий час обробки (від 0.5 до 2 секунд)
        processing_time = random.uniform(0.5, 2.0)
        print(f"Обробка заявки: {request['id']} (пріоритет: {request['priority']})")
        
        # Імітуємо затримку на обробку заявки
        time.sleep(processing_time)
        
        # Повідомляємо про завершення обробки
        print(f"Завершено заявку: {request['id']} за {processing_time:.2f} секунд")
        return True
    else:
        # Якщо черга порожня, повідомляємо про це
        print("Черга порожня. Очікування нових заявок...")
        return False

def main():
    # Створюємо чергу для заявок (FIFO - First In, First Out)
    service_queue = queue.Queue()
    
    print("Імітація роботи сервісного центру")
    print("----------------------------------")
    print("Команди: g - створити заявку, p - обробити заявку, q - вихід")
    
    # Головний цикл програми
    while True:
        # Отримуємо команду від користувача
        command = input("\nВведіть команду (g/p/q): ").lower()
        
        if command == 'g':
            # Генеруємо нову заявку
            generate_request(service_queue)
            # Виводимо поточний розмір черги
            print(f"Розмір черги: {service_queue.qsize()}")
        
        elif command == 'p':
            # Обробляємо заявку з черги
            process_request(service_queue)
            # Виводимо поточний розмір черги
            print(f"Розмір черги: {service_queue.qsize()}")
        
        elif command == 'q':
            # Виходимо з програми
            print("Завершення програми. До побачення!")
            break
        
        else:
            # Повідомляємо про невідому команду
            print("Невідома команда. Спробуйте знову.")

# Запускаємо програму, якщо файл виконується напряму
if __name__ == "__main__":
    main()
