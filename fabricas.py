#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from productos import *


class Pool():

    _instance = None
    _fabrica = None
    

    @classmethod
    def get_instance(cls): # Constructor alternativo que retorna una nueva instancia
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def get_fabrica(self, parametro):
        self.fabricas = [FabricaElfos(), FabricaMagos(), FabricaEnanos(), FabricaBarbaros()]
        if self._fabrica == None:
            self._fabrica = self.fabricas[parametro]
        return self._fabrica

    

class Fabrica(ABC):
    @abstractmethod
    def crear_arma(self):
        pass
    @abstractmethod
    def crear_escudo(self):
        pass
    @abstractmethod
    def crear_montura(self):
        pass

class FabricaEnanos(Fabrica):
    def crear_arma(self):
        return ArmaEnano()

    def crear_escudo(self):
        return EscudoEnano()

    def crear_montura(self):
        return MonturaEnano()

class FabricaBarbaros(Fabrica):
    def crear_arma(self):
        return ArmaBarbaro()

    def crear_escudo(self):
        return EscudoBarbaro()

    def crear_montura(self):
        return MonturaBarbaro()

class FabricaElfos(Fabrica):
    def crear_arma(self):
        return ArmaElfo()

    def crear_escudo(self):
        return EscudoElfo()

    def crear_montura(self):
        return MonturaElfo()

class FabricaMagos(Fabrica):
    def crear_arma(self):
        return ArmaMago()

    def crear_escudo(self):
        return EscudoMago()

    def crear_montura(self):
        return MonturaMago()
