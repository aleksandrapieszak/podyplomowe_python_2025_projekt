# Projekt Django: Aplikacja do udostępniania prac naukowych

## Opis
Aplikacja internetowa umożliwia użytkownikom dzielenie się swoimi pracami naukowymi z innymi użytkownikami.

## Instalacja
### 1. Sklonuj repozytorium
```sh
 git clone https://github.com/aleksandrapieszak/podyplomowe_python_2025_projekt
 cd podyplomowe_python_2025_projekt
```

### 2. Utwórz i aktywuj środowisko wirtualne (venv)
#### Utworzenie środowiska:
```sh
python -m venv .venv
```
#### Aktywacja:
- **Windows (cmd):**
  ```sh
  .\.venv\Scripts\activate.bat
  ```
- **Windows (PowerShell, domyślny dla PyCharm):**
  ```sh
  .\.venv\Scripts\Activate.ps1
  ```

### 3. Zainstaluj wymagane pakiety
```sh
pip install -r requirements.txt
```

### 4. Instalacja i konfiguracja bazy danych PostgreSQL (jednorazowo)
#### Instalacja PostgreSQL
Pobierz i zainstaluj PostgreSQL, korzystając z tego poradnika: [YouTube - Instalacja PostgreSQL](https://www.youtube.com/watch?v=sCsreF6nrmI). 
Podczas instalacji zostaniesz poproszony o ustawienie hasła dla superużytkownika – zapamiętaj je.

#### Konfiguracja PostgreSQL
1. **Utwórz użytkownika i bazę danych**:
   - Otwórz aplikację do zarządzania serverem PostgreSQL `pgAdmin 4`.
   - Rozwiń `Servers` > `Login/Group Roles`, kliknij prawym przyciskiem i wybierz **Create -> Login/Group Role...**.
   - W zakładce **General** wpisz `admin` jako nazwę użytkownika.
   - W zakładce **Definition** ustaw hasło: `projectdjango`.
   - W zakładce **Privileges** włącz wszystkie uprawnienia i kliknij **Save**.
   
2. **Utwórz bazę danych**:
   - Kliknij prawym przyciskiem na `Databases` > **Create -> Database...**.
   - W polu **Database** wpisz: `project_db`.
   - W polu **Owner** wybierz `admin`, kliknij **Save**.

3. **Upewnij się, że konfiguracja bazy danych zgadza się z ustawieniami w `settings.py`**.

### 5. Uruchom migracje
```sh
python manage.py migrate
```
Po wykonaniu tego kroku baza danych `project_db` zostanie uzupełniona o wymagane tabele.

## Uruchomienie projektu
Aby uruchomić serwer deweloperski Django:
```sh
python manage.py runserver
```

Teraz aplikacja będzie dostępna pod adresem: `http://127.0.0.1:8000/`.

