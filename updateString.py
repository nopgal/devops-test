#!/usr/bin/python

import sys, getopt
from re import sub


# upadting stringToUpdateing based on the acion: lowercase, uppercase, camelcase.
def stringUpdate(stringToUpdate, case_action):
   match case_action:
        case 'lowercase':
            stringToUpdate = stringToUpdate.lower();
        case 'uppercase':
            stringToUpdate = stringToUpdate.upper();
        case 'camelcase':
            stringToUpdate = sub(r"(_|-)+", " ", stringToUpdate).title().replace(" ", "");
        case _:    
            stringToUpdate = stringToUpdate;
   return stringToUpdate;


def main(argv):
   
   # reading arguments into stringToUpdate and case_action
   stringToUpdate = ''
   case_action = ''
   try:
      opts, args = getopt.getopt(argv,"hs:c:",["stringToUpdateToUpdate=","action="])
   except getopt.GetoptError:
      print ('updatestringToUpdateing.py -s <stringToUpdate> -c <case_action>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('Usage: updatestringToUpdateing.py -s <stringToUpdate> -c <case_action>')
         print ('Usage: cases suported are lowercase, uppercase, camelcase. Other input will result in the original stringToUpdateing.')
         sys.exit()
      elif opt in ("-s", "--stringToUpdateToUpdate"):
         stringToUpdate = arg
      elif opt in ("-c", "--action"):
         case_action = arg

   print ('original stringToUpdateing:', stringToUpdate);
   print ('action is:', case_action);

   stringToUpdate = stringUpdate(stringToUpdate, case_action);
   print('Updated stringToUpdateing:', stringToUpdate)

if __name__ == "__main__":
   case_action = main(sys.argv[1:])
