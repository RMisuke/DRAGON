#整体系统测试文件
import sys
print("你的名字是？")
Player_Name=input("")
print("你好！",Player_Name,"欢迎来到《DRAGON》")
list_Jobs=["剑士","弓箭手"]
print("请选择你的职业：",list_Jobs[0:2])
Player_Job=input("")
Player_Level=1
Player_Health_Max=100
Player_Defend=10
Player_SP_Max=20
Player_Money=0
list_Skills=[]
list_Choose=["战斗","逃跑"]
if Player_Job == "剑士":
    print("选择成功")
    Player_AT=10
    Player_Speed=5
    Player_equipment="平凡的铁剑"
    list_Skills.append("全力劈砍")
elif Player_Job == "弓箭手":
    print("选择成功")
    Player_AT=5
    Player_Speed=10
    Player_equipment="平凡的木弓"
    list_Skills.append("快速射击")
else:
    print("无效的职业名")
    sys.exit(0)
print("好的",Player_Job,Player_Name)
print("当前能力值：")
print("|生命:",Player_Health_Max)
print("|法力:",Player_SP_Max)
print("|攻击:",Player_AT)
print("|速度:",Player_Speed)
print("|防御:",Player_Defend)
print("|装备:",Player_equipment)
print("|技能:",list_Skills)
print("|等级:",Player_Level)
print("|金钱:",Player_Money)
print("是否开始新的冒险？","y/n")
Choose=input("")
if Choose == "y":
    print("开始冒险！")
elif Choose =="n":
    print("那也要开始冒险！")
print("角色创建成功！")
print("正在保存……")
print("保存完毕！")
print("战斗演示模块，开始")
Monster_Name="史莱姆"
Monster_Level=Player_Level
Monster_Health=50
Monster_Defend=5
Monster_AT=5
Monster_Speed=7
Player_Health = Player_Health_Max
if Player_Speed > Monster_Speed:
    print("野生的", Monster_Name, "出现了！")
    print("先手攻击！")
else:
    print("野生的", Monster_Name, "冲过来了！")
    print("后手攻击！")
    print(Monster_Name, "对你使用了", "冲撞！")
    Player_Health = Player_Health - (Monster_AT - (Player_Defend * 0.2))
    print("你受到了", (Monster_AT - (Player_Defend * 0.2)), "点伤害！")
    print("当前生命", Player_Health, Monster_Name, "生命值:", Monster_Health)
while Player_Health > 0:
   if Monster_Health >0 and Player_Health >0:
     print("你要怎么做？",list_Choose)
     Choose=input("")
     if Choose == list_Choose[0]:
        print("选择攻击方式")
        print("['普通攻击']", list_Skills)
        Choose = input("")
        if Choose == "普通攻击":
            Monster_Health = Monster_Health - (Player_AT - (Monster_Defend * 0.2))
            print(Monster_Name, "受到了", (Player_AT - (Monster_Defend * 0.2)), "点伤害")
            print("当前生命", Player_Health, Monster_Name, "生命值:", Monster_Health)
        elif Choose == list_Skills[0]:
            Monster_Health = Monster_Health - (Player_AT - (Monster_Defend * 0.2) + 10)
            Player_SP = Player_SP_Max - 5
            print(Monster_Name, "受到了", (Player_AT - (Monster_Defend * 0.2) + 10), "点伤害")
            print("当前生命", Player_Health, Monster_Name, "生命值:", Monster_Health)
            print("当前法力:",Player_SP)
        print(Monster_Name, "对你使用了", "冲撞！")
        Player_Health = Player_Health - (Monster_AT - (Player_Defend * 0.2))
        print("你受到了", (Monster_AT - (Player_Defend * 0.2)), "点伤害！")
        print("当前生命", Player_Health, Monster_Name, "生命值:", Monster_Health)
     elif Choose == list_Choose[1]:
        print("你逃跑了！")
        break
   elif Monster_Health <= 0 and Player_Health > 0:
       Player_Money=Player_Money+10
       print("你胜利了")
       print("获得了金钱10","当前金钱:",Player_Money)
       break
   elif Monster_Health >0 and Player_Health <= 0:
       print("你失败了")
       break







