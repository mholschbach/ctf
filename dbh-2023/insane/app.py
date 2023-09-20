#!/bin/python
import sys
import subprocess
import time
from flask import Flask, request
app = Flask(__name__)

class FailureException(Exception):
	pass

def check_file(filename):
	with open(filename, "rb") as inf:
		a = inf.read()
	if b"#" in a:
		x = "Keine Magie nutzen"
		if b"#include" in a:
			x += "<p>gcc kompiliert C auch ohne explizite includes."
		raise FailureException(x)

def rndstr(n=10):
	return "rzqnilawqb" # https://xkcd.com/221/

fn = "prog_" + rndstr() + ".c"

compilecmd = [
	"gcc",
	"-static",
	"-fdiagnostics-color=never",
	"-x", "c",
	fn,
	"-o",
	"/ctf/app/compiles/prog"
]

runcmd = [
	"/ctf/app/compiles/prog"
]

def compile(fn):
	try:
		c = subprocess.Popen(compilecmd,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE)
		o, e = c.communicate()
		if c.returncode != 0:
			raise FailureException("Fehler beim Kompilieren\n" + str(e.decode()))
	except FailureException as e:
		raise e
	except Exception:
		raise FailureException("Fehler beim Kompilieren\n")

def run(first):
	try:
		if first:
			c = subprocess.run([
				"cp",
				"/ctf/app/compiles/prog",
				"/ctf/secureenv/prog"
			], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			c = subprocess.run([
				"sudo",
				"-u", "nobody",
				"/ctf/secureenv/prog"
			], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		else:
			c = subprocess.run(runcmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	except Exception as e:
		return b""
	return c.stdout + c.stderr

def main():
	fc = open(fn,"rb").read()
	try:
		compile(fn)
	except:
		raise FailureException("Fehler beim initialen kompilieren")
	out = run(first=True)
	if len(out) == 0:
		raise FailureException("Keine Ausgabe")
	if out != fc:
		print(out)
		print(fc)
		raise FailureException("Falsches Ergebnis")

	for _ in range(10):
		with open(fn, "wb") as outf:
			outf.write(out)
		time.sleep(1) # Sichergehen, dass das Write wirklich auf der Festplatte angekommen ist
		compile(fn)
		out = run(first = False)
		if len(out) == 0:
			raise FailureException("Leere Ausgabe.")
		print(out)

def html():
	return '''
		<!doctype html>
		<title>C Code hochladen</title>
		<h1>C Code hochladen</h1>
		<form method=post enctype=multipart/form-data>
		  <input type=file name=file>
		  <input type=submit value=Upload>
		</form>
		'''

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		if 'file' not in request.files:
			return html() + "</br>Bitte eine C Datei hochladen"
		file = request.files['file']
		if file.filename == '':
			return html() + "</br>Bitte eine C Datei hochladen"
		file.save(fn)
		try:
			check_file(fn)
			main()
		except Exception as e:
			return html() + "<pre>" + str(e) + "</pre>"
		return html() + "</br>Danke"
	return html()

#app.run(debug=False,threaded=False, processes=1)
