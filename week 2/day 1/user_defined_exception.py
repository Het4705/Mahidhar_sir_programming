class MaxLimitError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return super().__str__()

arr=[]
while(True):
    x=input("Enter")
    if(len(arr)>5):
        raise MaxLimitError
    
    arr.append(x)



