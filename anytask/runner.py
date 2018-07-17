from django.test.runner import DiscoverRunner
from django.conf import settings

EXCLUDED_APPS = getattr(settings, 'TEST_EXCLUDE', [])


class ExcludeAppsTestSuiteRunner(DiscoverRunner):
    def build_suite(self, *args, **kwargs):
        suite = super(ExcludeAppsTestSuiteRunner, self).build_suite(*args, **kwargs)
        tests = []
        for case in suite:
            pkg = case.__class__.__module__.split('.')[0]
            if pkg not in EXCLUDED_APPS:
                tests.append(case)
        suite._tests = tests
        return suite
