"""Run from any directory with: python serve.py"""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path
root=Path(__file__).resolve().parent
print('Open http://127.0.0.1:8000/ ; press Ctrl+C to stop',flush=True)
ThreadingHTTPServer(('127.0.0.1',8000),partial(SimpleHTTPRequestHandler,directory=str(root))).serve_forever()
