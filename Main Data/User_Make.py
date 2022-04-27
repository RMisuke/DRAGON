#正式的角色创建模块
#《DRAGON》 ver 0.1 Alpha Test
import sys
print("欢迎来到《DRAGON》,角色创建界面！")
print("你的名字是？")
Player_Name=input("")
print("你好！",Player_Name,"欢迎来到《DRAGON》")
list_Jobs=["剑士","弓箭手","魔法师",]
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