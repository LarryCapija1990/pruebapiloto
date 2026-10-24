#!/usr/bin/env python3
"""Servidor estático local del prototipo; no usa servicios ni credenciales."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from functools import partial
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--port',type=int,default=4173)
parser.add_argument('--host',default='127.0.0.1')
args = parser.parse_args()
root = Path(__file__).resolve().parent
print(f'F4 CP01: sirviendo {root} en puerto {args.port}',flush=True)
ThreadingHTTPServer((args.host,args.port),partial(SimpleHTTPRequestHandler,directory=str(root))).serve_forever()
