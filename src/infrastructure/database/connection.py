from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from contextlib import contextmanager
from typing import Generator


class DatabaseConnection:
    def __init__(self, db_url: str, echo: bool) -> None:
        self._engine = create_engine(db_url, echo=echo)
        self._session_factory = sessionmaker(
            bind=self._engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        session: Session = self._session_factory()

        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
