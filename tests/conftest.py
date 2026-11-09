import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.deps import get_preditor
from app.main import create_app
from app.ml.preditor import HeuristicaCalor

ENTRADA = {
    "data": "2026-11-20",
    "temperaturaMaxOntem": 31.2,
    "temperaturaMinOntem": 19.8,
    "umidadeMediaOntem": 55.0,
    "ventoMedioOntem": 2.1,
}


class PreditorFixo:
    versao = "teste-1.0"

    def __init__(self, valor: float):
        self.valor = valor

    def probabilidade(self, observacao) -> float:
        return self.valor


@pytest.fixture
def engine():
    motor = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(motor)
    yield motor
    motor.dispose()


def _cliente(motor, preditor):
    sessao = sessionmaker(bind=motor, autoflush=False, expire_on_commit=False)

    def db():
        s = sessao()
        try:
            yield s
        finally:
            s.close()

    app = create_app()
    app.dependency_overrides[get_db] = db
    app.dependency_overrides[get_preditor] = lambda: preditor
    return TestClient(app)


@pytest.fixture
def preditor_fixo():
    return PreditorFixo(0.82)


@pytest.fixture
def client(engine, preditor_fixo):
    return _cliente(engine, preditor_fixo)


@pytest.fixture
def client_heuristica(engine):
    return _cliente(engine, HeuristicaCalor())
