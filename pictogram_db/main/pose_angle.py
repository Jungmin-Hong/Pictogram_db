#왼쪽 팔각도 L_arm
#오른쪽 팔각도 R_arm
#왼쪽 겨드랑이 L_gyeo
#오른쪽 겨드랑이 R_gyeo
#왼쪽 골반 L_hip
#오른쪽 골반 R_hip
#왼쪽 무릎 L_knee
#오른쪽 무릎 R_knee

from models import User
# from cam import getCal

# 여기에다가 캠에서 받아온 각도 추출한 것 각도 저장하고 L_arm등에 받아오기

def getCal(L_arm, L_gyeo, L_hip, L_knee, R_arm, R_gyeo, R_hip, R_knee):
    usertable = User()
    usertable.score=0
    """
    #동작1-태권도
    if(L_arm >= 80 and L_arm <= 110):
        if(L_gyeo >= 40 and L_gyeo <= 60):
            if(L_hip >= 110 and L_hip <= 130):
                if(L_knee >= 95 and L_knee <= 125):
                    if(R_arm >= 170 and R_arm <= 190):
                        if(R_gyeo >= 20 and R_gyeo <= 25):
                            if(R_hip >= 125 and R_hip <= 145):
                                if(R_knee >= 165 and R_knee <= 190):
                                    usertable.score += 200
                                    print ("Taekwondo")

    #동작2-전사포즈
    if(L_arm >= 170 and L_arm <= 190):
        if(L_gyeo >=80 and L_gyeo <= 110):
            if(L_hip >= 80 and L_hip <= 110):
                if(L_knee >= 80 and L_knee <= 110):
                    if(R_arm >= 170 and R_arm <= 190):
                        if(R_gyeo >= 80 and R_gyeo <= 110):
                            if(R_hip >= 125 and R_hip <= 145):
                                if(R_knee >= 170 and R_knee <= 190):
                                    usertable.score += 300
                                    print ("Warrior")

    #동작3-나무1(여자)
    if(L_arm >= 15 and L_arm <= 40):
        if(L_gyeo >= 95 and L_gyeo <= 110):
            if(L_hip >= 90 and L_hip <= 120):
                if(L_knee >= 30 and L_knee <= 45):
                    if(R_arm >= 15 and R_arm <= 40):
                        if(R_gyeo >= 95 and R_gyeo <= 110):
                            if(R_hip >= 170 and R_hip <= 190):
                                if(R_knee >= 170 and R_knee <= 190):
                                    usertable.score += 200
                                    print ("Tree 1")

    #동작4-나무2(남자)
    if(L_arm >= 160 and L_arm <= 185):
        if(L_gyeo >= 170 and L_gyeo <= 190):
            if(L_hip >= 90 and L_hip <= 120):
                if(L_knee >= 30 and L_knee <= 45):
                    if(R_arm >= 160 and R_arm <= 185):
                        if(R_gyeo >= 170 and R_gyeo <= 190):
                            if(R_hip >= 170 and R_hip <= 190):
                                if(R_knee >= 170 and R_knee <= 190):
                                    usertable.score += 100
                                    print ("Tree 2")

    #동작5-나무3(똥머리)
    if(L_arm >= 160 and L_arm <= 185):
        if(L_gyeo >= 150 and L_gyeo <= 170):
            if(L_hip >= 170 and L_hip <= 190):
                if(L_knee >= 170 and L_knee <= 190):
                    if(R_arm >= 170 and R_arm <= 190):
                        if(R_gyeo >= 45 and R_gyeo <= 70):
                            if(R_hip >= 85 and R_hip <= 115):
                                if(R_knee >= 30 and R_knee <= 45):
                                    usertable.score += 150
                                    print ("Tree 3")

    #동작6-십자가
    if(L_arm >= 170 and L_arm <= 190):
        if(L_gyeo >= 80 and L_gyeo <= 100):
            if(L_hip >= 170 and L_hip <= 190):
                if(L_knee >= 170 and L_knee <= 190):
                    if(R_arm >= 170 and R_arm <= 190):
                        if(R_gyeo >= 80 and R_gyeo <= 100):
                            if(R_hip >= 170 and R_hip <= 190):
                                if(R_knee >= 170 and R_knee <= 190):
                                    usertable.score += 50
                                    print ("Cross")
    """

    #동작1 - 니가 사는 그집(your_home)
    if(L_arm >= 120 and L_arm <= 170):
        if(L_gyeo >= 160 and L_gyeo <= 180):
            if(L_hip >= 120 and L_hip <= 180):
                if(L_knee >= 155 and L_knee <= 180):
                    if(R_arm >= 120 and R_arm <= 170):
                        if(R_gyeo >= 160 and R_gyeo <= 180):
                            if(R_hip >= 80 and R_hip <= 130):
                                if(R_knee >= 75 and R_knee <= 110):
                                    usertable.score += 200
                                    print("Your Home")

    #동작2 - 전사 포즈(warrior)
    if(L_arm >= 155 and L_arm <= 180):
        if(L_gyeo >= 80 and L_gyeo <= 110):
            if(L_hip >= 90 and L_hip <= 140):
                if(L_knee >= 100 and L_knee <= 160):
                    if(R_arm >= 155 and R_arm <= 180):
                        if(R_gyeo >= 80 and R_gyeo <= 110):
                            if(R_hip >= 130 and R_hip <= 160):
                                if(R_knee >= 170 and R_knee <= 190):
                                    usertable.score += 300
                                    print("Warrior")

    #동작3 - 서 (seo)
    if(L_arm >= 165 and L_arm <= 195):
        if(L_gyeo >= 65 and L_gyeo <= 100):
            if(L_hip >= 60 and L_hip <= 85):
                if(L_knee >= 165 and L_knee <= 195):
                    if(R_arm >= 165 and R_arm <= 195):
                        if(R_gyeo >= 100 and R_gyeo <= 140):
                            if(R_hip >= 140 and R_hip <= 180):
                                if(R_knee >= 165 and R_knee <= 195):
                                    usertable.score += 500
                                    print("Seo")

    #동작4 - Y
    if(L_arm >= 160 and L_arm <= 180):
        if(L_gyeo >= 150 and L_gyeo <= 170):
            if(L_hip >= 160 and L_hip <= 180):
                if(L_knee >= 160 and L_knee <= 180):
                    if(R_arm >= 160 and R_arm <= 180):
                        if(R_gyeo >= 150 and R_gyeo <= 170):
                            if(R_hip >= 160 and R_hip <= 180):
                                if(R_knee >= 160 and R_knee <= 180):
                                    usertable.score += 100
                                    print("Y")

    #동작5 - 가랑이 삼각형(triangle)
    if(L_arm >= 150 and L_arm <= 180):
        if(L_gyeo >= 100 and L_gyeo <= 125):
            if(L_hip >= 130 and L_hip <= 180):
                if(L_knee >= 120 and L_knee <= 180):
                    if(R_arm >= 150 and R_arm <= 180):
                        if(R_gyeo >= 90 and R_gyeo <= 130):
                            if(R_hip >= 120 and R_hip <= 160):
                                if(R_knee >= 70 and R_knee <= 100):
                                    usertable.score += 200
                                    print("Triangle")