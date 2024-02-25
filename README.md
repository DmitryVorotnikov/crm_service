# CRM_service (EN)

## Project Description
CRM_service is a non-commercial open-source project, a web application CRM (Customer Relationship Management) FullREST API, backend for an electronics sales network.

## Project Idea
The main goal of the project is to create a convenient online platform for efficient interaction with customers, tracking contacts, managing sales, as well as analyzing customer data to improve sales and service strategies.

## Project Functionalities
- The application provides a Full REST API using Django Rest Framework.
- Authorization is done through the JSON Web Token (JWT) token mechanism.
- PostgresQL relational database is used for data storage.
- Supplier model, Product model, and custom User model.
- Automatic determination of the supplier's level in the network.
- Configuration setup for the administrative panel, including custom actions, filtering, and searching by model fields.
- The project uses Docker-compose for containerization, while servers are individually configured.
- CORS settings to ensure security.
- Utilization of Swagger and Redoc for API documentation according to the OpenAPI standard.
- Examples of environment variables for quick project deployment locally are provided in the `.env.sample` file.
- Project settings and dependencies can be found in the `requirements.txt` file.

## Running the Project:
1) In the project root, create a `.env` file following the example of the `.env.sample` file.
2) Enter `docker compose up --build` in the console.

# CRM_service (RUS)

## Описание проекта
CRM_service - некоммерческий open-source проект, веб-приложение CRM (Customer Relationship Management) FullREST API, бэкенд для сети по продаже электроники. 

## Идея проекта
Главная цель проекта — создать удобную онлайн-платформу для эффективного взаимодействия с клиентами, отслеживания контактов, управления продажами, а также анализа данных о клиентах для улучшения стратегий продаж и обслуживания.

## Функциональности проекта
- Приложение предоставляет Full REST API, используя Django Rest Framework.
- Авторизация осуществляется через механизм токенов JSON Web Token (JWT).
- Для хранения данных используется реляционная база данных PostgresQL.
- Модель поставщика (Supplier), модель продукта (Product) и кастомная модель пользователя (User).
- Автоматическое определение уровня поставщика в сети. 
- Настройка конфигурации для административной панели,включая кастомные actions, фильтрация и поиск по полям моделей.
- Проект использует Docker-compose для контейнеризации, при этом серверы настраивается индивидуально.
- Настройки CORS для обеспечения безопасности.
- Использование Swagger и Redoc для документации API по стандарту OpenAPI.
- Примеры переменных окружения для быстрого разворачивания проекта локально представлены в файле `.env.sample`.
- Настройки и зависимости проекта можно найти в файле `requirements.txt`.

## Запуск проекта:
1) В корне проекта создайте файл `.env` по образцу файла `.env.sample`.
2) Введите в консоль `docker compose up --build`
