import sys
list=['a',0,2]

for entry in list:
    try:
        print("The entry:",entry)
        r=1/int(entry)
        break
    except:
        print("ah shit here we go again:",sys.exc_info(),"occured")
        print("Next entry")
        print()
    # print("reciprocal of",entry,"is",rs)
        