# Lesson 21 – Architektura Dockera i mikroserwisów

Repozytorium zawiera rozwiązania zadań z lekcji dotyczącej architektury Dockera, pracy z woluminami, sieciami Docker oraz analizy kontenerów.

## Zadanie 1 – Aplikacja wielokontenerowa

Celem zadania było utworzenie aplikacji składającej się z dwóch kontenerów:

- kontener z bazą danych PostgreSQL
- kontener z aplikacją webową Flask

### Wykorzystane technologie

- Docker
- Docker network
- Docker volume
- Python (Flask)
- PostgreSQL

### Funkcjonalność aplikacji

Aplikacja webowa umożliwia:

- sprawdzenie stanu aplikacji (`/health`)
- zapisanie wiadomości do bazy danych (`/write`)
- wyświetlenie zapisanych wiadomości (`/list`)

Kontenery komunikują się ze sobą za pomocą sieci Docker.

Dane bazy danych są przechowywane w nazwanym woluminie Docker, co zapewnia trwałość danych.

---

## Zadanie 2 – Analiza i debugowanie aplikacji Docker (Nginx)

Celem zadania było uruchomienie kontenera z serwerem Nginx oraz analiza jego działania.

### Wykonane kroki

- uruchomienie kontenera Nginx
- analiza konfiguracji kontenera za pomocą polecenia `docker inspect`
- generowanie ruchu HTTP (200, 404, 500)
- analiza logów kontenera przy użyciu `docker logs`
- przygotowanie raportu z wynikami analizy

### Wnioski

- Docker umożliwia łatwe uruchamianie aplikacji w izolowanych kontenerach
- polecenie `docker inspect` pozwala analizować konfigurację kontenerów
- polecenie `docker logs` umożliwia debugowanie działania aplikacji

## Struktura projektu
