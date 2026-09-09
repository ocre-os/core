import os
import subprocess
import sys
from pathlib import Path

import pytest
from pydantic import ValidationError

from app.modules.organizations.schemas import OrganizacionCreate


def test_migration_url_accepts_percent_encoded_password() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "alembic", "upgrade", "head", "--sql"],
        cwd=Path(__file__).resolve().parents[1],
        env={**os.environ, "DATABASE_URL": "postgresql+psycopg://test:local%40test@db/test"},
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "CREATE TABLE organizacion" in result.stdout


@pytest.mark.parametrize(
    ("field", "max_length"),
    [
        ("nombre_comercial", 200),
        ("nombre_legal", 250),
        ("telefono_principal", 40),
        ("email_general", 320),
        ("sitio_web", 500),
        ("estado_relacion", 60),
    ],
)
def test_organization_rejects_oversized_fields(field: str, max_length: int) -> None:
    with pytest.raises(ValidationError) as error:
        OrganizacionCreate.model_validate(
            {"nombre_comercial": "Prueba", field: "x" * (max_length + 1)}
        )
    assert error.value.errors()[0]["loc"] == (field,)
