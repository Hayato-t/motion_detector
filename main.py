import pylab
import numpy
import network_schema as ns
import sys

def main(args):
  # args[1]: network schema definition file path
  # args[2]: network celltype and amount definition file path
  # args[3]: network option file path
  # load configuration file
  Network = ns.generate_network_from_file(args[1],args[2], opt=args[3])
  
  

if __name__ == '__main__':
  main(sys.argv)


