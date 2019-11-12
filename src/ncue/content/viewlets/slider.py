from plone.app.layout.viewlets import ViewletBase


class Slider(ViewletBase):

    def update(self):
        self.message = self.get_message()

    def get_message(self):
        return u'My message'

    def render(self):
        return super(Slider, self).render()
