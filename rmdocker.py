import sys, os


list_ID = [ "71d6bbd19390", "e613dcacdf1f", "0c0f909cb7c5", "f7495220217b", "02e7df5644d0" ,"6467c8336394",
"619640d38e", "10d3db034b03", "04c16e311d11", "d3f02aa4e8a5", "c028aca4bf6b","8182da428eb1" ]

def killer():
    for elem in list_ID:
     command = "sudo docker rm -f {}".format(elem)
     os.system(command)


if __name__ == "__main__" :

    killer()



class Polygone :
    __init__(self, sides, name):
        self.sides = sides 
        self.name = name
        
