import re
import numpy as np
from validator_collection import errors
from .errors import NotInListError

CELLPHONE_REGEX = re.compile(
    r'\(?([0]?[1-9][0-9])\)?\s?(9)?\s?((9|8|7)\d{3})\s?-?\s?(\d{4})$'
)
ALPHANUMERIC_REGEX = re.compile(
    r'^[a-zA-Z0-9_]+$'
)

class CNPJ:
    def __init__(self, cnpj):
        self.cnpj = cnpj

    def validate(self):
        """
        Method to validate brazilian cnpjs
        Tests:
        >>> print Cnpj().validate('61882613000194')
        True
        >>> print Cnpj().validate('61882613000195')
        False
        >>> print Cnpj().validate('53.612.734/0001-98')
        True
        >>> print Cnpj().validate('69.435.154/0001-02')
        True
        >>> print Cnpj().validate('69.435.154/0001-01')
        False
        """

        # defining the two vectors of validation --> http://www.macoratti.net/alg_cnpj.htm
        lista_validacao_um = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        lista_validacao_dois = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        if isinstance(self.cnpj, int):
            cnpj = str(self.cnpj)
        else:
            cnpj = self.cnpj

        cnpj = cnpj.replace("-", "")
        cnpj = cnpj.replace(".", "")
        cnpj = cnpj.replace("/", "")

        # extract the verifying digits as string for later comparison
        verificadores = cnpj[-2:]

        # transforms the str into a list of characters
        cnpj = list(cnpj)
        # verifying the lenght of the cnpj
        if len(cnpj) != 14:
            return False

        # casts each character to int
        cnpj = [int(i) for i in cnpj]

        # calculating the first digit
        cabeca = cnpj[:12]
        dot_prod_1 = np.dot(cabeca, lista_validacao_um)
        dig_1_seed = dot_prod_1 % 11

        if dig_1_seed < 2:
            digito_1 = 0
        else:
            digito_1 = 11 - dig_1_seed

        # calculating the second digit
        cabeca.append(digito_1)
        dot_prod_2 = np.dot(cabeca, lista_validacao_dois)
        dig_2_seed = dot_prod_2 % 11

        if dig_2_seed < 2:
            digito_2 = 0
        else:
            digito_2 = 11 - dig_2_seed

        digito_1 = str(digito_1)
        digito_2 = str(digito_2)

        # returnig
        return bool(verificadores == digito_1 + digito_2)

    def format(self):
        """
        Method to format cnpj numbers.
        Tests:
        >>> print Cnpj().format('53612734000198')
        53.612.734/0001-98
        """
        return "%s.%s.%s/%s-%s" % (self.cnpj[0:2], self.cnpj[2:5], self.cnpj[5:8], self.cnpj[8:12], self.cnpj[12:14])

    def __str__(self):
        return '''
            CNPJ: {cnj_number}            
            Valid: {valid}                    
        '''.format(cnj_number=self.cnpj, valid=self.validate())



class CNJ:

    def __init__(self, cnj):
        self.cnj_number = cnj
        self.NNNNNN = None
        self.DD = None
        self.AAAA = None
        self.J = None
        self.J_Extenso = None
        self.TR = None
        self.OOOO = None
        self.regex_valid = None
        self.decomposable = None
        self.check_digit_valid = None
        self.validate()

    def validate(self):
        self.regex_valid = self.cnj_number_regex_validator()
        if self.regex_valid:
            self.decompose_cnj_number()
            self.decomposable = True
        self.check_digit_valid = self.check_digit_validator()

    def cnj_number_regex_validator(self):
        cnj_number_regex = re.compile('\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}')
        if re.fullmatch(cnj_number_regex, self.cnj_number):
            return True
        else:
            return False

    def decompose_cnj_number(self):
        self.NNNNNN = self.cnj_number.split('-')[0]
        self.DD = self.cnj_number.split('.')[0].split('-')[1]
        self.AAAA = self.cnj_number.split('.')[1]
        self.J = self.cnj_number.split('.')[2]
        J_dict = {'1': 'STF', '2': 'CNJ', '3': 'STJ', '4': 'Justiça Federal', '5': 'Justiça do Trabalho',
                  '6': 'Justiça Eleitoral', '7': 'Jutiça Militar da União', '8': 'Justiça Estadual',
                  '9': 'Justiça Militar Estadual'}
        self.J_extenso = J_dict[self.J]
        self.TR = self.cnj_number.split('.')[3]
        self.OOOO = self.cnj_number.split('.')[4]

    def check_digit_validator(self):

        # Inicialmente, os dígitos verificadores D1 D0 devem ser deslocados para o final do número do processo e
        # receber valor zero
        s = self.NNNNNN + self.AAAA + self.J + self.TR + self.OOOO
        s_00 = s + '00'

        # Os dígitos de verificação D1 D0 serão calculados pela aplicação da seguinte fórmula, na qual “módulo” é a
        # operação “resto da divisão inteira”:
        # D1D0 = 98 – (N6N5N4N3N2N1N0A3A2A1A0J2T1R0O3O2O1O00100 módulo 97)
        digits = str(98 - (int(s_00) % 97))

        # se o resultado tiver apenas 1 digito, colocar 0 à esquerda
        if len(digits) == 1:
            digits = '0' + digits

        # VI – A verificação da correção do número único do processo deve ser realizada pela aplicação da seguinte fórmula, cujo
        # resultado deve ser igual a 1 (um):
        # N6N5N4N3N2N1N0A3A2A1A0J2T1R0O3O2O1O0D1D0 módulo 97
        return self.DD == digits

    def __str__(self):
        return '''
            CNJ: {cnj_number}
            NNNNNNN: {NNNNNNN}
            DD: {DD}
            AAAA: {AAAA}
            J: {J} - {J_extenso}
            TR: {TR}
            OOOO: {OOOO}
            Regex Valid: {regex_valid}        
            Check Digit Valid: {check_digit_valid}        
        '''.format(cnj_number=self.cnj_number, NNNNNNN=self.NNNNNN, DD=self.DD, AAAA=self.AAAA, J=self.J,
                   J_extenso=self.J_extenso, TR=self.TR, OOOO=self.OOOO, regex_valid=self.regex_valid, check_digit_valid=self.check_digit_valid)

# TR - identifica o tribunal do respectivo segmento do Poder Judiciário e, na Justiça Militar da União, a Circunscrição Judiciária. O dicionario abaixo segue a ordem dos incisos do parágrafo 5o
tribunal = {
    'I': '00',
    'II': '90'
}
# unidade_origem OOOO - de 0001 a 8999
# http://www.cnj.jus.br/programas-e-acoes/pj-numeracao-unica/documentos/268-acoes-e-programas/programas-de-a-a-z/numeracao-unica

class CPF:
    def __init__(self, cpf):
        self.cpf = cpf

    def validate(self):
        """
        Method to validate brazilian cpfs
        Tests:
        >>> print Cpf().validate('11144477735')
        True
        >>> print Cpf().validate('11144477736')
        False
        >>> print Cpf().validate('111.444.777-35')
        True
        >>> print Cpf().validate('099.264.116-06')
        True
        >>> print Cpf().validate('111.444.777-36')
        False
        """

        # defining the two vectors of validation --> http://www.macoratti.net/alg_cpf.htm
        lista_validacao_um = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        lista_validacao_dois = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

        if isinstance(self.cpf, int):
            cpf = str(self.cpf)
        else:
            cpf = self.cpf

        cpf = cpf.replace("-", "")
        cpf = cpf.replace(".", "")


        # extract the verifying digits as string for later comparison
        verificadores = cpf[-2:]

        # transforms the str into a list of characters
        cpf = list(cpf)
        # verifying the lenght of the cnpj
        if len(cpf) != 11:
            return False

        # casts each character to int
        cpf = [int(i) for i in cpf]

        # calculating the first digit
        cabeca = cpf[:9]
        dot_prod_1 = np.dot(cabeca, lista_validacao_um)
        dig_1_seed = dot_prod_1 % 11

        if dig_1_seed < 2:
            digito_1 = 0
        else:
            digito_1 = 11 - dig_1_seed

        # calculating the second digit
        cabeca.append(digito_1)
        dot_prod_2 = np.dot(cabeca, lista_validacao_dois)
        dig_2_seed = dot_prod_2 % 11

        if dig_2_seed < 2:
            digito_2 = 0
        else:
            digito_2 = 11 - dig_2_seed

        digito_1 = str(digito_1)
        digito_2 = str(digito_2)

        # returnig
        return bool(verificadores == digito_1 + digito_2)

    def format(self):
        """
        Method to format cpf numbers.
        Tests:
        >>> print cpf().format('11144477735')
        111.444.777-35
        """
        return "%s.%s.%s-%s" % (self.cpf[0:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:11])

    def __str__(self):
        return '''
            CPF: {cpf_number}            
            Valid: {valid}                    
        '''.format(cpf_number=self.cpf, valid=self.validate())

# Function to validate lists:


def in_list(value, values_list):
    if len(values_list) == 0:
        raise errors.EmptyValueError('The list cannot be empty')
    if value not in values_list:
        raise NotInListError('The {value} is not in the list'.format(value=value))

    def cellphoneValidator(value, allow_empty=False):
        '''
        Validate that 'value' is a Brazilian Cellphonenumber

        :param value: The value to validate.

        :param allow_empty:
        If ``True``, returns :obj:`None <python:None>` if ``value`` is empty.
        If ``False``, raises a :class:`EmptyValueError <validator_collection.errors.EmptyValueError>`
        if ``value`` is empty. Defaults to ``False``.
        :type allow_empty: :class:`bool <python:bool>`

        if value is None and allow_empty:
            return None
        elif value is None or value == "":
            raise errors.EmptyValueError('value cannot be None')
        '''
        if CELLPHONE_REGEX.search(value):
            return True
        else:
            return False

    def alphanumericValidator(value, allow_empty=False):
        '''
        Validate that 'value' contains alphanumeric digits.

        :param value: The value to validate.

        :param allow_empty:
        If ``True``, returns :obj:`None <python:None>` if ``value`` is empty.
        If ``False``, raises a :class:`EmptyValueError <validator_collection.errors.EmptyValueError>`
        if ``value`` is empty. Defaults to ``False``.
        :type allow_empty: :class:`bool <python:bool>`

        if value is None and allow_empty:
            return None
        elif value is None or value == "":
            raise errors.EmptyValueError('value cannot be None')
        '''
        if ALPHANUMERIC_REGEX.match(value):
            return True
        else:
            return False
