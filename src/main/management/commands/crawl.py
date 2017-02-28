import requests
from bs4 import BeautifulSoup
from django.core.management import BaseCommand

from allies.models import Ally
from civilians.models import Civilian
from monsters.models import Monster
from series.models import Series
from villains.models import Villain

BASE_URL = 'http://powerrangers.wikia.com'

TYPES = [
    'allies',
    'civilians',
    'monsters',
    'villains',
]

SERIES = {
    '1': {
        'overview': BASE_URL + '/wiki/Mighty_Morphin_Power_Rangers_(Season_1)',
        'monsters': BASE_URL + '/wiki/Mighty_Morphin_1_Monsters',
    },
    '2': {
        'overview': BASE_URL + '/wiki/Mighty_Morphin_Power_Rangers_(Season_2)',
        'monsters': BASE_URL + '/wiki/Mighty_Morphin_2_Monsters',
    },
    '3': {
        'overview': BASE_URL + '/wiki/Mighty_Morphin_Power_Rangers_(Season_3)',
        'monsters': BASE_URL + '/wiki/Mighty_Morphin_3_Monsters',
    },
}

MONSTERS_OVERRIDES = {
    'Bones': BASE_URL + '/wiki/Bones_(MMPR)'
}


class Command(BaseCommand):
    help = 'Crawls a website for allies, civilians, monsters and villains'

    def add_arguments(self, parser):
        parser.add_argument(
            '--type',
            action='store',
            dest='type',
            default='',
            help='Type'
        )
        parser.add_argument(
            '--series',
            action='store',
            dest='series',
            default='',
            help='Series'
        )

    def handle(self, **options):

        if options.get('type') not in TYPES:
            raise Exception('Unknown type {0}'.format(options.get('type')))

        if options.get('series') not in SERIES:
            raise Exception('Unknown series {0}'.format(options.get('series')))

        if options.get('type') == 'allies':
            self._allies(options.get('series'))

        elif options.get('type') == 'civilians':
            self._civilians(options.get('series'))

        elif options.get('type') == 'villains':
            self._villains(options.get('series'))

        elif options.get('type') == 'monsters':
            self._monsters(options.get('series'))

    def _allies(self, series):
        html = requests.get(SERIES[series]['overview'])
        soup = BeautifulSoup(html.content, 'html.parser')
        allies = soup.find('span', id='Allies').parent.findNext('ul').find_all('li')

        for ally in allies:
            ally_html = requests.get('{0}{1}'.format(BASE_URL, ally.find('a').attrs.get('href')))
            ally_soup = BeautifulSoup(ally_html.content, 'html.parser')

            try:
                info = self._info(ally_soup.find('div', id='mw-content-text'))

                try:
                    ally = Ally.objects.get(name=info['name'])
                except Ally.DoesNotExist:
                    ally = Ally(name=info['name'])

                ally.description = info['description']
                ally.save()

                try:
                    series_obj = Series.objects.filter(number=series).order_by('-parent')[0]
                    if not ally.series.filter(series=series_obj).count():
                        ally.series.add(series_obj)
                except IndexError:
                    pass

                    # image_name = urlparse(info['image'])[2].replace('/revision/latest', '').split('/')[-1]

                    # if ally.images.count():
                    #     for image in ally.images.all():
                    #         if image.image.name.split('/')[-1] != image_name:
                    #             image = AllyImage(ally=ally)
                    #             image.image.save(image_name, ContentFile(requests.get(info['image']).content))
                    # else:
                    #     image = AllyImage(ally=ally)
                    #     image.image.save(image_name, ContentFile(requests.get(info['image']).content))
            except AttributeError:
                pass

    def _civilians(self, series):
        html = requests.get(SERIES[series]['overview'])
        soup = BeautifulSoup(html.content, 'html.parser')
        civilians = soup.find('span', id='Civilians').parent.findNext('ul').find_all('li')

        for civilian in civilians:
            civilian_html = requests.get('{0}{1}'.format(BASE_URL, civilian.find('a').attrs.get('href')))
            civilian_soup = BeautifulSoup(civilian_html.content, 'html.parser')

            try:
                info = self._info(civilian_soup.find('div', id='mw-content-text'))

                try:
                    civilian = Civilian.objects.get(name=info['name'])
                except Civilian.DoesNotExist:
                    civilian = Civilian(name=info['name'])

                civilian.description = info['description']
                civilian.save()

                try:
                    series_obj = Series.objects.filter(number=series).order_by('-parent')[0]
                    if not civilian.series.filter(series=series_obj).count():
                        civilian.series.add(series_obj)
                except IndexError:
                    pass

                    # image_name = urlparse(info['image'])[2].replace('/revision/latest', '').split('/')[-1]

                    # if civilian.images.count():
                    #     for image in civilian.images.all():
                    #         if image.image.name.split('/')[-1] != image_name:
                    #             image = CivilianImage(civilian=civilian)
                    #             image.image.save(image_name, ContentFile(requests.get(info['image']).content))
                    # else:
                    #     image = CivilianImage(civilian=civilian)
                    #     image.image.save(image_name, ContentFile(requests.get(info['image']).content))
            except AttributeError:
                pass

    def _monsters(self, series):
        html = requests.get(SERIES[series]['monsters'])
        soup = BeautifulSoup(html.content, 'html.parser')
        monsters = soup.find('div', id='mw-content-text').find('ul').find_all('li')

        for monster in monsters:
            monster_name = monster.find('a').text.strip()

            if monster_name in MONSTERS_OVERRIDES:
                monster_url = MONSTERS_OVERRIDES[monster_name]
            else:
                monster_url = '{0}{1}'.format(BASE_URL, monster.find('a').attrs.get('href'))

            monster_html = requests.get(monster_url)
            monster_soup = BeautifulSoup(monster_html.content, 'html.parser')

            try:
                monster = Monster.objects.get(name=monster_name)
            except Monster.DoesNotExist:
                monster = Monster(name=monster_name)

            monster.description = monster_soup.find('div', id='mw-content-text').find('p').text.strip()
            monster.save()

    def _villains(self, series):
        html = requests.get(SERIES[series]['overview'])
        soup = BeautifulSoup(html.content, 'html.parser')
        villains = soup.find('span', id='Villains').parent.findNext('ul').find('ul').find_all('li')

        for villain in villains:
            villain_html = requests.get('{0}{1}'.format(BASE_URL, villain.find('a').attrs.get('href')))
            villain_soup = BeautifulSoup(villain_html.content, 'html.parser')

            try:
                info = self._info(villain_soup.find('div', id='mw-content-text'))

                try:
                    villain = Villain.objects.get(name=info['name'])
                except Villain.DoesNotExist:
                    villain = Villain(name=info['name'])

                villain.description = info['description']
                villain.gender = info['gender'].lower()
                villain.type = info['type'].lower()
                villain.homeworld = info['homeworld']
                villain.save()

                try:
                    series_obj = Series.objects.filter(number=series).order_by('-parent')[0]
                    if not villain.series.filter(series=series_obj).count():
                        villain.series.add(series_obj)
                except IndexError:
                    pass

                    # image_name = urlparse(info['image'])[2].replace('/revision/latest', '').split('/')[-1]

                    # if villain.images.count():
                    #     for image in villain.images.all():
                    #         if image.image.name.split('/')[-1] != image_name:
                    #             image = VillainImage(villain=villain)
                    #             image.image.save(image_name, ContentFile(requests.get(info['image']).content))
                    # else:
                    #     image = VillainImage(villain=villain)
                    #     image.image.save(image_name, ContentFile(requests.get(info['image']).content))
            except AttributeError:
                pass

    def _info(self, soup):
        try:
            description = soup.find('div', {'class': 'quote'}).findNext('p').text
        except AttributeError:
            description = None

        infobox = soup.find('table', {'class': 'infobox'})
        data_list = [x.find_all('td')[-1].text.strip() for x in infobox.find_all('tr')]
        return {
            'name': data_list[0] if data_list[0] else data_list[2],
            'description': description,
            'gender': data_list[3] if description else None,
            'type': data_list[4] if description else None,
            'homeworld': data_list[6] if description else None,
            'image': infobox.find('img').parent.attrs.get('href')
        }
