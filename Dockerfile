# Вибираємо базовий образ
FROM python:3.12

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файли проекту
COPY . .

# Встановлюємо необхідні залежності
RUN pip install -r requirements.txt

# Вказуємо команду за замовчуванням
CMD ["scrapy", "crawl", "quotes"]
