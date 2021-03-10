from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.8 (from the example template)"


@app.route('/')
def main():
	return str(isMutant('aaaa', 'a'))

def isMutant(adn, sample):
	'''
	Devuelve True si la secuencia coincide con un mutante o False si no lo hace
	La definición de las caracteristicas que coinciden con un mutante son 
	independientes del tamaño de la matriz y de la estretegia para recorrerla,

	La funcion que recorre la matriz es independiente de la funcion que evalua
	la secuencia de ADN
	'''
	sequence = []
	for i in range(4):
		sequence.append(str(sample))

	match_str = str('').join(sequence)

	if (adn.upper() == match_str.upper()):
		return True
	else :
		return False


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=8850)
