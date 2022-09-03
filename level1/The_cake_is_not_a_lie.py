def check(inpt):
    if len(inpt) <= 200 and inpt.isalpha() == True:
        return True
    return False
        

def solution(s):
    
    if check(s) == False:
        print("Invalid Input")

    strLength = len(s)

    for i in range(1, strLength):
        if strLength % i == 0:
            subStrings = [s[a: a + i] for a in range(0, strLength, i)]
            res = all(ele == subStrings[0] for ele in subStrings)
            print(str(subStrings) + " " + str(res))
            if res:
                return int(strLength / i)
    
    return 1


if __name__ == "__main__":
    slices = solution("aa")
    print("The Number of slice = " + str(slices))