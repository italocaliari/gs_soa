"""Configuração do serviço. Tudo vem de variáveis de ambiente (ou de um arquivo .env)."""
import os
from dataclasses import dataclass

try:  # python-dotenv é opcional: sem ele, só as variáveis de ambiente valem
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # pragma: no cover
    pass


@dataclass(frozen=True)
class Settings:
    database_url: str
    modelo_path: str | None
    modelo_versao: str
    limiar_perigo: float


def get_settings() -> Settings:
    return Settings(
        database_url=os.getenv("REFRESCA_PREVISAO_DB_URL", "sqlite:///./refresca_previsao.db"),
        modelo_path=os.getenv("REFRESCA_MODELO_PATH") or None,
        modelo_versao=os.getenv("REFRESCA_MODELO_VERSAO", "1.0"),
        limiar_perigo=float(os.getenv("REFRESCA_LIMIAR_PERIGO", "0.5")),
    )
