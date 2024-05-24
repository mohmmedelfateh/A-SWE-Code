#Open-Closed Principles
from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def get_discount(self):
        raise NotImplementedError("Subclasses must implement get_discount method")


class NormalDiscount(Discount):
    def get_discount(self):
        return 20


class VIPDiscount(Discount):
    def get_discount(self):
        return 50


class SuperVIPDiscount(Discount):
    def get_discount(self):
        return 90
