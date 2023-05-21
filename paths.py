import os
from getpass import getuser

usr = getuser()

# Para las maquinas virtuales
path_base_para_mv = f"C:/Users/{usr}/Desktop/pedidos_copiados_rechazados"
path_osde_mdq = os.path.join(path_base_para_mv, "mar_del_plata")
path_chaco = os.path.join(path_osde_mdq, "osde_chaco")


# PATH DE CARPETA DE CADA FILIAL QUE SE COPIA Y SE RECHAZA
path_base_local = os.getcwd()
# path_resources_local = os.path.join(path_base_local, "../resources")
# path_local_osde_mdq = os.path.join(path_resources_local,"OSDE_SEM_MDQ")
# path_local_osde_chaco = os.path.join(path_resources_local, "OSDE_CHACO")
# path_local_osde_rosario = os.path.join(path_resources_local, "ROSARIO")

# PATHS PARA FACU (crear una carpeta COP_RECH_OSDE en el escritorio)
path_carpeta_escritorio = f"C:/Users/{usr}/Desktop/COP_RECH_OSDE"


# Rutas de cada archivo base excel
# excel_local_osde_mdq = os.path.join(path_local_osde_mdq, "COP_RECH_MDQ.xlsx")
# excel_local_osde_chaco = os.path.join(path_local_osde_chaco, "COP_RECH_CHACO.xlsx")
excel_base_local_rosario = os.path.join(path_carpeta_escritorio, "BASE_COP_RECH_ROSARIO.xlsx")


# Excel para dataframes con fechas de pedidos
# excel_df_fechas_pedidos_mdq = os.path.join(path_local_osde_mdq, "DF_PEDIDOS_Y_FECHAS_MDQ.xlsx")
# excel_df_fechas_pedidos_chaco = os.path.join(path_local_osde_chaco, "DF_FECHAS_CHACO.xlsx")
excel_df_fechas_entr_y_pedidos = os.path.join(path_carpeta_escritorio, "DF_PEDIDOS_Y_FECHAS_ROSARIO.xlsx")
