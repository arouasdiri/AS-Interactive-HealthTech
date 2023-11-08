
# AS Interactive HealthTech

## Über das Projekt

Dieses Projekt fokussiert auf die Entwicklung eines Systems zur präzisen Identifizierung von 3D-Punkten in chirurgischen Anwendungen mithilfe der Intel RealSense Camera D415. Unter Einsatz von Python und einer MongoDB-Datenbank bietet das System chirurgischen Teams eine robuste und intuitive Plattform zur Erfassung und Verwaltung von Patienteninformationen. Eine Benutzeroberfläche, realisiert mit PyQt, sorgt für eine benutzerfreundliche Interaktion und macht das System ideal für den Einsatz in medizinischen Einrichtungen.

## Inhaltsverzeichnis

- [Installation und Setup](#installation-und-setup)
- [Abhängigkeiten und Voraussetzungen](#abhängigkeiten-und-voraussetzungen)
- [Systemanforderungen](#systemanforderungen)
- [Bekannte Probleme](#bekannte-probleme)
- [Tests](#tests)
- [Entwicklungsrichtlinien](#entwicklungsrichtlinien)
- [Kontakt](#kontakt)

## Installation und Setup

Folgen Sie den unten stehenden Schritten, um das Projekt auf Ihrem System zu installieren:

1. Überprüfen Sie die Pip-Version:
    ```bash
    pip --version
    ```

2. Installieren Sie PyQt5:
    ```bash
    pip install PyQt5
    ```

3. Installieren Sie python3-pip:
    ```bash
    sudo apt install python3-pip
    ```

4. Installieren Sie pyrealsense2:
    ```bash
    pip install pyrealsense2
    ```

5. Installieren Sie numpy:
    ```bash
    pip install numpy
    ```

6. Installieren Sie OpenCV für Python:
    ```bash
    pip install opencv-python
    ```

7. Installieren Sie pymongo:
    ```bash
    pip install pymongo
    ```

8. Starten Sie den MongoDB-Dienst:
    ```bash
    sudo systemctl start mongod
    ```

9. Aktualisieren Sie die Paketliste:
    ```bash
    sudo apt update
    ```

10. Installieren Sie qtcreator und qt5-default:
    ```bash
    sudo apt install qtcreator qt5-default
    ```

11. Falls erforderlich, führen Sie die Neuinstallation von qtcreator durch:
    ```bash
    sudo apt install --reinstall qtcreator
    ```

12. Führe die Anwendung mit dem Befehl aus:
    ```bash
    python3 main.py
    ```

## Abhängigkeiten und Voraussetzungen

Das Projekt setzt voraus:

- PyQt5
- python3-pip
- pyrealsense2
- numpy
- opencv-python
- pymongo
- MongoDB
- qtcreator und qt5-default

## Systemanforderungen

- Betriebssystem: Ubuntu 18.04 oder neuer
- Python-Version: Python 3.6 oder höher

## Bekannte Probleme

- Einige Funktionen sind eventuell nicht mit älteren Python-Versionen kompatibel.
- Es können Probleme bei nicht unterstützten Betriebssystemen auftreten.

## Tests

### Unittests

Navigieren Sie zum Hauptverzeichnis des Projekts und führen Sie den Befehl aus:

```bash
python3 -m unittest [NameDerTestDatei].py
```

Beispiel:

```bash
python3 -m unittest unittest_Firstpage.py
```

### Leistungstests

Navigieren Sie zum Hauptverzeichnis des Projekts und führen Sie den Befehl aus:

```bash
python3 test_performance.py
```

## Entwicklungsrichtlinien

Wenn Sie zum Projekt beitragen möchten, beachten Sie bitte:

- Verwenden Sie aussagekräftige Commit-Nachrichten.
- Halten Sie sich an den PEP 8-Standard.
- Testen Sie Ihre Änderungen vor dem Erstellen eines Pull Requests.
- Erstellen Sie Issues für bekannte Probleme und Vorschläge.

## Kontakt

Bei Fragen oder Anfragen kontaktieren Sie mich bitte unter [s85150@bht-berlin.de](mailto:s85150@bht-berlin.de).
