import pkg_resources

__name__ = "sample-project"
__version__ = pkg_resources.get_distribution(__name__).version

from sample_project.main import func
