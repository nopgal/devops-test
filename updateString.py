#!/usr/bin/python
from flask import Flask
from flask import request
app = Flask(__name__)

import sys, getopt
from re import sub

@app.route("/")
# upadting stringToUpdateing based on the acion: lowercase, uppercase, camelcase.
def main():
   # reading arguments into stringToUpdate and case_action   
   stringToUpdate = request.args.get("str")
   case_action = request.args.get("case")  
   
   match case_action:
        case 'lowercase':
            stringToUpdate = stringToUpdate.lower();
        case 'uppercase':
            stringToUpdate = stringToUpdate.upper();
        case 'camelcase':
            stringToUpdate = sub(r"(_|-)+", " ", stringToUpdate).title().replace(" ", "");
        case _:    
            stringToUpdate = stringToUpdate;

   print('Updated stringToUpdateing:', stringToUpdate)
   return stringToUpdate;

if __name__ == "__main__":
   app.run(host='0.0.0.0')
   
