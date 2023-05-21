from datetime import datetime
from hdbcli import dbapi
from pandas import read_sql_query
from datetime import datetime


class GetDataHana:
    def __init__(self):
        self.__host = "172.31.0.130"
        # self.__host = "172.31.0.138"
        self.port = "30115"
        self.__user = "OYP"
        # self.__password = "5tAgt7S8k7XvDx"
        self.__password = "A112ShhtPLZYVv"
        self.__conection = None
        self.__query = ""
        self.volumen = ""

    def init_conection(self):
        try:
            self.__conection = dbapi.connect(address=self.__host, port=self.port, user=self.__user, password=self.__password)
        except Exception as e:
            print(f"Ocurrio un error en la conexion a HANA: {e}")

    def define_query(self, pedidos):
        self.__query = f"""
            SELECT VBAK.VBELN AS PEDIDOS,
                VBAK.ERDAT AS FECHA_CREACION,
                VBAK.VDATU AS FE_ENTREGA,
                VBAK.KUNNR AS SOLICITANTE_ACTUAL,
                VBKD.PRSDT AS FE_PRECIO
            FROM VBAK
            INNER JOIN VBKD
            ON VBAK.VBELN = VBKD.VBELN
            WHERE VBAK.VBELN IN {pedidos}
        """

    def get_request_hana(self):
        try:
            cursor = self.get_conection().cursor()
            cursor.execute("SET SCHEMA SAPABAP1")
            data_frame = read_sql_query(self.__query, self.__conection)
            return data_frame
        except Exception as e:
            print(f"Algo ocurrio mal al realizar la consulta SQL: {e}")

    def get_conection(self):
        if not self.__conection:
            self.init_conection()
            return self.__conection
        else:
            return self.__conection

    def get_request_data(self):
        try:
            df = self.get_request_hana()
            return df if not df.empty else False
        except Exception as e:
            print(f"Error al obtener datos de la base de datos de SAP.{e}")
            return False
# try:
#     hana = GetDataHana()              # 1
#     # hana.define_query((4481992, 4481988))      # 2
#     # hana.show_request_hana()
#     # print(hana.show_request_hana()) # 3
# except Exception as e:
#     print(e)