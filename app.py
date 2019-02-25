
import os
import tornado.httpserver
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json
items=[]

class LoanDecision(RequestHandler):
  def set_default_headers(self):
  	self.set_header("Access-Control-Allow-Origin", "*")
  	self.set_header("Access-Control-Allow-Headers", "x-requested-with,access-control-allow-origin,authorization,content-type")
  	self.set_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')

  def post(self):
  	print(self.request.body)
  	var = json.loads(self.request.body)
  	print(var)
  	print(self.request.body)
  	decision =""
  	loanAmount = var['requestedAmount']
  	print(loanAmount)

  	if loanAmount == 500000:
  		decision = "Undecided"
  	elif loanAmount < 500000:
  		decision = "Approved"
  	elif loanAmount > 500000:
  		decision = "Declined"
  	print(decision)
  	self.write({'decision':decision})

def make_app():
  urls = [
    ("/api/loandecision/", LoanDecision)
  ]
  return Application(urls, debug=True)
  
if __name__ == '__main__':
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()