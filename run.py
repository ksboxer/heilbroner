import yaml
import os, sys

sys.path.append('classes/')

from person import *

def create_people(num_of_people, configs):
    people = []
    for i in range(0, num_of_people):
        person = Person(configs)
        people.append(person)
    return(people)


def run(configs_file):

    # read in configs file

    with open(configs_file) as file:
        configs = yaml.load(file)

    # generate number of people
    num_of_people = configs['num_of_people']

    print('creating '+ str(num_of_people)+ ' people')
    people = create_people(num_of_people, configs)

configs_file = 'configs.yaml'

run(configs_file)
