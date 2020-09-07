while 1:
    print("----------------------- 原根提取器   NEW SOLUTION -----------------------")
    mod_num=eval(input("\n模数:    "))
    fai=eval(input("\n模数的Eular函数:    "))
    ord=1
    for j in range(1,mod_num):
        num=1
        for i in range(1,mod_num):
            num=num*j;
            num=num-mod_num*(num//mod_num)
            if num==1:
                ord=i
                if ord==fai:
                    print(j,",",end="")
                break
    print("\n\n>>>SOLUTION END\n")
