import csv
f=open("other.csv","w+",newline="")
mov_writer=csv.writer(f)
mov_writer.writerows([["Movie Name","Trailer"],
                      ["Aamis","https://www.youtube.com/watch?v=-zv11DpavFI"],
                      ["Kothanodi","https://www.youtube.com/watch?v=rgzYIOV374I"],
                      ["Village rockstars","https://www.youtube.com/watch?v=tTov2nVgXaU"],
                      ["Hellaro","https://www.youtube.com/watch?v=qb8uOylK3R4"],
                      ["Goodachari","https://www.youtube.com/watch?v=V-8GGhn0oDk"],
                      ["Kavaludaari","https://www.youtube.com/watch?v=5w1vgMoPMRA"],
                      ["Agent Sai Srinivasa Athreya","https://www.youtube.com/watch?v=iPfVbR5oAWE"],
                      ["HIT:The first case","https://www.youtube.com/watch?v=uYdsWe9iBAA"],
                      ["NANI's GANGLEADER","https://www.youtube.com/watch?v=AjAe_Q1WZ_8"],
                      ["Jersey","https://www.youtube.com/watch?v=AjAe_Q1WZ_8"],
                      ["1Awe!","https://www.youtube.com/watch?v=xOEscQChX7M"],
                      ["Gentleman","https://www.youtube.com/watch?v=MgmowJ5r-es"],
                      ["Sairat","https://www.youtube.com/watch?v=wMrMKnoYWwA"],
                      ["Mathu vadalara","https://www.youtube.com/watch?v=tmb2G-C6byM"],
                      ["Gantumoote","https://www.youtube.com/watch?v=CY5c2VNaI2s"],
                      ["Rangitaranga","https://www.youtube.com/watch?v=L8wWqg2oYiQ"],
                      ["KGF:Chapter1","https://www.youtube.com/watch?v=qXgF-iJ_ezE"],
                      ["Pelli choopulu","https://www.youtube.com/watch?v=zHO7BuWCHK8"],
                      ["Lucia","https://www.youtube.com/watch?v=pgIL2H-OdcA"],
                      ["Kirik Party","https://www.youtube.com/watch?v=IfvnbER_6sQ"],
                      ["Ulidavaru Kandante","https://www.youtube.com/watch?v=POJ_6EtGeMw"],
                      ["Avane Srimannarayana","https://www.youtube.com/watch?v=Dj-HNEZ59Z4"],
                      ["The gangster,the cop,the devil","https://www.youtube.com/watch?v=hS-fztIL8HE"],
                      ["Oldboy","https://www.youtube.com/watch?v=2HkjrJ6IK5E"],
                      ["Parasite","https://www.youtube.com/watch?v=5xH0HfJHsaY"],
                      ["I saw the devil","https://www.youtube.com/watch?v=xwWgp1bqVwE"],
                      ["Train to Busan","https://www.youtube.com/watch?v=pyWuHv2-Abk"],
                      ["Peninsula","https://www.youtube.com/watch?v=2kE1Ydf4jIo"],
                      ["U-Turn","https://www.youtube.com/watch?v=Kdh5P8dtMXA"],
                      ["Yatra","https://www.youtube.com/watch?v=OuIJDxLeEBc"],
                      ["Godhi banna sadharana mykattu","https://www.youtube.com/watch?v=aPk9fBdtugg"],
                      ["Uma maheswara ugra roopasya","https://www.youtube.com/watch?v=ggzOfWWpoK8"],
                      ["C/o Kancharapalem","https://www.youtube.com/watch?v=-YeQZwlNeaY"],
                      ["Rangasthalam","https://www.youtube.com/watch?v=sueMmTm-M4Y"],
                      ["Oopiri","https://www.youtube.com/watch?v=e1ddsJ38D5Q"],
                      ["Thithi","https://www.youtube.com/watch?v=Q_NltD4Stv4"],
                      ["Dia","https://www.youtube.com/watch?v=mMqcXDkCRLs"],
                      ["Mufti","https://www.youtube.com/watch?v=PdH5AcS7BR4"],
                      ["Ugramm","https://www.youtube.com/watch?v=f7XQSsZLjmo"],
                      ["Katha Sangama","https://www.youtube.com/watch?v=2a8hE5Y9pH4"],
                      ["Memories of murder","https://www.youtube.com/watch?v=-YvWR3Bds0A"],
                      ["Miracle in cell no.7","https://www.youtube.com/watch?v=tvJQoFGKA0Y"],
                      ["Natarang","https://www.youtube.com/watch?v=CnXdnNAyaY0"],
                      ["Natsamrat","https://www.youtube.com/watch?v=DCXDyIsPEN8"],
                      ["Bulbul can sing","https://www.youtube.com/watch?v=6DsjnhSR9ww"],
                      ["Evaru","https://www.youtube.com/watch?v=TfW6lil5uyc"],
                      ["Kshanam","https://www.youtube.com/watch?v=OroFSmQQm1U"]])
                      


f.close()

def Display():
    f=open("Other.csv","r")
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
    f=open("Other.csv","r")
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
    var=input("1.Press D to display the movies in the database.\n2.Press S to search if a movie is in the database.\n3.Press E to Exit.\n")
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
    
