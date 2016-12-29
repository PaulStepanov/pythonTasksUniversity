from datetime import timedelta, datetime


class Resource:
    __consuming_resources_size = 0

    def __init__(self, res_type, capacity):
        self.res_type = res_type
        self.capacity = capacity

    def start_consume(self, value):
        """
        Начинается потреблемение ресурса возвращает кортеж:первый элемен 1 или 0 хватилоли ресурсов,
        второй количество потребляемых ресурсов
        """
        if value > self.capacity:
            self.__consuming_resources_size = self.capacity
            self.capacity = 0
            return (0,self.__consuming_resources_size)
        self.__consuming_resources_size += value
        self.capacity -= value
        return (1,value)

    def release_resources(self, value):
        """
        Высвобождает потребляемый ресурс,ничего не возращает
        """
        self.capacity += value
        self.__consuming_resources_size -= value


class Provider:
    name = ''
    category = ''
    resources = []

    def __init__(self, name, category, resources):
        """"""
        self.name = name
        self.category = category
        self.resources = resources

    def getResources(self, resource, amount, time=None):
        """Начинается потребление ресурса в заданом количестве,время передается для логированиея ошибок"""
        resur = None
        for res in self.resources:
            if res.res_type == resource:
                resur = res
        flag = resur.start_consume(amount)
        if flag:
            return (1,flag[1])
        else:
            print(self.name, "couldn't provide enough res at", time)
            return (0,flag[1])

    def releaseResources(self, resource, amount):
        """Высвобождается ресурс в указаном количестве"""
        resur = None
        for res in self.resources:
            if res.res_type == resource:
                resur = res
        resur.release_resources(amount)


class Consumer:
    consuming_resources = []
    consuming_resources_tuple=[]
    consuming_size = 0

    def __init__(self, name, category, consuming_resources):
        self.consuming_category = category
        self.name = name
        self.consuming_resources = consuming_resources

    def consume(self, resource, amount, provider, time):
        """Начинает потреблять ресурс в указаном количестве у указанного провайдера,время передается для логирования ошибок """
        cons_amount=provider.getResources(resource, amount, time=time)[1]
        if cons_amount<amount:
            print("not enought res consumer:",self.name,"time:",time,"we have",cons_amount)
        self.consuming_size+=cons_amount
        self.consuming_resources_tuple.append((resource, cons_amount,provider))
    def stopConsume(self):
        """Прекращает потребление всех ресурсов """
        for res in self.consuming_resources_tuple:
            res[2].releaseResources(res[0],res[1])

class Universal(Provider, Consumer):
    pass


class Event:
    date_time = None
    duration = None
    providers = []
    consumers = []

    def __init__(self, date_time, duration, providers, consumers):
        self.date_time = date_time
        self.duration = duration
        self.providers = providers
        self.consumers = consumers

    def start(self, function):
        function(self)

    def stopAllConsume(self):
        for consumer in self.consumers:
            consumer.stopConsume()

# make
# providers
John = Provider('John', 'Water', [Resource('water', 170), Resource('fizzy water', 70)])
Bill = Provider('Bill', 'Ammo', [Resource('5x56.5', 9000), Resource('7x62x51', 1000)])
# consumers
Zoltan = Consumer('Zoltan', 'Water', [Resource('5x56.5', 1000), Resource('7x62x51', 700)])
Jack = Consumer('Jack', 'Ammo', [Resource('7x62x51', 900)])
Univ=Universal('Jack', 'Water', [Resource('water', 170), Resource('fizzy water', 70)],
               'Jack', 'Ammo', [Resource('7x62x51', 900)])
first_ev = Event(
    datetime(year=2016, month=12, day=12, hour=10, minute=2),
    timedelta(days=10, hours=12),
    # Providers
    [John, Bill],
    # Consumers
    [Zoltan,]
)
def first_func(event):
    event.consumers[0].consume('water',120,event.providers[0],event.date_time)
    event.consumers[0].consume('5x56.5',920,event.providers[1],event.date_time)
    event.stopAllConsume()
    event.consumers[0].consume('water',120,event.providers[0],event.date_time)
first_ev.start(first_func)



# print(John.getResources('water', 120, datetime(year=1997, month=12, day=12, hour=10, minute=2)))
# John.releaseResources('water', 120)
# print(John.getResources('water', 130, datetime(year=1997, month=12, day=12, hour=10, minute=2)))
#
# # first_ev.start()
# if 0:
#     print(datetime(year=1997, month=12, day=12, hour=10, minute=2) + timedelta(minutes=1, hours=12))
