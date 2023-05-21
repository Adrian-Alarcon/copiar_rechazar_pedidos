import win32com.client as win32
import pythoncom
import win32com.client
from va01_2 import va01_2


def toma(nro_pedido, nuevo_rnos, sesionsap):
    pythoncom.CoInitialize()
    SapGuiAuto = win32com.client.GetObject('SAPGUI')
    if not type(SapGuiAuto) == win32com.client.CDispatch:
        return
    application = SapGuiAuto.GetScriptingEngine
    if not type(application) == win32com.client.CDispatch:
        SapGuiAuto = None
        return
    connection = application.Children(0)
    if not type(connection) == win32com.client.CDispatch:
        application = None
        SapGuiAuto = None
        return
    session = connection.Children(sesionsap)
    if not type(session) == win32com.client.CDispatch:
        connection = None
        application = None
        SapGuiAuto = None
        return
    try:
        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nzsd_toma"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/tbar[1]/btn[7]").press()
        session.findById("wnd[0]/usr/subSBS_PARSEL:ZDMSD_TOMA_PEDIDO:1100/ctxtS_KUNNR-LOW").text = ""
        session.findById("wnd[0]/usr/subSBS_PARSEL:ZDMSD_TOMA_PEDIDO:1100/ctxtS_KUNNR-LOW").setFocus()
        session.findById("wnd[0]/usr/subSBS_PARSEL:ZDMSD_TOMA_PEDIDO:1100/ctxtS_KUNNR-LOW").caretPosition = 8
        session.findById("wnd[0]/usr/subSBS_PARSEL:ZDMSD_TOMA_PEDIDO:1100/ctxtS_VBELN-LOW").text = nro_pedido
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/cntlCC_LISTAPED/shellcont/shell").currentCellColumn = "VBELN"
        session.findById("wnd[0]/usr/cntlCC_LISTAPED/shellcont/shell").selectedRows = "0"
        session.findById("wnd[0]/usr/cntlCC_LISTAPED/shellcont/shell").pressToolbarButton("FN_MODDEL")
        session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-CLIENTE").text = nuevo_rnos
        session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-CLIENTE").caretPosition = 8
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]").sendVKey(0)
        # Bloque para validar que el pedido tenga el codigo de producto externo cargado en todas las posiciones
        try:
            session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT").select()
            session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT").select()
            session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/btnBTN_CALC_FECHA").press()
        except:
            session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/subSUBS_TRAB:ZDMSD_TOMA_PEDIDO:0111/tblZDMSD_TOMA_PEDIDOTC_CARRITO/txtGS_CARRITO-COD_EXTERNO[19,0]").text = "99999"
            session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/subSUBS_TRAB:ZDMSD_TOMA_PEDIDO:0111/tblZDMSD_TOMA_PEDIDOTC_CARRITO/txtGS_CARRITO-COD_EXTERNO[19,0]").setFocus()
            session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/subSUBS_TRAB:ZDMSD_TOMA_PEDIDO:0111/tblZDMSD_TOMA_PEDIDOTC_CARRITO/txtGS_CARRITO-COD_EXTERNO[19,0]").caretPosition = 5
            session.findById("wnd[0]").sendVKey(0)
            session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT").select()
            session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT").select()
            session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/txtGS_ENTREGA-FILIAL_CLI").text = "2"
            session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/txtGS_ENTREGA-FILIAL_CLI").setFocus()
            session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/txtGS_ENTREGA-FILIAL_CLI").caretPosition = 1

            session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/btnBTN_CALC_FECHA").press()

        session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/btnBTN_CALC_FECHA").press()
        session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED").select()
        try:
            return nro_pedido
            # session.findById("wnd[0]/tbar[0]/btn[11]").press()
            # session.findById("wnd[1]/usr/btnBUTTON_1").press()
            # session.findById("wnd[1]/tbar[0]/btn[0]").press()
        except:
            mensaje_error = session.findById("wnd[0]/sbar").text
            print(f"Excepcion general en el programa: {mensaje_error} | {e}")
        finally:
            return nro_pedido

    except Exception as e:
        mensaje_error = session.findById("wnd[0]/sbar").text
        print(f"Excepcion general en el programa: {mensaje_error} | {e}")


def toma_prd(nro_pedido, nuevo_rnos, fecha, sesionsap):
    pythoncom.CoInitialize()
    SapGuiAuto = win32com.client.GetObject('SAPGUI')
    if not type(SapGuiAuto) == win32com.client.CDispatch:
        return
    application = SapGuiAuto.GetScriptingEngine
    if not type(application) == win32com.client.CDispatch:
        SapGuiAuto = None
        return
    connection = application.Children(0)
    if not type(connection) == win32com.client.CDispatch:
        application = None
        SapGuiAuto = None
        return
    session = connection.Children(sesionsap)
    if not type(session) == win32com.client.CDispatch:
        connection = None
        application = None
        SapGuiAuto = None
        return
    try:
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nzsd_toma"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/tbar[1]/btn[7]").press()
        session.findById("wnd[0]/usr/subSBS_PARSEL:ZDMSD_TOMA_PEDIDO:1100/ctxtS_VBELN-LOW").text = nro_pedido
        session.findById("wnd[0]/usr/subSBS_PARSEL:ZDMSD_TOMA_PEDIDO:1100/ctxtS_ERDAT-LOW").text = "01.01.2021"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/subSBS_PARSEL:ZDMSD_TOMA_PEDIDO:1100/ctxtS_VBELN-LOW").setFocus()
        session.findById("wnd[0]/usr/subSBS_PARSEL:ZDMSD_TOMA_PEDIDO:1100/ctxtS_VBELN-LOW").caretPosition = 8
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/cntlCC_LISTAPED/shellcont/shell").currentCellColumn = "BSTKD"
        session.findById("wnd[0]/usr/cntlCC_LISTAPED/shellcont/shell").selectedRows = "0"
        session.findById("wnd[0]/usr/cntlCC_LISTAPED/shellcont/shell").pressToolbarButton("FN_MODDEL")
        session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-CLIENTE").text = nuevo_rnos
        session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0101/ctxtZSD_TOMA_CABEC-CLIENTE").caretPosition = 8
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT").select()
        session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/btnBTN_CALC_FECHA").press()
        session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/btnBTN_CALC_FECHA").press()
        session.findById("wnd[0]/usr/tabsTABS/tabpTAB_ENT/ssubTABS_SCA:ZDMSD_TOMA_PEDIDO:0102/btnBTN_CALC_FECHA").press()
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/tabsTABS/tabpTAB_PED").select()
        # Boton grabar
        session.findById("wnd[0]/tbar[0]/btn[11]").press()
        try:
            for i in range(5):
                try:
                    session.findById("wnd[1]/usr/btnBUTTON_1").press()
                except:
                    break

            # Boton de grabar
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            mensaje = session.findById("wnd[0]/sbar").text
            nuevo_pedido_toma = mensaje[23:30]
            mensaje_va02, nuevo_pedido = va01_2(sesionsap, fecha, nuevo_pedido_toma)
            if mensaje_va02:
                return nro_pedido, mensaje, mensaje_va02, nuevo_pedido ,f"'000{nuevo_pedido}',"
            else:
                return nro_pedido, mensaje, "ERROR VA02", "NO PEDIDO VA02", "NO PEDIDO VA02"
        except:
            session.findById("wnd[1]/tbar[0]/btn[0]").press()
            mensaje = session.findById("wnd[0]/sbar").text
            nuevo_pedido_toma = mensaje[23:30]
            mensaje_va02, nuevo_pedido = va01_2(sesionsap, fecha, nuevo_pedido_toma)
            if mensaje_va02:
                return nro_pedido, mensaje, mensaje_va02, nuevo_pedido, f"'000{nuevo_pedido}',"
            else:
                return nro_pedido, mensaje, "ERROR VA02", "NO PEDIDO VA02", "NO PEDIDO VA02"
    except Exception as ex:
        try:
            mensaje = session.findById("wnd[0]/sbar").text
            return nro_pedido, mensaje, "No pude ir a la VA02", " ", " "
        except Exception as e:
            print(f"------- Error general -------")
            return nro_pedido, "Error General", "Error General", "ERROR GENERAL", "ERROR GENERAL"


# print(toma_prd("6140075", "10000305", 0))
# ped_mod = toma("6140075","10000305",0)
# va01_2.va01_2(0, ped_mod, "20230110")

