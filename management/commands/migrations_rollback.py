from django.core.management.base import BaseCommand
from django.db.models import Model
from tivol.Assertions.assertions import NotEntryPointClass
from tivol.base_classes.entry_point import EntryPoint
from tivol.management.helpers import SwagHelpers
from tivol.models import ContentMigrationStatus
from django.apps import apps


class Command(BaseCommand, SwagHelpers):
    help = 'Rolling back content'

    def handle(self, *args, **options):
        confirmed = self.confirmation_question(self.red("Are you sure you want to remove any migrated data?", True))

        if not confirmed:
            self.green('Ok, no harm have been done!')

        # todo: allow option to revert specific migrations.

        status_trackers = ContentMigrationStatus.objects.all()
        bar = self.progress_bar(len(status_trackers))

        self.yellow('Starting to rollback migration. Collecting migrated rows')
        for migration_status in status_trackers:
            bar.advance()

            # Get the model object.
            app, model = migration_status.model_target.split('.')
            model: Model = apps.get_model(app_label=app, model_name=model)
            model.objects.filter(pk=migration_status.destination_id).delete()
            migration_status.delete()
            self.green(f' Removing {model.__name__}:{migration_status.destination_id}')
