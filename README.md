# Тестовое задание для компании Турчанинов
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat-square&logo=FastAPI)](https://fastapi.tiangolo.com/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)  
  
Задание выполнялось для компании Турчанинов  
Реализация чата с самим с собой при помощи WebSockets  

## Для запуска проекта
* Склонировать репозиторий на локальную машину:
```
https://github.com/NIK-TIGER-BILL/test_task_Turchaninov
```
* Запустить сборку образа, находясь в директории проекта (не забудьте точку в конце, это адрес до Dockerfile'а):  
```
docker build -t self_chat .
```
* Запустить контейнер:
```
docker run -it -p 8000:8000 self_chat
```