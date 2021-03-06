import csv
f=open("Hindi.csv","w",newline="")
mov_writer=csv.writer(f)
mov_writer.writerows([["Movie Name","Trailer"],
                      ["Dangal","https://www.youtube.com/watch?v=x_7YlGv9u1g"],
                      ["3 Idiots","https://www.youtube.com/watch?v=K0eDlFX9GMc"],
                      ["Angrezi Medium","https://www.youtube.com/watch?v=rzlfeocUVhI"],
                      ["Mard Ko Dard Nahi Hota","https://www.youtube.com/watch?v=jb0-Mw_V_bA"],
                      ["Aashiqui 2","https://www.youtube.com/watch?v=Fb0qB11Sb1E"],
                      ["Dil Chahata Hai","https://www.youtube.com/watch?v=m13b25V0B10"],
                      ["Zindagi Na Milegi Dobara","https://www.youtube.com/watch?v=FJrpcDgC3zU"],
                      ["Bhavesh Joshi Superhero","https://www.youtube.com/watch?v=RYsdZHc7MI8"],
                      ["Chak De! India","https://www.youtube.com/watch?v=6a0-dSMWm5g"],
                      ["Andhadhun","https://www.youtube.com/watch?v=2iVYI99VGaw"],
                      ["Queen","https://www.youtube.com/watch?v=KGC6vl3lzf0"],
                      ["Chhichhore","https://www.youtube.com/watch?v=tsxemFX0a7k"],
                      ["M.S Dhoni: The Untold Story","https://www.youtube.com/watch?v=6L6XqWoS8tw"],
                      ["Taare Zameen Par","https://www.youtube.com/watch?v=tn_2Ie_jtX8"],
                      ["Lunchbox","https://www.youtube.com/watch?v=IJIGJtb_N7E"],
                      ["Karwaan","https://www.youtube.com/watch?v=IUCeN7kelXs"],
                      ["PK","https://www.youtube.com/watch?v=SOXWc32k4zA"],
                      ["Badla","https://www.youtube.com/watch?v=xHWQiok-ei0"],
                      ["Piku","https://www.youtube.com/watch?v=oeiKUlUUNQ8"],
                      ["Airlift","https://www.youtube.com/watch?v=vb5xCMbMfZ0"],
                      ["Khuda Haafiz","https://www.youtube.com/watch?v=ByYWL1SEe-k"],
                      ["Malang","https://www.youtube.com/watch?v=sft5baUuzQs"],
                      ["The Sky Is Pink","https://www.youtube.com/watch?v=prwUFBsDRLk"],
                      ["Dishoom","https://www.youtube.com/watch?v=DU6IdS2gVog"],
                      ["Thappad","https://www.youtube.com/watch?v=jBw_Eta0HDM"],
                      ["Lootcase","https://www.youtube.com/watch?v=Q9ij1MUCXVg"],
                      ["Luka Chuppi","https://www.youtube.com/watch?v=-JLewvWBkCw"],
                      ["Super 30","https://www.youtube.com/watch?v=QpvEWVVnICE"],
                      ["Omerta","https://www.youtube.com/watch?v=ikf3UodZJHA"],
                      ["Badhai Ho","https://www.youtube.com/watch?v=unAljCZMQYw"],
                      ["Parmanu: The Story of Pokhran","https://www.youtube.com/watch?v=qN_9DnBh3hM"],
                      ["Sanju","https://www.youtube.com/watch?v=1J76wN0TPI4"],
                      ["Raazi","https://www.youtube.com/watch?v=YjMSttRJrhA"],
                      ["Ek Villian","https://www.youtube.com/watch?v=ruO0VrqOkdE"],
                      ["Padmavaat","https://www.youtube.com/watch?v=XgUBV9p9jfk&list=PL0ZrCfkcPKNz-5Fy0uIQ2qZgAM1GXjkup&index=27&t=0s"],
                      ["October","https://www.youtube.com/watch?v=VjPePUA6MO4"],
                      ["Dil Dhadakane Do","https://www.youtube.com/watch?v=qfnJCv4_1Ts"],
                      ["Haider","https://www.youtube.com/watch?v=ZmN_VSo8DOo"],
                      ["2 States","https://www.youtube.com/watch?v=CGyAaR2aWcA"],
                      ["Tumbbad","https://www.youtube.com/watch?v=sN75MPxgvX8"],
                      ["Andaz Apna Apna","https://www.youtube.com/watch?v=fd_w7Qw8biU"],
                      ["Lagaan","https://www.youtube.com/watch?v=oSIGQ0YkFxs"],
                      ["Munna Bhai MBBS","https://www.youtube.com/watch?v=6lCGvu-hwX4"],
                      ["Khoobsurat","https://m.youtube.com/watch?v=pOreDBy1YfI&list=PLjKvpT-8JGXHs2bmMBZ7vIbxIWFBEKWXW&index=7&t=0s"],
                      ["Vicky Donor","https://www.youtube.com/watch?v=Jme-VkIzkoU"],
                      ["Jab We Met","https://www.youtube.com/watch?v=i7VGyugYCIk"],
                      ["Yeh Jawaani Hai Deewani","https://www.youtube.com/watch?v=Rbp2XUSeUNE"],
                      ["Wake Up Sid","https://www.youtube.com/watch?v=Ngimy3GpHS0"],
                      ["English Vinglish","https://www.youtube.com/watch?v=wmGVY4T88dc"],
                      ["Barilly Ki Barfi","https://www.dailymotion.com/video/x5u6znl"],
                      ["Tanu Weds Manu","https://www.youtube.com/watch?v=hq0RMAuQGWA"],
                      ["Shubh Mangal Savadhan","https://www.youtube.com/watch?v=r6r8UYU7Zcs"],
                      ["Dostana","https://www.youtube.com/watch?v=PYNpmI_MHXc"],
                      ["Hera Pheri","https://www.youtube.com/watch?v=BtQqo_4ypkM"],
                      ["Dilwale Dulhania Le Jayenge","https://www.youtube.com/watch?v=cmax1C1p660Z"],
                      ["Uri: The Surgical Strike","https://www.youtube.com/watch?v=VVY3do673Zc"],
                      ["The Body","https://www.youtube.com/watch?v=4f9jIdg4rTQ"],
                      ["Hamari Adhuri Kahani","https://www.youtube.com/watch?v=2fiT_TJlySk"],
                      ["Madari","https://www.youtube.com/watch?v=j4s3JmLGLCA"],
                      ["Gangs Of Wasseypur","https://www.youtube.com/watch?v=j-AkWDkXcMY"],
                      ["Talwar","https://www.youtube.com/watch?v=aQNMsw8Ljjc"],
                      ["Rockstar","https://www.youtube.com/watch?v=bD5FShPZdpw"],
                      ["Barfi","https://www.youtube.com/watch?v=nQ3FYUgSjC8"],
                      ["Kai Po Che","https://www.youtube.com/watch?v=G19faYsLtlc"],
                      ["Gully Boy","https://www.youtube.com/watch?v=JfbxcD6biOk"],
                      ["Paan Sing Tomar","https://www.youtube.com/watch?v=A0cT7ukL4GI"],
                      ["Sholay","https://www.youtube.com/watch?v=zzTUvWfvlBg"],
                      ["Tamasha","https://www.youtube.com/watch?v=o-e5eWVCzx8"],
                      ["Bajrangi Bhaijaan","https://www.youtube.com/watch?v=Oz_ZJhcOX1E"],
                      ["Masaan","https://www.youtube.com/watch?v=SKJfBo3xMW0"],
                      ["Pink","https://www.youtube.com/watch?v=AL2TShb6fFs"],
                      ["Article 15","https://www.youtube.com/watch?v=HKOJY0cU63E"],
                      ["Mughal E Azam","https://www.youtube.com/watch?v=rXz_vWzMh_U"],
                      ["Highway","https://www.youtube.com/watch?v=LSrDD52bx4A"],
                      ["Shahid","https://www.youtube.com/watch?v=2p8LyAte-M8"],
                      ["Hindi Medium","https://www.youtube.com/watch?v=GjkFr48jk68"],
                      ["Rocket Singh - Salesman of the Year ","https://www.youtube.com/watch?v=MctcqGHpfdM"],
                      ["Hum Apke Hain Kon","https://www.youtube.com/watch?v=45JY12a6zJA"],
                      ["Koi Mil Gaya","https://www.youtube.com/watch?v=IBpZH-CFgZ0"],
                      ["Kuch Kuch Hota Hai","https://www.youtube.com/watch?v=05i3eIuJLaU"],
                      ["Paa","https://www.youtube.com/watch?v=mTjEWy4InQ4"],
                      ["Slumdog Millionaire","https://www.youtube.com/watch?v=AIzbwV7on6Q"],
                      ["Om Shanti Om","https://www.youtube.com/watch?v=9oeGoQGt7Ao"],
                      ["Guru","https://www.youtube.com/watch?v=D1eE-lCKcxI"],
                      ["Azhar","https://www.youtube.com/watch?v=C1MOI8vaQos"],
                      ["Padman","https://www.youtube.com/watch?v=-K9ujx8vO_A"],
                      ["Bajirao Mastani","https://www.youtube.com/watch?v=eHOc-4D7MjY"],
                      ["Kahaani","https://www.youtube.com/watch?v=j1wEeuAosNM"],
                      ["Chennai Express","https://www.youtube.com/watch?v=hZGR5Sj1Bfo"],
                      ["Batla House","https://www.youtube.com/watch?v=dG3K6jB3iW8"],
                      ["Mission Mangal","https://www.youtube.com/watch?v=q10nfS9V090"],
                      ["Baby","https://www.youtube.com/watch?v=vKXHxluLTUo"],
                      ["Kapoor And Sons","https://www.youtube.com/watch?v=s7YYt9_KfsM"],
                      ["Kaabil","https://www.youtube.com/watch?v=nubDFeiUAsI"],
                      ["Game Over","https://www.youtube.com/watch?v=BY-R6NcnkbE"],
                      ["Ae Dil Hai Mushkil","https://www.youtube.com/watch?v=Z_PODraXg4E"],
                      ["Goliyon Ki Raasleela Ram-Leela","https://www.youtube.com/watch?v=StphRCLkx6Q"],
                      ["Hasee Toh Phasee","https://www.youtube.com/watch?v=Xv5MG0LhaP4"],
                      ["Dum Laga Ke Haisha","https://www.youtube.com/watch?v=lFZpPpSU3k0&vl=en"],
                      ["Bala","https://www.youtube.com/watch?v=veJ6ejMjzgE"],
                      ["Badlapur","https://www.youtube.com/watch?v=9KEoZanqlOE"]])

f.close()

#def Add():
    #f=open("Hindi.csv","a")
    #mov_writer=csv.writer(f)
    #Movie=input("Enter Movie Name:")
    #Link=input("Enter Trailer Link:")
    #mov_writer.writerow([Movie,Link])
    #f.close()

def Display():
    f=open("Hindi.csv","r")
    mov_reader=csv.reader(f)
    Var=0
    next(mov_reader)
    try:
        for rec in mov_reader:
            print(rec[0])
            Var+=1
        print("Total Number of Movies In the database:",Var,"movies")
    except IndexError:
        pass
    f.close()

def Search():
    f=open("Hindi.csv","r")
    mov_reader=csv.reader(f)
    Movie_Name=input("Enter the Movie Name that you want to Search:")
    Var=False
    for rec in mov_reader:
        if rec[0].casefold()==Movie_Name.casefold():
            Var=True
    if Var==True:
        print("Movie Found")
    else:
        print("Movie Not Found!")
    

while True:
    var=input("1.Press A to add more movies to th database.\n2.Press D to display the movies in the database.\n3.Press S to search if a movie is in the database.\n4.Press E to Exit.\n")
    #if var in "Aa":
        #Add()
    if var in "Dd":
        Display()
    elif var in "Ss":
        Search()
    elif var in "Ee":
        break
    else:
        continue
    











    

