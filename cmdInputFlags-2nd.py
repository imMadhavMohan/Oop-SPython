import sys
import getopt

name = None
age = None
quali = None

# first argument is the filename itself with an index of 0
# so, we want to start with an index value of 1
argv = sys.argv[1:]


def details():
    try:
        opts, args = getopt.getopt(argv, "n:a:q:", ["name=", "age=", "quali="])

    except getopt.GetoptError as err:
        print(err)          # will print something like "option -a not recognized"        

    for opt, arg in opts:
        if opt in ["-n", "--name"]:
            name = arg

        elif opt in ["-a", "--age"]:
            age = arg

        elif opt in ["-q", "--quali"]:
            quali = arg


details()  # Call to function

# Won't print unless will get all 3 values (More Restricted)
if((name is not None) and (age is not None) and (quali is not None)):
    print(f'name: {name}')
    print(f'age: {age}')
    print(f'quali: {quali}')
else:
    sys.exit('INVALID INPUT')  # immidiately terminate the program
  

# Run Using These Commands
# Long formate:
    # python Test.py --name Madhav --age 23 --quali Btech
# Short formate:
    # python Test.py -n Madhav -a 23 -q Btech
