def twons(array,targetsum):
    nums ={}
    for num in array:
        potentialmatch = targetsum - num
        if potentialmatch in nums:
            return [potentialmatch,nums]
        else:
            nums[num]= True
    return []


def main():
    array = [8,2,-16,23,4]
    twons(array,10)


if __name__== "__main__":
  main()
