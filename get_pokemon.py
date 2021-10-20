from bs4 import BeautifulSoup
import requests
pokemon = 'absol'

class get_pokemon():
    def __init__(self,poke,numero_poke):
        raw_venusaur_html = requests.get(f'https://www.pokemonunite.gg/builds/{poke}')
        self.raw_sopa = BeautifulSoup(raw_venusaur_html.text, 'lxml')
        self.numero_poke = numero_poke

        self.setup_pokemon()
        self.get_name()
        self.get_role_lane()
        self.get_items()
        self.get_skills()
        self.get_battle_item()
        self.get_info()
        self.get_author()
        self.get_result()


    def setup_pokemon(self):

        self.poke_build = ''
        self.poke_role = ''
        self.poke_lane = ''
        self.item_1 = ''
        self.item_2 = ''
        self.item_3 = ''
        self.skill_1 = ''
        self.skill_2 = ''
        self.skill_3 = ''
        self.battle_item = ''
        self.info = ''
        self.author = ''
        self.link = ''


    def get_name(self):
        name_txt = self.raw_sopa.find_all('h3')
        build = (str(name_txt).replace('<h3>', '').replace('</h3>', '')).replace('[', '').replace(']', '').split(',')

        self.poke_build = build[self.numero_poke]
        return self.poke_build

    def get_role_lane(self):
        name_text = self.raw_sopa.find_all('section',class_="pokemon-card-header")
        build = str(name_text)
        begin = build.find('</h3><div>') + len('</h3><div>')
        end = build.find('</div></section>')
        role = (build[begin:end].split('|'))
        self.poke_role = role[1]
        self.poke_lane = role[2]

    def get_items(self):

        name_text = self.raw_sopa.find_all('div', class_ ="pokemon-card-equipped-items")
        build = str(name_text).split('<img alt="')

        item_1 = (build[self.numero_poke +1][0:build[self.numero_poke +1].index('"')])
        item_2 = (build[self.numero_poke + 2][0:build[self.numero_poke + 2].index('"')])
        item_3 = (build[self.numero_poke + 3][0:build[self.numero_poke + 3].index('"')])

        self.item_1 = item_1
        self.item_2 = item_2
        self.item_3 = item_3
        return['self.item_1','self.item_2','self.item_3']

    def get_skills(self):
        name_text = self.raw_sopa.find_all('div', class_="pokemon-card-equipped-skills")
        build = str(name_text).split('<img alt="')

        skill_1 = (build[self.numero_poke + 1][0:build[self.numero_poke + 1].index('"')])
        skill_2 = (build[self.numero_poke + 2][0:build[self.numero_poke + 2].index('"')])
        skill_3 = (build[self.numero_poke + 3][0:build[self.numero_poke + 3].index('"')])

        self.skill_1 = skill_1
        self.skill_2 = skill_2
        self.skill_3 = skill_3

    def get_battle_item(self):
        name_text = self.raw_sopa.find_all('div', class_="pokemon-card-equipped-battle-item")
        build = str(name_text).split('<img alt="')


        battle_item = (build[self.numero_poke + 1][0:build[self.numero_poke + 1].index('"')])


        self.battle_item = battle_item

    def get_info(self):
        name_text = self.raw_sopa.find_all('section', class_="pokemon-card-synopsis")
        build = str(name_text[self.numero_poke])
        begin = build.find('[<section class="pokemon-card-synopsis"><div>') + len('[<section class="pokemon-card-synopsis"><div>')
        end = build.find('</div></section>')

        self.info = build[begin:end]
        return str(self.info)
    
    def get_link(self):
        name_text = self.raw_sopa.find_all('a', href=True)
        build=[]
        for a in name_text:
            if a.text:
                build.append(a['href'])
        self.link= f'https://www.pokemonunite.gg/{build[self.numero_poke + 25]}'
        

        return self.link

    def get_author(self):
        name_text = self.raw_sopa.find_all('section', class_="pokemon-card-author")
        build = str(name_text)
        build_cut =''.join(''.join((build).split('<section class="pokemon-card-author">')).split('</div><img alt="Pokemon Unite.gg')).split('Logo" height="14.3" src="/res/img/pokemonunitegg_logo.svg" width="70"/></section>')
        self.author = str(build_cut[self.numero_poke]).replace('<div>','').replace(', ','').replace('[','')
        
      



    def get_result(self):
        return(f'Build name: {self.poke_build}\n'
              f'Role: {self.poke_role}\n'
              f'Lane: {self.poke_lane}\n'
              f'Items: {self.item_1},{self.item_2},{self.item_3}\n'
              f'Skills: {self.skill_1},{self.skill_2},{self.skill_3}\n'
              f'Battle Item: {self.battle_item}\n\n'
              f'{self.info}\n\n'
              f'Author: {self.author}')
