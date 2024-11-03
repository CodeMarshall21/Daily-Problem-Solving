nums = [num for num in range (1,101)]
print("Think of a number between 1 and 100")

low = 0
high = len(nums) - 1

while (low <= high): 
    mid = (low + high)//2
    print("Is it", nums[mid] ,"?")
    val = input()
    if(val == 'c'):
        print("***end***")
        break
    elif(val == 'h'):
        high = mid
    elif(val == 'l'):
        low = mid
    else:
        print("---Invalid Input---")


