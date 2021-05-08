#python pinpon game
#created by yunus arli
#01.29.2021
import random, pygame, sys
from pygame.locals import *
import time
import math
#maçtaki skorları tutabilmek için oluşturulan bir py dosyası
from test import FileRead
from pygame import mixer


def main():

    pygame.init()
    window = (800,400)
    FPS = 30
    clock = pygame.time.Clock()
    DİSPLAYSURF = pygame.display.set_mode(window)
    pygame.display.set_caption("Python Pinpon Game")
    #cubuğun y eksenindeki yeri
    y_stick = 200  
    #topun eksenlerdeki yerleri
    x_ball = 400
    y_ball = 200
    #x ve y eksenlerindeki hızları
    vel_ball_y = 4
    vel_ball_x = 7
    #cubuğun hızı
    vel_stick = 10
    #cubukların boyu
    width = 10
    height = 70
    #daima aynı yönde oyuna başlamarını engellemek
    vel_ball_x = up_or_down(vel_ball_x)
    vel_ball_y = up_or_down(vel_ball_y)
    #skorboard
    score = 0
    pygame.font.init()
    mixer.init()
    bg_image = pygame.image.load("pinpon.png")
    #for crashing
    mixer.music.load("match1.wav")
    mixer.music.set_volume(0.7)

    #belli bir süre oyunun hızını artırmak.her 1000*30 fps hızda +1 fps hız
    speed = 0
    #oyuncu oyunu kaybettiğinde pencerenin kapanacağı süre counter/300 = 1sn
    counter = 900
    #oyuncu oyunu kaybetti mi?
    lose = False
    # en yüksek skorun tutlacağı bir text dosyası
    FİLENAME = "scores.txt"
    #dökümantasyon için test.py-->
    myFile = FileRead(FİLENAME)
    highest = myFile.highest()
    myFile.clear()
    myFile.add(highest)
    while True:
        speed+=1
        if speed%1000==0:
            FPS+=1


        clock.tick(FPS)#kabul edilebilir bir hız için
        #DİSPLAYSURF.fill((0,0,0))
        DİSPLAYSURF.blit(bg_image,(0,0))
        #klavye olayları
        keys=pygame.key.get_pressed()

        if not lose:
            if keys[K_UP] and y_stick>0+vel_stick:
                y_stick-=vel_stick
            elif keys[K_DOWN] and y_stick<400-height-vel_stick:
                y_stick+=vel_stick
        if lose:
            if keys[K_RETURN]:
                lose = False
                main()
        
        x_ball+=vel_ball_x#oyun başladığında topu harekete geçirmek

        #topun dışarı çıkmasını engellemek(x ekseninde)
        if x_ball==15 and y_stick-(math.sin(45)*10)<=y_ball<=y_stick+height + (math.sin(45)*10):#topun açılı geldiği durumlarda merkezi en uca taşımak için kullanılan sinüs fonksiyonları
            vel_ball_x  = vel_ball_x*-1
            score+=1
            #dosyaya skorların eklenmesi
            myFile.add(score)
            mixer.music.play()

        elif x_ball==785 and y_stick-(math.sin(45)*10)<=y_ball<=y_stick+height+ (math.sin(45)*10):
            vel_ball_x = vel_ball_x*-1
            score+=1
            myFile.add(score)
            mixer.music.play()
        elif x_ball>=820 or x_ball<=-20:
            counter-=1
            lose = True


            scorefont = pygame.font.SysFont('Comic Sans MS', 20)
            textsurface = scorefont.render("You lost.Press enter to replay Score  : "+str(score)+"highest score :{}".format(myFile.highest()), False, (255, 255, 255))
            DİSPLAYSURF.blit(textsurface,(75,170))

            
            
            counter_font = pygame.font.SysFont('Sans MS', 30)
            counter_surface = counter_font.render("Remaining time to close game  : "+str(counter//30), False, (255, 255, 255))
            DİSPLAYSURF.blit(counter_surface,(75,270))
            if counter==0:
                sys.exit()


        y_ball+=vel_ball_y
        #topun dışarı çıkmasını engellemek(y ekseninde)
        if y_ball>=390:
            vel_ball_y = vel_ball_y*-1

        elif y_ball<=10:
            vel_ball_y = vel_ball_y*-1 
        
        #çubuk ve topun yerleri
        pygame.draw.rect(DİSPLAYSURF, (255, 0, 0), ((0,y_stick,width,height)))
        pygame.draw.rect(DİSPLAYSURF, (255, 0, 0), ((790,y_stick,width,height)))
        pygame.draw.circle(DİSPLAYSURF,(255,0,255),(x_ball,y_ball),10) 

        #skoru yazdırmak
        scorefont = pygame.font.SysFont('Comic Sans MS', 15)
        textsurface = scorefont.render("Score  : "+str(score), False, (255, 255, 255))
        DİSPLAYSURF.blit(textsurface,(50,20))#putting scoreboard in a randomly place

        #çıkış operasyonları
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()#oyunun sürekli güncellenmesini istiyoruz
        
        

def up_or_down(vel):
    #topun başlangıç yönünü belirmeye çalışıyoruz.
    import random
    res = [vel,-vel]
    random.shuffle(res)
    return res[0]


if __name__=="__main__":
    main()