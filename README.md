# System For Control Of Auto Parts



## Requirements
* Docker
* Docker Compose

## Первый запуск

1. Установка виртуального окружения

   MacOS/Linux/Windows:

   ```
   python -m venv venv
   ```
2. Активация виртуального окружения

   MacOS/Linux:

   ```
   source venv/bin/activate
   ```

   Windows:

   ```
   venv\Scripts\activate
   ```
3. Установка зависимостей

   MacOS/Linux/Windows:

   ```
   pip install -r requirements.txt
   ```
4. Запуск приложения

   * Запуск из локальной среды:
     ```
     python manage.py runserver --settings=shop.settings.local
     ```
   * Запуск из производственной среды:
     ```
     python manage.py runserver --settings=shop.settings.prod
     ```


