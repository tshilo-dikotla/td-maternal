from edc_locator.forms import LocatorFormMixin
from ..models import MaternalLocator


class MaternalLocatorForm(LocatorFormMixin):

    class Meta:
        model = MaternalLocator
        fields = '__all__'
