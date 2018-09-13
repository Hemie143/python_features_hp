import yaml
from python_features_hp.magic_universe import CastleKilmereMember, Pupil

if __name__ == '__main__':
    with open('config.yaml', 'r') as c:
        config = yaml.load(c)
        bromley = CastleKilmereMember(**config['bromley'])
        print('bromley: ', bromley)

        cleon = Pupil(**config['cleon'])
        print('cleon: ', cleon)