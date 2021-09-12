def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    def step2_umbrella():
        print('Теперь утке не страшен дождь')
    def step2_no_umbrella():
        print('Тогда ей придется пить до тех пор, пока не закончится дождь')
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()