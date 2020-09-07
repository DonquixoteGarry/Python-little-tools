while 1:
    print("----------------------- 次数求解器   NEW SOLUTION -----------------------")
    under=eval(input("\nunder:    "))
    mod_num=eval(input("\nmod:    "))
    num=1
    for i in range(1,mod_num):
        num=num*under;
        num=num-mod_num*(num//mod_num)
        if num==1:
            print("\n>>>底数",under,"对模",mod_num,"的次数为",i,"\n")
            break
