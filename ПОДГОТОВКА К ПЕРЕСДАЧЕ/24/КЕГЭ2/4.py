f = open('4.txt').readline()
BOSS = f.count('BOSS')
JBOSS = f.count('JBOSS')
JBOSSJ = f.count('JBOSSJ')
BOSSJ = f.count('BOSSJ')

print(BOSS + JBOSSJ - JBOSS - BOSSJ)