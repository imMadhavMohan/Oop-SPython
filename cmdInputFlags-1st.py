import argparse

name = None
age = None
quali = None

def details():
    parser = argparse.ArgumentParser(description='Details') 
    parser.add_argument('-n','--name',required=True,type=str,help='name')
    parser.add_argument('-a','--age',required=True,type=int,help='age')
    parser.add_argument('-q','--quali',required=True,type=str,help='qualification')
    args = parser.parse_args()
    print(f'{args.name}, {args.age}, {args.quali}')
  
details()  

# Run Using These Commands
# Long formate:
    # python MyTest.py --name Mukund --age 23 --quali Mtech(VLSi)
# Short formate:
    # python MyTest.py -n Mukund -a 23 -q Mtech(VLSi)