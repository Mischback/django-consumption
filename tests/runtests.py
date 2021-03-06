#!/usr/bin/env python

# SPDX-License-Identifier: MIT

"""Includes an app-specific test runner.

This test runner heavily relies on Django's DiscoverRunner. In fact, it is very
close to Django's own test runner.
It accepts less options and looks for the tests to be run in the current
directory instead of app's test-directories.
    - available command line options:
        * --disable-optimisation    disables all test-specific optimisations
        * --enable-migrations       enables migrations during testing
        * --settings                specify a settings-module for the test run
        * --tag, -t                 specify one (or multiple) tags to be tested
        * --time                    enables time measurement during tests
        * --verbosity, -v           verbosity level (0, 1, 2, 3)
It can't be run on certain modules only, but on given tags.
"""

# Python imports
import argparse
import os
import sys
from typing import List

# Django imports
import django
from django.conf import settings
from django.test.utils import get_runner


def setup(
    disable_optimisation: bool,
    enable_migrations: bool,
    enable_timing: bool,
    verbosity: int,
) -> None:
    """Prepare the test environment.

    Basically, this function is used to inject test-specific settings. It should
    be ensured, that these settings are only relevant to testing. A minimal
    configuration to actually run the app has to be specified using Django's
    setting-mechanism.
    """

    class DisableMigrations:
        """A generic class to disable all migrations during tests.

        See setup()-function on how this is applied.
        """

        def __contains__(self, item: str) -> bool:
            return True

        def __getitem__(self, item: str) -> None:
            # return 'thesearenotthemigrationsyouarelookingfor'
            return None

    if not disable_optimisation:
        # don't test with debugging enabled
        settings.DEBUG = False
        settings.ALLOWED_HOSTS = []  # type: ignore[misc]

        # only use one password hasher (and the fastest one)
        settings.PASSWORD_HASHERS = [
            "django.contrib.auth.hashers.MD5PasswordHasher",
        ]  # type: ignore[misc]

        # turn off logging
        # Python imports
        import logging

        logging.disable(logging.CRITICAL)

        # disable migrations during tests
        if not enable_migrations:
            # see https://simpleisbetterthancomplex.com/tips/2016/08/19/django-tip-12-disabling-migrations-to-speed-up-unit-tests.html  # noqa: W505
            settings.MIGRATION_MODULES = DisableMigrations()
            if verbosity >= 2:
                print("Testing without applied migrations.")
        else:
            if verbosity >= 2:
                print("Testing with applied migrations.")
    else:
        if verbosity >= 2:
            print("Testing without any test-specific optimisations.")

    if enable_timing:
        # Python imports
        import time

        # Django imports
        from django import test

        def setUp(self):  # type: ignore[no-untyped-def]
            self.start_time = time.time()

        def tearDown(self):  # type: ignore[no-untyped-def]
            total = time.time() - self.start_time
            if total > 0.5:
                print(
                    "\n\t\033[91m{:.3f}s\t{}\033[0m".format(total, self._testMethodName)
                )

        test.TestCase.setUp = setUp  # type: ignore[assignment]
        test.TestCase.tearDown = tearDown  # type: ignore[assignment]

    # actually build the Django configuration
    django.setup()


def app_tests(
    disable_optimisation: bool,
    enable_migrations: bool,
    enable_timing: bool,
    tags: List[str],
    verbosity: int,
) -> int:
    """Get the TestRunner and runs the tests."""
    # provide a list of tags, that are excluded by default
    default_excluded_tags = ["requires_system_tex"]

    for excluded in default_excluded_tags:
        try:
            if excluded in tags:
                default_excluded_tags.remove(excluded)
        except TypeError:
            pass

    # prepare the actual test environment
    setup(disable_optimisation, enable_migrations, enable_timing, verbosity)

    # reuse Django's DiscoverRunner
    if not hasattr(settings, "TEST_RUNNER"):
        settings.TEST_RUNNER = "django.test.runner.DiscoverRunner"
    TestRunner = get_runner(settings)

    test_runner = TestRunner(
        verbosity=verbosity, tags=tags, exclude_tags=default_excluded_tags
    )

    failures = test_runner.run_tests(["."])

    return failures


if __name__ == "__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser(
        description="Run the django-auth_enhanced test suite"
    )
    parser.add_argument(
        "--disable-optimisation",
        action="store_true",
        dest="disable_optimisation",
        help="Disables the test specific optimisations.",
    )
    parser.add_argument(
        "--enable-migrations",
        action="store_true",
        dest="enable_migrations",
        help="Enables the usage of migrations during tests.",
    )
    parser.add_argument(
        "--settings",
        help="Python path to settings module, e.g. 'myproject.settings'. If "
        "this is not provided, 'tests.util.settings' will be used.",
    )
    parser.add_argument(
        "-t",
        "--tag",
        dest="tags",
        action="append",
        help="Run only tests with the specified tags. Can be used multiple times.",
    )
    parser.add_argument(
        "--time",
        action="store_true",
        dest="enable_timing",
        help="Enables time measurements for all tests.",
    )
    parser.add_argument(
        "-v",
        "--verbosity",
        default=1,
        type=int,
        choices=[0, 1, 2, 3],
        help="Verbosity level; 0=minimal, 3=maximal; default=1",
    )

    # actually get the options
    options = parser.parse_args()

    # run tests according to the options
    if options.settings:  # type: ignore[misc]
        os.environ["DJANGO_SETTINGS_MODULE"] = options.settings  # type: ignore[misc]
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "util.settings_test")
        options.settings = os.environ["DJANGO_SETTINGS_MODULE"]

    failures = app_tests(
        options.disable_optimisation,  # type: ignore[misc]
        options.enable_migrations,  # type: ignore[misc]
        options.enable_timing,  # type: ignore[misc]
        options.tags,  # type: ignore[misc]
        options.verbosity,  # type: ignore[misc]
    )

    if failures:
        sys.exit(1)
