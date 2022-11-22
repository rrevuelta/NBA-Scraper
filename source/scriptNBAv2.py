# Librerias necesarias 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd

# Listas vacías con los datos que vamos a extraer
Season = []
Player = []
Pos = []
Age = []
Tm = []
G = []
GS = []
MP = []
FG = []
FGA = []
FGPer = []
TriP = []
TriPA = []
TriPer = []
TwoP = []
TwoPA = []
TwoPer = []
eFGPer = []
FT = []
FTA = []
FTPer = []
ORB = []
DRB = []
TRB = []
AST = []
STL = []
BLK = []
TOV = []
PF = []
PTS = []

# Iniciamos el webdriver 
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.basketball-reference.com/')

# La ruta del botón de aceptar cookies es dinámica, por lo que hemos puesto las 2 diferentes maneras que nos hemos encontrado
try:
    cookiesButton = driver.find_element(By.XPATH,'//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]')
    cookiesButton.click()
    time.sleep(0.5)
    
    cookiesButton2 = driver.find_element(By.XPATH,'//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]/span')
    cookiesButton2.click()
    
except:
    pass
    
# Hacemos click en diferentes partes de la web hasta llegar a la tabla con los datos que queremos
seasons_button = driver.find_element(By.XPATH,'//*[@id="header_leagues"]/a')
seasons_button.click()
time.sleep(0.5)

# Contamos el número de filas de la tabla con las temporadas
seasons_table = driver.find_element(By.XPATH,'//*[@id="stats"]/tbody')
season_rows = 0
for tr in seasons_table.find_elements(By.TAG_NAME,'tr'):
    season_rows+=1
print(season_rows)

for j in range(2,season_rows):
    
    season = driver.find_element(By.XPATH,'//*[@id="stats"]/tbody/tr['+str(j)+']/th/a')
    season.click()
    time.sleep(1.5)
    player_stats = driver.find_element(By.XPATH,'//*[@id="inner_nav"]/ul/li[6]/span')
    player_stats.click()
    time.sleep(1)
    statistics_button = driver.find_element(By.XPATH,'//*[@id="inner_nav"]/ul/li[6]/div/ul/li[1]/a')
    statistics_button.click()
    
    try:
        hide_partial_rows = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="per_game_stats_toggle_partial_table"]')))
        hide_partial_rows.click()
        time.sleep(0.5)
        
    except TimeoutException:
        pass
        

    # Contamos el número de filas de la tabla con datos de jugadores
    statistics_rows = 0
    statistics_table=driver.find_element(By.XPATH,'//*[@id="per_game_stats"]/tbody')
    for tr in statistics_table.find_elements(By.TAG_NAME,"tr"):
        statistics_rows+=1
        nba_season = driver.find_element(By.XPATH,'//*[@id="inner_nav"]/ul/li[1]/a/u').text
    
    for i in range(1,statistics_rows):
        
        try:
            nba_season = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="inner_nav"]/ul/li[1]/a/u'))).text
            players = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[1]/a'))).text
            position = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[2]'))).text
            age = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[3]'))).text
            team = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[4]/a'))).text
            games = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[5]'))).text
            games_started = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[6]'))).text
            minutes = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[7]'))).text
            tiros = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[8]'))).text
            tiros_intentados = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[9]'))).text
            porcentaje_tiros = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[10]'))).text
            triples = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[11]'))).text
            triples_intentados = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[12]'))).text
            porcentaje_triples = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[13]'))).text
            tiros_dos = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[14]'))).text
            tiros_dos_intentados = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[15]'))).text
            porcentaje_tiros_dos = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[16]'))).text
            porcentaje_tiro_efectivo = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[17]'))).text
            tiros_libres = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[18]'))).text
            tiros_libres_intentados = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[19]'))).text
            porcentaje_tiros_libres = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[20]'))).text
            rebotes_ofensivos = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[21]'))).text
            rebotes_defensivos = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[22]'))).text
            rebotes_totales = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[23]'))).text
            asistencias = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[24]'))).text
            robos = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[25]'))).text
            tapones = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[26]'))).text
            perdidas = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[27]'))).text
            faltas = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[28]'))).text
            puntos = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="per_game_stats"]/tbody/tr['+str(i)+']/td[29]'))).text
    
            # Añadimos los datos extraídos a las listas creadas anteriormente
            Season.append(nba_season)
            Player.append(players)
            Pos.append(position)
            Age.append(age)
            Tm.append(team)    
            G.append(games)
            GS.append(games_started)
            MP.append(minutes)
            FG.append(tiros)
            FGA.append(tiros_intentados)
            FGPer.append(porcentaje_tiros)
            TriP.append(triples)
            TriPA.append(triples_intentados)
            TriPer.append(porcentaje_triples)
            TwoP.append(tiros_dos)
            TwoPA.append(tiros_dos_intentados)
            TwoPer.append(porcentaje_tiros_dos)
            eFGPer.append(porcentaje_tiro_efectivo)
            FT.append(tiros_libres)
            FTA.append(tiros_libres_intentados)
            FTPer.append(porcentaje_tiros_libres)
            ORB.append(rebotes_ofensivos)
            DRB.append(rebotes_defensivos)
            TRB.append(rebotes_totales)
            AST.append(asistencias)
            STL.append(robos)
            BLK.append(tapones)
            TOV.append(perdidas)
            PF.append(faltas)
            PTS.append(puntos)
            
            
        except TimeoutException:
            pass    

        print('Season: ', nba_season,'Player: ', players, 'Position: ', position, 'Team: ', team, 'Games: ', games, 'Games started: ', games_started,
              'Minutes played: ', minutes, 'Tiros: ', tiros, 'Tiros intentados: ', tiros_intentados, '% tiros: ', porcentaje_tiros,
              'Triples: ',triples, 'Triples intentados: ', triples_intentados, '% Triples: ',porcentaje_triples,
              'Tiros de 2: ',tiros_dos, 'Tiros de 2 intentados: ',tiros_dos_intentados, '% Tiros de 2: ',porcentaje_tiros_dos,
              '% tiro efectivo: ',porcentaje_tiro_efectivo, 'Tiros libres: ',tiros_libres, 'Tiros libres intentados: ',tiros_libres_intentados,
              '% tiros libres: ',porcentaje_tiros_libres, 'Rebotes ofensivos: ',rebotes_ofensivos, 'Rebotes defensivos: ',rebotes_defensivos,
              'Rebotes totales: ', rebotes_totales, 'Asistencias: ',asistencias, 'Robos: ',robos, 'Tapones: ',tapones,
              'Pérdidas: ',perdidas, 'Faltas: ',faltas, 'Puntos: ',puntos)
        
    # Volvemos a la pantalla con todas las temporadas    
    seasons_button = driver.find_element(By.XPATH,'//*[@id="header_leagues"]/a')
    seasons_button.click()
        
          
driver.quit()

# Convertimos las listas en series y formamos un dataframe
sea = pd.Series(Season, name= 'NBA Season')
pl = pd.Series(Player, name= 'Player')
pos = pd.Series(Pos, name= 'Position')
age = pd.Series(Age, name= 'Age')
tm = pd.Series(Tm, name= 'Team')
g = pd.Series(G, name= 'Games')
gs = pd.Series(GS, name= 'Games Started')
mn = pd.Series(MP, name='Minutes')
fg = pd.Series(FG, name= 'Field Goals')
fga = pd.Series(FGA, name= 'Field Goals Attempt')
fgp = pd.Series(FGPer, name= 'Field Goals %')
tri = pd.Series(TriP, name= '3-Point Field Goals Per Game')
tri_at = pd.Series(TriPA, name= '3-Point Field Goal Attempts Per Game')
tri_per = pd.Series(TriPer, name= '3-Point Field Goal %')
two_fg = pd.Series(TwoP, name= '2-Point Field Goals Per Game')
two_fga = pd.Series(TwoPA, name= '2-Point Field Goal Attempts Per Game')
two_per = pd.Series(TwoPer, name= '2-Point Field Goal %')
efg = pd.Series(eFGPer, name= 'Effective Field Goal %')
ft = pd.Series(FT, name= 'Free Throws Per Game')
fta = pd.Series(FTA, name= 'Free Throw Attempts Per Game')
fta_per = pd.Series(FTPer, name= 'Free Throw %')
ofr = pd.Series(ORB, name= 'Offensive Rebounds Per Game')
dfr = pd.Series(DRB, name= 'Defensive Rebounds Per Game')
tr = pd.Series(TRB, name= 'Total Rebounds Per Game')
ass_pg = pd.Series(AST, name= 'Assists Per Game')
stl = pd.Series(STL, name= 'Steals Per Game')
blk = pd.Series(BLK, name= 'Blocks Per Game')
tv = pd.Series(TOV, name= 'Turnovers Per Game')
pf = pd.Series(PF, name= 'Personal Fouls Per Game')
pts = pd.Series(PF, name= 'Points Per Game')


df = pd.concat([sea, pl, pos, age, tm, g, gs, mn, fg, fga, fgp, tri, tri_at, tri_per, two_fg, two_fga, 
                two_per, two_fg, two_fga, two_per, efg, ft, fta, fta_per, ofr, dfr, tr, ass_pg, stl, 
                blk, tv, pf, pts], axis=1)

print(df)
df.to_csv('PEC1_dataset.csv', index=False, header=True)
    
    
