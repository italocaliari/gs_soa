"""Entidade Previsao: o registro persistido de cada previsão de calor perigoso."""
from datetime import date, datetime, timezone

from sqlalchemy import Boolean, CheckConstraint, Date, DateTime, Float, Index, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


def _agora() -> datetime:
    return datetime.now(timezone.utc)


class Previsao(Base):
    __tablename__ = "previsoes"
    __table_args__ = (
        CheckConstraint("probabilidade >= 0 AND probabilidade <= 1", name="ck_previsoes_probabilidade"),
        Index("ix_previsoes_data", "data"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    data: Mapped[date] = mapped_column(Date, nullable=False)
    temperatura_max_ontem: Mapped[float] = mapped_column(Float, nullable=False)
    temperatura_min_ontem: Mapped[float] = mapped_column(Float, nullable=False)
    umidade_media_ontem: Mapped[float] = mapped_column(Float, nullable=False)
    vento_medio_ontem: Mapped[float] = mapped_column(Float, nullable=False)
    probabilidade: Mapped[float] = mapped_column(Float, nullable=False)
    perigoso: Mapped[bool] = mapped_column(Boolean, nullable=False)
    versao_modelo: Mapped[str] = mapped_column(String(32), nullable=False)
    criado_em: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=_agora)

    @staticmethod
    def e_perigosa(probabilidade: float, limiar: float) -> bool:
        """Regra de negócio: a previsão é de dia perigoso quando a probabilidade atinge o limiar."""
        return probabilidade >= limiar
