from guardaconsulta import guardapostos,guardasupermercados,guardafarmacia, guardarestaurante,guardaclientes,formatador_cad
from fazconsulta import get_pasta
from automate import iecoper_import


if get_pasta() in ('35','41','48','114'):
    guardasupermercados()
    guardaclientes()
    formatador_cad()


elif get_pasta() in ('83','101'):
    guardapostos()
    guardaclientes()
    formatador_cad()



elif get_pasta() in ('57'):
    guardafarmacia()
    guardaclientes()
    formatador_cad()


elif get_pasta() in ('71'):
    guardarestaurante()
    guardaclientes()
    formatador_cad()


else:
    guardaclientes()
