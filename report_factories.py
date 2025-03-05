from report_generators import *

# Classe abstrata base para as fábricas de geradores de relatórios
# Cada fábrica deve ser responsável por criar o gerador de relatório adequado (TXT, CSV ou JSON).
class FactoryReportGenerator(ABC):
    @abstractmethod
    def get_report(self) -> ReportGenerator:
        """
        Método abstrato para criar um gerador de relatório.
        Cada fábrica deve retornar um gerador de relatório específico.
        """
        pass

# Fábrica para criar o gerador de relatórios TXT
class FactoryTxtReportGenerator(FactoryReportGenerator):
    def get_report(self):
        """
        Cria e retorna um gerador de relatórios no formato TXT.
        """
        return TxtReportGenerator()

# Fábrica para criar o gerador de relatórios CSV
class FactoryCsvReportGenerator(FactoryReportGenerator):
    def get_report(self):
        """
        Cria e retorna um gerador de relatórios no formato CSV.
        """
        return CsvReportGenerator()

# Fábrica para criar o gerador de relatórios JSON
class FactoryJsonReportGenerator(FactoryReportGenerator):
    def get_report(self):
        """
        Cria e retorna um gerador de relatórios no formato JSON.
        """
        return JsonReportGenerator()

"""
Função auxiliar para evitar repetição do código ao criar e chamar os geradores.

Recebe a fábrica, nome do arquivo e os dados que serão usados.
"""    

def generate_report(factory: FactoryReportGenerator, data, file_name):
    generator = factory.get_report()  
    generator.generate_report(data, file_name)  