import time
import pytest
from PyQt5.QtWidgets import QApplication
from Firstpage import Window
from Secondpage import SurgicalDataForm
from Thirdpage import CameraPage
from Lastpage import FinalPage
from AllinfoPage import AllInfo

@pytest.fixture(scope="module")
def app():
    # Erstelle eine QApplication-Instanz für den Test
    app = QApplication([])
    yield app
    # Beende die QApplication-Instanz nach dem Test
    app.quit()

def test_start_time(app):
    # Startzeit der Anwendung messen
    start_time = time.time()

    # Erstelle und zeige die erste Seite
    window = Window()
    window.show()

    # Simuliere langsame Initialisierung oder Berechnungen auf der ersten Seite
    time.sleep(2)

    # Gehe zur nächsten Seite
    window.show_next_signal.emit()

    # Erstelle und zeige die zweite Seite
    surgical_form = SurgicalDataForm()
    surgical_form.show()

    # Simuliere langsame Initialisierung oder Berechnungen auf der zweiten Seite
    time.sleep(2)

    # Gehe zur nächsten Seite
    surgical_form.show_next_signal.emit()

    # Erstelle und zeige die dritte Seite
    camera_page = CameraPage()
    camera_page.show()

    # Simuliere langsame Initialisierung oder Berechnungen auf der dritten Seite
    time.sleep(2)

    # Gehe zur nächsten Seite
    camera_page.show_next_signal.emit()

    # Erstelle und zeige die letzte Seite
    final_page = FinalPage()
    final_page.show()

    # Simuliere langsame Initialisierung oder Berechnungen auf der letzten Seite
    time.sleep(2)

    # Gehe zur AllInfo-Seite
    final_page.show_all_signal.emit()

    # Erstelle und zeige die AllInfo-Seite
    all_info_page = AllInfo()
    all_info_page.loadData()

    # Simuliere langsame Datenladung auf der AllInfo-Seite
    time.sleep(2)

    end_time = time.time()
    execution_time = end_time - start_time

    # Teste, ob die Gesamtausführungszeit der Anwendung angemessen ist (z.B. unter 15 Sekunden)
    assert execution_time < 15.0
