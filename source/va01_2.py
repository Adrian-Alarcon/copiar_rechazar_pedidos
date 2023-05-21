import win32com.client as win32
import pythoncom
import win32com.client
from time import sleep
from datetime import datetime

def va01_2(sesionsap, fecha, pedido):
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
          date_time = datetime.strptime(str(fecha), "%Y%m%d")
          fecha_formato_sap = datetime.strftime(date_time, "%d.%m.%Y")

          session.findById("wnd[0]/tbar[0]/okcd").text = "/NVA02"
          session.findById("wnd[0]").sendVKey(0)
          session.findById("wnd[0]/usr/ctxtVBAK-VBELN").text = pedido
          session.findById("wnd[0]/usr/ctxtVBAK-VBELN").caretPosition = 7
          session.findById("wnd[0]").sendVKey(0)
          session.findById(r"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\01/ssubSUBSCREEN_BODY:SAPMV45A:4400/ssubHEADER_FRAME:SAPMV45A:4440/ctxtRV45A-KETDAT").text = fecha_formato_sap
          session.findById(r"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\01/ssubSUBSCREEN_BODY:SAPMV45A:4400/ssubHEADER_FRAME:SAPMV45A:4440/ctxtRV45A-KETDAT").setFocus()
          session.findById(r"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\01/ssubSUBSCREEN_BODY:SAPMV45A:4400/ssubHEADER_FRAME:SAPMV45A:4440/ctxtRV45A-KETDAT").caretPosition = 10
          session.findById("wnd[0]").sendVKey(0)
          session.findById("wnd[0]").sendVKey(0)
          session.findById("wnd[0]").sendVKey(0)
          session.findById("wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\\01/ssubSUBSCREEN_BODY:SAPMV45A:4400/ssubHEADER_FRAME:SAPMV45A:4440/cmbVBAK-LIFSK").key = "PF"
          session.findById("wnd[0]").sendVKey(0)

          session.findById(r"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\02").select()
          # for i in range(7):
          #      try:
          #           session.findById(rf"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\02/ssubSUBSCREEN_BODY:SAPMV45A:4401/subSUBSCREEN_TC:SAPMV45A:4900/tblSAPMV45ATCTRL_U_ERF_AUFTRAG/ctxtRV45A-ETDAT[11,{i}]").text = fecha_formato_sap
          #           session.findById(rf"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\02/ssubSUBSCREEN_BODY:SAPMV45A:4401/subSUBSCREEN_TC:SAPMV45A:4900/tblSAPMV45ATCTRL_U_ERF_AUFTRAG/ctxtRV45A-ETDAT[11,{i}]").setFocus()
          #           session.findById(rf"wnd[0]/usr/tabsTAXI_TABSTRIP_OVERVIEW/tabpT\02/ssubSUBSCREEN_BODY:SAPMV45A:4401/subSUBSCREEN_TC:SAPMV45A:4900/tblSAPMV45ATCTRL_U_ERF_AUFTRAG/ctxtRV45A-ETDAT[11,{i}]").caretPosition = 10
          #           session.findById("wnd[0]").sendVKey(0)
          #           session.findById("wnd[0]").sendVKey(0)
          #           sleep(0.5)
          #           # print(f"Iteracion: {i}")
          #      except Exception as e:
          #           print(i, f"--{e}")
          #           print(f"Error al cargar fecha en posiciones")
          #           break
          try:
               session.findById("wnd[0]/tbar[0]/btn[11]").press()
               mensaje = session.findById("wnd[0]/sbar").text
               print(f"Resultado VA02: {mensaje}")
               return mensaje, mensaje[18:25]
          except Exception as ex:
               print(f"Error al grabar pedido {pedido} en VA02 -- {ex}")
               return False, False
     except Exception as e:
          print(f"Error al cargar el pedido", e)

# va01_2(0, "6145641", 20230218)
