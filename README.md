# Установка окружения и запуск тестов

### Обязательные требования: python, allure, pip

## Установка pip (для windows)

1. Установить [python](https://www.python.org/)
2. Скачать [установочный скрипт get-pip.py](https://bootstrap.pypa.io/get-pip.py).
   Щелкнуть правой кнопкой мыши на ссылке и нажать “Сохранить как…”.
3. Открыть командную строку, перейдите к каталогу с файлом get-pip.py и
   запустить ``` python get-pip.py ```.

## Установка allure (для windows)

1. Для начала необходимо установить [scoop](https://scoop.sh/)
2. Установить allure командой ``` scoop install allure ```

## Установка виртуального окружения

1. Установить virtualenv: ``` pip install virtualenv ```
2. Перейти в папку с проектом
3. Создать виртуальное окружение: ``` python -m venv venv ``` 
4. Активировать виртуальное окружение: ``` venv\Scripts\activate ``` 
5. Установить зависимости: ``` pip install -r requirements.txt ```

## Запуск тестов

1. Запуск тестов ``` pytest --alluredir=<папка для результатов> ./tests ``` 
или ``` pytest -s -v --alluredir=allure-report --host=local tests/ ```
```--host=local``` локально(default), ```--host=remote``` в локальном selenoid,
```--host={hostname}``` на удаленном хосте
```-n 4``` параметр для параллельного запуска(4 потока)

2. Генерация отчета ``` allure serve <папка для результатов> ```

## Установка SELENOID (для windows)

1. Скачать утилиту https://github.com/aerokube/cm/releases/tag/1.8.1
2. В командной строке выполнить команду ``` ./cm_windows_amd64 selenoid start --vnc ```
3. В командной строке выполнить команду ``` ./cm_windows_amd64 selenoid-ui start ```

Подробнее здесь можно почитать https://aerokube.com/selenoid/latest/#_start_selenoid

