from flask import Flask
from flask import abort
from flask import jsonify
app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.8 (from the example template)"


@app.route('/')
def main():
	'''
	Obtengo una serie de secuencias, valido el formato y verifico si pertenece a un mutante
	'''
	dna = '{"ATGCGA","CAGTGC","TTATGT","AGAtGG","CCCCTA","TCACTG"};'
    
    # Genero la matriz desde el string recibido
	matriz = validarMatriz(dna)

	if(isMutant('aaaa', 'b')):
		return ''
	else:
		abort(_ERROR_CODES["NOT_MUTANT"], '') # Se envía response code 403 sin mensaje, flask agrega Forbidden por default

def isMutant(adn, sample):
	'''
	Devuelve True si la secuencia coincide con una secuencia mutante o False si no lo hace
	Si la secuencia repite una base SEQUENCE_LENGTH veces se considera secuencia mutante

	La definición de las caracteristicas que coinciden con un mutante son 
	independientes del tamaño de la matriz y de la estretegia para recorrerla,

	La funcion que recorre la matriz es independiente de la funcion que evalua
	la secuencia de ADN
	'''
	sequence = []
	# Con la primer base de la secuencia genero un string 
	for i in range(_CONFIG['SEQUENCE_LENGTH']):
		sequence.append(str(sample))

	match_str = str('').join(sequence)

	if (adn.upper() == match_str.upper()):
		return True
	else :
		return False

def validarMatriz(dna):
	'''
	Valida que la matriz recibida tenga el formato correcto
	formato:
		{"aaaa","bbbb","cccc","dddd";}
	'''
	matriz = []
	# Validar inicio y fin de string 
	if(not dna[0] == '{' or not dna[-2:] == '};'):
		raise InvalidUsage('La matriz recibida no es valida, debe iniciar con { y terminar con };', status_code=_ERROR_CODES["INVALID_BSTRING_HEADERS"])
	# Validar comillas dobles en cada secuencia y genero la matriz sanitizada
	m = dna[1:-2].split(",")
	for item in m:
		if(not item[0] == '"' or not item[-1] == '"'):
			raise InvalidUsage('La matriz recibida no es valida, las secuencias deben iniciar y terminar con comillas dobles', status_code=_ERROR_CODES['IVALID_STRING_IDENTIFIER'])
		else:
			sequence = item[1:-1]
			# Validar el valor de cada base en todas las secuencias
			validarSequence(sequence)
			# Validar que el tamaño de la secuencia 
			validarTamañoSequence(sequence, len(m[0][1:-1]))
			# Añado la secuencia validada a la matriz
			matriz.append(sequence) #creo una matriz con las secuencias sanitizadas
	return matriz

def validarSequence(sequence):
	'''
	Valida que cada la secuencia tenga todas las bases validas
	'''
	validValues = ('A','T','G','C')
	for base in sequence:
		if (base.upper() not in validValues):
			raise InvalidUsage('La matriz recibida no es valida, valores validos ' + str(validValues), status_code=_ERROR_CODES["INVALID_BASE"])

def validarTamañoSequence(sequence, size):
	''' 
	comparo el tamaño de todas las secuencias con el tamaño de la primer secuencia y
	que el tamaño de la secuencia sea mayor o igual al numero de bases consecutivas requeridas
	'''
	iSize = len(sequence)
	if(not iSize == size ):
		raise InvalidUsage('La matriz recibida no es valida, una secuencia es mas corta;', status_code=_ERROR_CODES["SEQUENCE_LENGTH_MISMATCH"])
	if(iSize < _CONFIG["SEQUENCE_LENGTH"]):
		raise InvalidUsage('La matriz recibida no es valida, la secuencia es muy corta;', status_code=_ERROR_CODES["SEQUENCE_TO_SHORT"])

# Constants
_ERROR_CODES = {"NOT_MUTANT":403,"SEQUENCE_LENGTH_MISMATCH":514,"SEQUENCE_TO_SHORT":513,"INVALID_BASE":512,"IVALID_STRING_IDENTIFIER":511,"INVALID_BSTRING_HEADERS":510}
_CONFIG = {"SEQUENCE_LENGTH":4,"NUM_SEQUENCE_MATCH":2}

# Custom Exceptions
class InvalidUsage(Exception):
    status_code = 501

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=8850)
