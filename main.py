from guardaconsulta import guardapostos,guardasupermercados,guardafarmacia,guardaclientes,formatador_cad
from fazconsulta import get_pasta

if get_pasta() in ('35','41','48','71','114'):
    guardasupermercados()
    guardaclientes()
    formatador_cad()


elif get_pasta() in ('83','101'):
    guardapostos()
    print("Postos OK")
    guardaclientes()
    print("Cli OK")
    formatador_cad()
    print("Format OK")



elif get_pasta() in ('57'):
    guardafarmacia()
    guardaclientes()
    formatador_cad()

else:
    guardaclientes()
