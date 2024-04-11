class min_list:
    # def __init__(self,list) -> None:
    #     self.List=list
    def minimumList(List):
        min=List[-1]
        for i in range(len(list)-1,-1,-1):
            if List[i] < min:
                min=List[i]
        return min


list=[1,4,25,2,4]

print(min_list.minimumList(list))
    