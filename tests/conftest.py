import pytest
from utils.helpers import get_driver
import logging
import datetime
from utils import api_ancillary as api_utils
import pathlib


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# Seccion APIs
@pytest.fixture
def api_base_url():
    return api_utils.api_url

# Carpeta de logs
path_dir = pathlib.Path('logs')

# Crear carpeta de logs si no existe
if not path_dir.exists():
    path_dir.mkdir()

# Configuración del logger
logging.basicConfig(
    filename=f'{path_dir}/log_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger()

#  reporte HTML
def pytest_html_report_title(report):
    report.title = "Entrega Final - Reporte de Test Automatizados - Cristian Farelo"


@pytest.fixture
def tomarCaptura(driver):
    ### captura de pantallas
    def tomar(nombre):
        timeStamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        path = f"capturas/{nombre}_{timeStamp}.png"
        driver.save_screenshot(path)
    return tomar