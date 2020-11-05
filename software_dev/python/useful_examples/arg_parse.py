"""
args - using arg parse to parse the following args...

-f in file
-d destination
-n number of candidate images
-p number of simultaneous processes
"""
import argparse


def parseArguments():

    parser = argparse.ArgumentParser()
    
    parser.add_argument(type=str,dest="filename", 
        help="the source file (in CSV format) containing names of devices")
    
    parser.add_argument("-d",type=str,dest="dest", default=".",
        help = "folder where the candidate folder should be placed")
    
    parser.add_argument("-p",type=int,dest="processes",default="20",
        help = "max number of simultaneous download processes")
    
    parser.add_argument("-n",type=int,dest="candidates",default="50",
        help = "max number of candidates to search for with each device")

    
    return(parser.parse_args().filename,
            parser.parse_args().dest,
            parser.parse_args().processes,
            parser.parse_args().candidates
    )



if __name__ == "__main__":
    print(parseArguments())