from django.db import models


class Train(models.Model):
    train_id = models.AutoField(primary_key=True)
    train_name = models.TextField()
    train_type = models.TextField()
    
    def __str__(self) -> str:
        return self.train_name

class Station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.TextField()

    def __str__(self) -> str:
        return self.station_name


class Route(models.Model):
    route_id = models.AutoField(primary_key=True)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    arrival_date = models.DateTimeField()
    break_period = models.TimeField()
    departure_date = models.DateTimeField()

    def __str__(self) -> str:
        return f'Поезд {self.train}\nСтанция {self.station}\nДата прибытия {self.arrival_date}\n'


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    n_carriage = models.DecimalField(max_digits=3, decimal_places=0)
    n_seat = models.DecimalField(max_digits=5, decimal_places=0)
    seat_type = models.TextField()
    seat_availibility = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f'Маршрут\n{self.route}Вагон {self.n_carriage}, Место {self.n_seat}, \
            Тип места {self.seat_type}, {self.seat_availibility}\nЦена {self.price}\n'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    fio = models.TextField()
    passport = models.TextField()
    country = models.TextField()
    city = models.TextField()
    phone_number = models.TextField()
    email = models.TextField(blank=True, null=True)
    post_index = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)

    def __str__(self) -> str:
        return self.fio


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
    summary = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.customer}, {self.payment_date}, {self.summary}'


# Create your models here.
