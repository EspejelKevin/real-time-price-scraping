from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from src.domain import Settings


class APSchedulerAdapter:
    def __init__(self, container, settings: Settings) -> None:
        self.container = container
        self.settings = settings
        self.scheduler = AsyncIOScheduler()

    async def _job_wrapper(self) -> None:
        await self.container.scraping_orchestrator().execute()

    def start(self) -> None:
        self.scheduler.add_job(
            self._job_wrapper,
            trigger=IntervalTrigger(minutes=self.settings.INTERVAL_TIME),
            id=self.settings.JOB_ID,
            name=self.settings.JOB_NAME,
            replace_existing=True
        )
        self.scheduler.start()
    
    def stop(self) -> None:
        self.scheduler.shutdown()
