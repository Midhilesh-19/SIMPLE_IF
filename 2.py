user_floor=int(input("enter user:-"))
current_floor=int(input("enter current:-"))
diff=user_floor-current_floor
if diff<0:
    print("lift down")

if diff>0:
    print("lift up")
