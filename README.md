# Lesson 21 – Architektura Dockera i mikroserwisów

Repozytorium zawiera rozwiązania zadań z lekcji dotyczącej Dockera.

## Zadanie 1 – Aplikacja wielokontenerowa

Utworzono aplikację składającą się z dwóch kontenerów:

- PostgreSQL (baza danych)
- Flask (aplikacja webowa)

Aplikacja zapisuje i odczytuje dane z bazy danych.  
Kontenery komunikują się ze sobą przez Docker network.  
Dane bazy są przechowywane w Docker volume.

## Zadanie 2 – Analiza kontenera Nginx

W zadaniu uruchomiono kontener Nginx i przeprowadzono jego analizę.

Wykonane czynności:

- uruchomienie kontenera Nginx
- analiza konfiguracji przy użyciu `docker inspect`
- generowanie ruchu HTTP (200, 404, 500)
- analiza logów za pomocą `docker logs`
- przygotowanie raportu z wynikami
