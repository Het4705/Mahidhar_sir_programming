try:
    num=int(input("Enter a num"))
    assert num % 2 == 0           #* For forcefully passing exception
except:
    print("Not an even number")
else:
    reciprocal =1/num
    print(reciprocal)
finally:
    print(" It will be printed irrespective of Exception")