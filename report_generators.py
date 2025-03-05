from abc import ABC, abstractmethod
import json
import csv

# Classe abstrata base para os geradores de relatórios.
# Cada tipo de relatório deve implementar o método `generate_report`.
class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, data, file_name):
        """
        Método abstrato para gerar o relatório. Deve ser implementado por
        subclasses para gerar diferentes tipos de relatórios (TXT, CSV, JSON).

        Args:
            data (list): Lista de dicionários com os dados a serem incluídos no relatório.
            file_name (str): Nome do arquivo onde o relatório será salvo.
        """
        pass

# Gerador de relatório no formato TXT 
class TxtReportGenerator(ReportGenerator):
    def generate_report(self, data, file_name):
        """
        Gera um relatório em formato TXT e salva no arquivo especificado.

        Args:
            data (list): Lista de dicionários com os dados a serem incluídos no relatório.
            file_name (str): Nome do arquivo onde o relatório será salvo.
        """
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                for client in data:
                    file.write(f"Nome: {client['Nome']}, Endereço: {client['Endereço']}\n")
            print(f"Relatório TXT gerado com sucesso! Nome do arquivo: {file_name}")
        except Exception as e:
            print(f"Erro ao gerar o relatório TXT: {e}")

# Gerador de relatório no formato CSV
class CsvReportGenerator(ReportGenerator):
    def generate_report(self, data, file_name):
        """
        Gera um relatório no formato CSV e salva no arquivo especificado.

        Args:
            data (list): Lista de dicionários com os dados a serem incluídos no relatório.
            file_name (str): Nome do arquivo onde o relatório será salvo.
        """
        try:
            with open(file_name, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Nome", "Endereço"])  # Cabeçalho do CSV
                for client in data:
                    writer.writerow([client["Nome"], client["Endereço"]])
            print(f"Relatório CSV gerado com sucesso! Nome do arquivo: {file_name}")
        except Exception as e:
            print(f"Erro ao gerar o relatório CSV: {e}")

# Gerador de relatório no formato JSON
class JsonReportGenerator(ReportGenerator):
    def generate_report(self, data, file_name):
        """
        Gera um relatório no formato JSON e salva no arquivo especificado.

        Args:
            data (list): Lista de dicionários com os dados a serem incluídos no relatório.
            file_name (str): Nome do arquivo onde o relatório será salvo.
        """
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                json.dump({"relatório": data}, file, indent=4)
            print(f"Relatório JSON gerado com sucesso! Nome do arquivo: {file_name}")
        except Exception as e:
            print(f"Erro ao gerar o relatório JSON: {e}")