while 1:
    print("\n----------------------- 指数表构造器   NEW SOLUTION -----------------------")
    root=eval(input("\n已知原根:    "))
    mod=eval(input("\n模数:    "))
    eular=eval(input("\n欧拉函数值:    "))
    num=1
    for i in range(0,eular):
        num=num*root;
        num=num-mod*(num//mod)
        print(root,"^",i+1,"≡",num,"( mod",mod," )")
    
