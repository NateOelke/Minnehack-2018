import csv
import random

with open('exampledata.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'age', 'height', 'weight', 'qb', 'te', 'ot', 'og', 'c', 'rb', 'wr', 'de', 'dt', 'lb', 'cb', 's', 'kp', 'ls',  'years', 'games', 'hours', 'weeks', 'squat', 'bench', 'clean', 'dash', 'exercise', 'concussion_old', 'bone_old', 'ligament_old', 'muscle_old', 'joint_old', 'tendonitis_old', 'sprain_old', 'meniscus_old', 'concussion_new', 'bone_new', 'ligament_new', 'muscle_new', 'joint_new', 'tendonitis_new', 'sprain_new', 'meniscus_new', 'total_new']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range (1000):
        
        #age
        r = random.random()
        if(r < 0.05):
            age = 14
        elif(r < 0.15):
            age = 15
        elif(r < 0.35):
            age = 16
        elif(r < 0.75):
            age = 17
        else:
            age = 18
            
        height = random.normalvariate(72,2)
        weight = random.normalvariate(175,10)
        years = int(3*random.random()) + 1
        games = int(30*random.random()) + 1
        lift = int(30*random.random()) + 1
        weeks = int(30*random.random()) + 1
        squat = random.normalvariate(175,10)
        bench = random.normalvariate(175,10)
        clean = random.normalvariate(175,10)
        dash = random.normalvariate(5,0.2)
        exercise = int(2*random.random()) + 1
        

        concussion = max(0,round(random.normalvariate(1,3)))
        bone = max(0,round(random.normalvariate(1,3)))
        ligament = max(0,round(random.normalvariate(1,3)))
        muscle = max(0,round(random.normalvariate(1,3)))
        joint = max(0,round(random.normalvariate(1,3)))
        tendonitis = max(0,round(random.normalvariate(1,3)))
        sprain = max(0,round(random.normalvariate(3,3)))
        meniscus = max(0,round(random.normalvariate(1,3)))
        other = max(0,round(random.normalvariate(1,3)))
        total = max(0,round(random.normalvariate(9,5)))

        total_new = max(0,random.normalvariate(1 + 3*joint + total - lift/7 + squat/200 - bench/200 - dash/4 - clean/120 + years/3 + exerciseint, 2))

        writer.writerow({'id':i, 'age':age, 'height':height, 'weight':weight, 'qb':1, 'te':0, 'ot':0, 'og':0, 'c':0, 'rb':0, 'wr':0, 'de':0, 'dt':0, 'lb':0, 'cb':0, 's':0, 'kp':0, 'ls':0, 'years':years, 'games':games, 'hours':lift, 'weeks':weeks, 'squat':squat, 'bench':bench, 'clean':clean, 'dash':dash, 'exercise':exercise, 'concussion_old':concussion, 'bone_old':bone, 'ligament_old':ligament, 'muscle_old':muscle, 'joint_old':joint, 'tendonitis_old':tendonitis, 'sprain_old':sprain, 'meniscus_old':meniscus, 'concussion_new':0, 'bone_new':0, 'ligament_new':0, 'muscle_new':0, 'joint_new':0, 'tendonitis_new':0, 'sprain_new':0, 'meniscus_new':0, 'total_new':total_new})
        
