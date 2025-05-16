from pywinauto.application import Application
from pywinauto import Desktop
import time
from fazconsulta import get_pasta


def iecoper_import():
    app = Application(backend='uia').start(r'C:\PRATIC\iecoper.exe')
    time.sleep(5)
    dlg = app.window(title_re=r'.*\(925\)Imp/Exp.*')
    time.sleep(5)
    dlg.wait('enabled', timeout=15)
    dlg.set_focus()
    dlg.wait('ready', timeout=15)

    dlg.child_window(title="Aplicativo", control_type="MenuBar").child_window(title="Importar",control_type="MenuItem").invoke()
    print("MenuItem 'Importar' clicado")

    time.sleep(1)

    try:
        # Conecta à janela "Pergunta do sistema"
        pergunta = Desktop(backend="uia").window(title="Pergunta do sistema")
        pergunta.wait('visible', timeout=5)
        pergunta.child_window(title="Sim", control_type="Button").invoke()
        print("Botão 'Sim' clicado")
    except Exception as e:
        print("Erro ao clicar em 'Sim':", e)

    # 3. Aguarda e tenta clicar no botão "Confirmar"
    time.sleep(1)

    for w in Desktop(backend="uia").windows():
        try:
            if w.child_window(title="Confirmar", control_type="Button").exists(timeout=1):
                w.child_window(title="Confirmar", control_type="Button").invoke()
                print("Botão 'Confirmar' clicado")
                break
        except:
            continue

    # 4. Aguarda possível janela de seleção de arquivo
    time.sleep(1)

    try:
        imp_win = Desktop(backend="uia").window(title="Confirmação importação estabelecimento")
        imp_win.child_window(title="Confirmar", control_type="Button").invoke()
        print("Botão 'Confirmar' clicado.")

    except Exception as e:
        print("Erro durante preenchimento e confirmação:", e)

    time.sleep(5)
    abrir_janela = Desktop(backend="uia").window(title="Abrir")

    # Inserir o caminho do arquivo no campo de nome
    abrir_janela.child_window(auto_id="1148", control_type="Edit").set_edit_text(f"cad{get_pasta().zfill(3)}.txt")

    # Clicar no botão "Abrir"
    abrir_janela.child_window(title="Abrir", auto_id="1", control_type="Button").invoke()

    try:
        imp_win = Desktop(backend="uia").window(title="Confirm")
        imp_win.child_window(title="Yes", control_type="Button").invoke()
        print("Botão 'Yes' clicado.")

    except Exception as e:
        print("Erro durante aceite:", e)