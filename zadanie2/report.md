# Zadanie domowe 2 – Analiza i debugowanie aplikacji Docker (Nginx)

## 1. Polecenia użyte do utworzenia kontenera
Uruchomienie kontenera:
sudo docker run -d --name web-server -p 8080:80 nginx

## 2. Analiza konfiguracji kontenera (docker inspect)
Zapis wyniku inspekcji do pliku:
sudo docker inspect web-server > inspect.json

Adres IP kontenera (bridge):
sudo docker inspect -f '{{(index .NetworkSettings.Networks "bridge").IPAddress}}' web-server

## 3. Generowanie ruchu (200 / 404 / 500)
200:
curl -I http://localhost:8080/

404:
curl -I http://localhost:8080/nonexistent

500:
Najpierw dodano regułę do konfiguracji Nginx (default.conf) i wykonano reload:
sudo docker exec web-server sh -c 'sed -i "/server {/a\    location = /500 { return 500; }\n" /etc/nginx/conf.d/default.conf && nginx -s reload'

Następnie:
curl -I http://localhost:8080/500

## 4. Analiza logów (docker logs)
Polecenia:
sudo docker logs web-server
sudo docker logs --tail 50 web-server

Wyniki (przykłady):
- /nonexistent zwraca 404 i w logach pojawia się informacja o braku pliku
- /500 zwraca 500 i w logach widać wpis z kodem 500

## 5. Wnioski dotyczące działania aplikacji
- Kontener Nginx działa poprawnie i jest dostępny z hosta przez port 8080.
- `docker inspect` pozwala sprawdzić konfigurację (sieć, porty, obraz).
- `docker logs` umożliwia debugowanie odpowiedzi HTTP (404/500) i zdarzeń Nginx.

## 6. Propozycje optymalizacji konfiguracji
- Skonfigurować niestandardowy format logów (log_format) i centralizację logów.
- Skonfigurować rotację logów.
- Użyć woluminu do przechowywania logów na hoście (bonus).
- Dodać politykę restartu kontenera: `--restart unless-stopped`.

