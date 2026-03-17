# My_payments

Простой API для работы с платежами. 

## Стек технологий

- FastAPI
- PostgreSQL
- asyncpg
- Docker / Docker Compose 
- Pydantic 

## Возможности

- Создание платежа (POST /payments/)
- Получение списка платежей (GET /payments/)
- Получение платежа по ID (GET /payments/{id})
- Проверка здоровья (GET /health)

## Как запустить

1. Клонировать репозиторий
```
git clone https://github.com/poskrebish/payments-api.git

cd payments-api
```

2. Запустить проект
```
docker compose up -d --build
```

3. Проверить логи
```
docker logs payments_app -f
```

4. Открыть документацию
```
http://localhost:8000/docs
```

## Запуск проекта через Docker-образ

1. Скачать образ
```
docker pull ghcr.io/poskrebish/my_payments:latest
```
2. Запустить контейнер
```
docker run -p 8000:8000 ghcr.io/poskrebish/my_payments:latest
```
3. Открыть документацию
```
http://localhost:8000/docs
```

## Примеры запросов

Создать платеж
```
curl -X POST http://localhost:8000/payments/ \
  -H "Content-Type: application/json" \
  -d '{"user_id": 123, "amount": 1500.50, "status": "completed"}'
```

Получить список платежей
```
curl http://localhost:8000/payments/?limit=10
```

Получить платеж по ID
```
curl http://localhost:8000/payments/1
```

## Остановка
```
docker compose down
```
