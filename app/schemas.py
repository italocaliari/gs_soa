"""Contratos JSON (Pydantic). Os nomes em camelCase seguem o contrato do README."""
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field, model_validator
from pydantic.alias_generators import to_camel


class CamelModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True, from_attributes=True)


class PrevisaoEntrada(CamelModel):
    """Observações de ontem usadas para prever se o dia é perigoso."""

    data: date = Field(description="Dia que se quer prever (AAAA-MM-DD).")
    temperatura_max_ontem: float = Field(ge=-10, le=50, description="Temperatura máxima de ontem, em °C.")
    temperatura_min_ontem: float = Field(ge=-10, le=50, description="Temperatura mínima de ontem, em °C.")
    umidade_media_ontem: float = Field(ge=0, le=100, description="Umidade relativa média de ontem, em %.")
    vento_medio_ontem: float = Field(ge=0, le=60, description="Velocidade média do vento de ontem, em m/s.")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "data": "2026-11-20",
                "temperaturaMaxOntem": 31.2,
                "temperaturaMinOntem": 19.8,
                "umidadeMediaOntem": 55.0,
                "ventoMedioOntem": 2.1,
            }
        }
    )

    @model_validator(mode="after")
    def minima_nao_pode_superar_maxima(self) -> "PrevisaoEntrada":
        if self.temperatura_min_ontem > self.temperatura_max_ontem:
            raise ValueError("temperaturaMinOntem não pode ser maior que temperaturaMaxOntem")
        return self


class PrevisaoSaida(CamelModel):
    """Resposta do POST /previsoes (contrato com a API principal)."""

    id: int
    data: date
    probabilidade: float = Field(ge=0, le=1, description="Probabilidade de o dia ser perigoso.")
    perigoso: bool
    versao_modelo: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {"id": 42, "data": "2026-11-20", "probabilidade": 0.82, "perigoso": True, "versaoModelo": "1.0"}
        }
    )


class PrevisaoDetalhe(PrevisaoSaida):
    """Previsão com os dados de entrada e o momento do registro (consultas GET)."""

    temperatura_max_ontem: float
    temperatura_min_ontem: float
    umidade_media_ontem: float
    vento_medio_ontem: float
    criado_em: datetime


class ErroResposta(BaseModel):
    erro: str
    detalhe: str
