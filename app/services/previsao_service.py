"""Casos de uso: orquestra preditor, regra de negócio e repositório."""
import logging
from datetime import date

from app.domain.previsao import Previsao
from app.errors import PrevisaoNaoEncontrada
from app.ml.preditor import Observacao, Preditor
from app.repositories.previsao_repository import PrevisaoRepository
from app.schemas import PrevisaoEntrada

log = logging.getLogger("refresca.previsao")


class PrevisaoService:
    def __init__(self, repositorio: PrevisaoRepository, preditor: Preditor, limiar_perigo: float):
        self._repo = repositorio
        self._preditor = preditor
        self._limiar = limiar_perigo

    def prever(self, entrada: PrevisaoEntrada) -> Previsao:
        observacao = Observacao(
            temperatura_max_ontem=entrada.temperatura_max_ontem,
            temperatura_min_ontem=entrada.temperatura_min_ontem,
            umidade_media_ontem=entrada.umidade_media_ontem,
            vento_medio_ontem=entrada.vento_medio_ontem,
        )
        probabilidade = min(1.0, max(0.0, round(self._preditor.probabilidade(observacao), 4)))
        previsao = Previsao(
            data=entrada.data,
            temperatura_max_ontem=entrada.temperatura_max_ontem,
            temperatura_min_ontem=entrada.temperatura_min_ontem,
            umidade_media_ontem=entrada.umidade_media_ontem,
            vento_medio_ontem=entrada.vento_medio_ontem,
            probabilidade=probabilidade,
            perigoso=Previsao.e_perigosa(probabilidade, self._limiar),
            versao_modelo=self._preditor.versao,
        )
        salva = self._repo.adicionar(previsao)
        log.info("previsao id=%s data=%s p=%.4f perigoso=%s modelo=%s",
                 salva.id, salva.data, salva.probabilidade, salva.perigoso, salva.versao_modelo)
        return salva

    def obter(self, previsao_id: int) -> Previsao:
        previsao = self._repo.obter(previsao_id)
        if previsao is None:
            raise PrevisaoNaoEncontrada(f"Previsão {previsao_id} não encontrada")
        return previsao

    def listar(self, data: date | None, limite: int, deslocamento: int) -> list[Previsao]:
        return self._repo.listar(data, limite, deslocamento)

    def da_data(self, data: date) -> Previsao:
        previsao = self._repo.ultima_da_data(data)
        if previsao is None:
            raise PrevisaoNaoEncontrada(f"Nenhuma previsão registrada para {data.isoformat()}")
        return previsao
