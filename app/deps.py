"""Injeção de dependências do FastAPI (nos testes, tudo isto é substituído)."""
from functools import lru_cache

from fastapi import Depends
from sqlalchemy.orm import Session

from app.config import get_settings
from app.database import get_db
from app.ml.preditor import Preditor, criar_preditor
from app.repositories.previsao_repository import PrevisaoRepository
from app.services.previsao_service import PrevisaoService


@lru_cache
def get_preditor() -> Preditor:
    configuracao = get_settings()
    return criar_preditor(configuracao.modelo_path, configuracao.modelo_versao)


def get_service(db: Session = Depends(get_db), preditor: Preditor = Depends(get_preditor)) -> PrevisaoService:
    return PrevisaoService(PrevisaoRepository(db), preditor, get_settings().limiar_perigo)
