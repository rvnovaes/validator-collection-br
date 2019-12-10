import traceback
import pytest
from validator_collection_br.validators_br import in_list
from validator_collection_br.errors_br import NotInListError
from validator_collection_br import validators_br, errors_br
from validator_collection import errors


# malformed_lawsuits_numbers = ['15201201038073', '19890010109053', '19970011037802', '1020857820138200000', '10514093820138200000', '0056758-98.2017', '0062436-28.2016.8.19.000',  '0078346-55.2003''0078821-61.2013', '0079413-74.2011', '008.09.2099979', '0083734-55.2011.8.19.000', '0084047-93.2017.8.05.000', '009.08.603715-1', '011.10.016102-3', '0114968-57.2013.8.20.0', '0114968-57.2013.8.20.000', '0120646-89.2007', '0123367-53.2017.8.05.000', '0123526-78.2012.8.26.010', '0124351-27.2009', '0126620-05.2010.8.26.010', '0134621-91.2015.8.05.000', '0137755-29.2015.8.05.000', '013958-23.2012', '013958-23.2012', '0146570-29.2012', '015.01..000150-2', '0151068-04.2014.8.19.000', '016.10.611108-1', '0163240-79.2011.8.26.010', '0164068-51.2006', '0172804482012/01', '0174361-32.2010.8.05.000', '0187146-35.2010', '0188528-29.2011', '01993355-70.2009.8.26.010', '0201338-57.2013.8.19.000', '0203102-23.2012.8.26.010', '0208229-10.2010', '0319066-26.2016', '032.2011.022.137-4', '0350717-52.2011', '0422056-32.2015', '0533540-62.2006', '0603715-96-2008', '0607852-95.2011', '0610207.44.2012', '0624529-50.2008', '0706581-07.2017.8.07.', '0713 13005841-3', '0713942-11.2007', '07176-54-06.2016.8.14.03', '0717890-86/2014', '0718855-35.2012', '0800109-22.2016.8.20.500', '0800190-33.2009', '0800265-77.2013.8.20.000', '10.110.805.320.148.260.00', '100.10.610064-', '1000331-43.2013.8.26.015', '1000652-26.2017-X', '1001389_x0013_82.2014.8.26.0011', '1001714-82.2016-01', '1001979-31.2015.8.26.000', '1002291-06.2015', '1002303-58.2014.8.26.000', '1003497-11.2016.8.26.004', '1003497-11.2016.8.26.004', '1004605-05.2013.8.26.036', '1004654-24.2011', '1004917-78.2013.8.26.036', '1005816-12.2015', '1007417-83.2014.8.26.0', '1007585-24.2016.8.26.010', '1008571-07.2014', '1009077-28.2017', '1010581-58.2013', '1012988-81.2015', '1016137-12-2015-01', '1016315-58.2015', '1020444-09.2014.8.26.056', '1022387-91.2014.8.26.055', '1024512-70.2013', '1024738-76.2015', '10314-16.2011 - cód. 7191', '1031478-15.2014', '1031645-61.8.26.0100', '1040129-36.2014', '1045764-61.2015', '1045978-23.2013', '1051437-69.2014', '1053564-46.2015', '1054631-77.2014', '1058724-83.2014.8.26.010', '1064382-25.2013', '1066864-43.2013', '1068654-28.2014', '1072883-65.2013', '1089219-13.2014.8.26.010', '1090251-82.2016', '1092882-67.2014', '110527-81.2014.8.26.0100', '1125855-07.2016', '164626-47.2011', '164626-47.2011', '2000889-13.2016.8.26.0', '2005 102305 7  ORD', '2005.542-63.2013.8.26.001', '2010.0007215-31', '2010.0007549-65', '2014.01.1.192579-8', '2015.14.1.002136-7', '2015.14.1.006175-6', '2015.14.1.008604-8', '2016.14.1.006604-4', '2016.16.1.000562-6', '2016.16.1.004832-4', '2016.16.1.007301-6', '2016.16.1.009376-6', '2016.16.1.011841-7', '2017.16.1.000001-6', '2025388-32/2014', '240654-18.2015', '2767-72.8.26.0654', '283212-73.2013', '284790-03.2015', '302459-35.2016', '4001449-28.2013.8.26.056', '4006551-81.2013', '4008248-79.2013', '465260-63.2014', '495508-80.2012', '5255449.64.2015.8.09.005', '583 00 2004 008628 9', '583 00 2005 069234 5', '583.07.2005.023123-8', '998.10.602.359', '999.11.606502-', 'kk0017042-122009.8.19.020']

well_formed_lawsuits_numbers = ['0000013-59.2013.8.05.0250', '0611925-60.2017.8.04.0001', '0004268-07.2016.8.06.0063',
                                '0005714-53.2008.8.18.0140']
malformed_lawsuits_numbers = ['0000023-59.2013.8.05.0250', '0611925-60.8888.8.04.0010', '7770000-07.2016.8.06.0063',
                              '0005714-53.2008.8.18.0000']

well_formed_cnpj_numbers = ['04.170.575/0001-03',
                            61198164000160, 58768284000140, 33448150000111, 8816067000100, 4540010000170,
                            4862600000110, 40303299000178, 48041735000190, '02340041000152', '09436686000132']

customers = ["DIRECIONAL JUDICIAL", "DIRECIONAL EXTRAJUDICIAL", "MRV JUDICIAL", "MRV EXTRAJUDICIAL", "PRECON", "BTM",
             "SEMPRE EDITORA EXTRAJUDICIAL", "SANTO ANDRÉ JUDICIAL", "SANTO ANDRÉ EXTRAJUDICIAL", "KINEA JUDICIAL",
             "KINEA EXTRAJUDICIAL", "ITAU", "SEMPRE EDITORA JUDICIAL"]

negotiation_status = ["CONTATO INICIAL", "EM ANDAMENTO", "AVANÇADA", "QUITAÇÃO INTEGRAL", "RENEGOCIAÇÃO EFETIVADA",
                      "RENEGOCIAÇÃO QUITADA", "INADIMPLÊNCIA APÓS ACORDO", "RECUSA NÃO TEM CONDIÇÕES",
                      "RECUSA NÃO TEM INTERESSE"]

deal = ["SIM", "NÃO"]

deal_type = ["PARCELADO", "À VISTA"]

customers_status = ["ADIMPLENTE", "INADIMPLENTE"]

suspended_action = ["SUSPENSO", "ATIVO"]

customers_lawyer = ["SIM", "NÃO"]

customer_guarantee = ["SIM", "NÃO"]

court = ["SUPREMO TRIBUNAL FEDERAL", "TRIBUNAL SUPERIOR DO TRABALHO", "CONSELHO SUPERIOR DA JUSTIÇA DO TRABALHO",
         "SUPERIOR TRIBUNAL DE JUSTIÇA", "CONSELHO DA JUSTIÇA FEDERAL", "TRIBUNAL SUPERIOR ELEITORAL",
         "SUPERIOR TRIBUNAL MILITAR", "TRIBUNAL REGIONAL FEDERAL", "TRIBUNAL DE JUSTIÇA", "TRIBUNAL REGIONAL ELEITORAL",
         "TRIBUNAL DE JUSTIÇA MILITAR", "PROCON", "OAB", "PREFEITURA", "GOVERNO DO ESTADO", "ÓRGÃO PROFISSIONAL",
         "OUTROS"]

state = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",
         "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

subpoena = ["SIM", "NÃO"]

pawn = ["SIM", "NÃO"]

patrimony_repossessed = ["VALOR EM CONTA", "VEÍCULO", "IMÓVEL", "DIREITOS AQUISITIVOS", "OUTROS"]

court_decision = ["NÃO", "PROCEDENTE", "PARCIALMENTE PROCEDENTE", "IMPROCEDENTE", "EXTINTO SEM JULGAMENTO DO MÉRITO",
                  "HOMOLOGADO ACORDO"]

appeal = ["SIM", "NÃO"]

res_judicata = ["SIM", "NÃO"]

cellphoneValidatorsTests = [
    ["33991749686", True],
    ["XXX", False],
    ["33 9 9174 - 7498", True],
    ["(37)982159000", True],
    ["37J982159000", False],
    ["+(55)31991749686", True],
    ["", False]
]

alphanumericValidatorsTests = [
    ["123456", True],
    ["XXX", True],
    ["XXX456", True],
    ["", False],
    ["....", False],
    ["asas.5464", False],
    ["", False]
]


class TestCPF:

    well_formed_cpf = '020.388.410-80'
    malformed_digit_cpf = '020.388.410-00'
    malformed_mask_cpf = '02038841080'
    malformed_numeric_cpf = 2038841080
    malformed_short_cpf = '20.388.410-80'
    malformed_long_cpf = '0020.388.410-80'

    def test_empty_cpf(self):
        with pytest.raises(errors.EmptyValueError):
            validators_br.cpf('')

    def test_cpf_string_type(self):
        with pytest.raises(errors_br.DataTypeError):
            validators_br.cpf(self.malformed_numeric_cpf)

    def test_cpf_too_short(self):
        with pytest.raises(errors.MinimumLengthError):
            validators_br.cpf(self.malformed_short_cpf)

    def test_cpf_too_long(self):
        with pytest.raises(errors.MaximumLengthError):
            validators_br.cpf(self.malformed_long_cpf)

    def test_cpf_wrong_mask(self):
        with pytest.raises(errors_br.InvalidCpfMaskError):
            validators_br.cpf(self.malformed_mask_cpf)

    def test_cpf_digit(self):
        with pytest.raises(errors_br.InvalidCpfError):
            validators_br.cpf(self.malformed_digit_cpf)

    def test_cpf_formation(self):
        assert self.well_formed_cpf == validators_br.cpf(self.well_formed_cpf)
