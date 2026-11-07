"""Preditores de dia de calor perigoso.

Contrato: receber as observações de ontem e devolver a probabilidade (0 a 1) de HOJE/AMANHÃ
ser um dia perigoso. Há dois preditores:

* ModeloSklearn: carrega o modelo treinado pelo responsável de ML (arquivo .joblib).
* HeuristicaCalor: linha de base sem treino, usada enquanto o modelo não é entregue.
"""
import math
import os
from dataclasses import dataclass
from typing import Protocol

from app.domain.calor import LIMITE_PERIGO_C, indice_calor_celsius
from app.errors import ModeloIndisponivel

# Ordem das colunas que o modelo de ML deve esperar. Se o notebook usar outra, ajustar AQUI.
FEATURES = ("temperatura_max_ontem", "temperatura_min_ontem", "umidade_media_ontem", "vento_medio_ontem")


@dataclass(frozen=True)
class Observacao:
    temperatura_max_ontem: float
    temperatura_min_ontem: float
    umidade_media_ontem: float
    vento_medio_ontem: float

    def como_linha(self) -> list[float]:
        return [getattr(self, nome) for nome in FEATURES]


class Preditor(Protocol):
    versao: str

    def probabilidade(self, observacao: Observacao) -> float: ...


class HeuristicaCalor:
    """Sem treino: estima o índice de calor de ontem (máxima + umidade) e o compara com o limite
    de perigo da NOAA (32 °C) por uma curva sigmoide. Serve de baseline, não de modelo final."""

    versao = "heuristica-1.0"
    ESCALA = 1.5  # °C de índice de calor que separam ~73% de ~27% de probabilidade

    def probabilidade(self, observacao: Observacao) -> float:
        ic = indice_calor_celsius(observacao.temperatura_max_ontem, observacao.umidade_media_ontem)
        return 1.0 / (1.0 + math.exp(-(ic - LIMITE_PERIGO_C) / self.ESCALA))


class ModeloSklearn:
    """Envolve um classificador scikit-learn salvo com joblib (precisa de predict_proba)."""

    def __init__(self, caminho: str, versao: str):
        if not os.path.isfile(caminho):
            raise ModeloIndisponivel(f"Arquivo do modelo não encontrado: {caminho}")
        try:
            import joblib

            self._modelo = joblib.load(caminho)
            classes = list(self._modelo.classes_)
            self._indice_positivo = classes.index(1) if 1 in classes else len(classes) - 1
        except Exception as erro:  # arquivo corrompido, lib ausente, sem predict_proba...
            raise ModeloIndisponivel(f"Não foi possível carregar o modelo: {erro}") from erro
        self.versao = versao

    def probabilidade(self, observacao: Observacao) -> float:
        return float(self._modelo.predict_proba([observacao.como_linha()])[0][self._indice_positivo])


def criar_preditor(modelo_path: str | None, modelo_versao: str) -> Preditor:
    if modelo_path:
        return ModeloSklearn(modelo_path, modelo_versao)
    return HeuristicaCalor()
