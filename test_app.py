import numpy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from skimage.external import tifffile

from src.image_widget import ImDisplay, IndexedDisplay

class TestWidget(Widget):

    def show_im(self):

        im_d = ImDisplay(size_hint=(1., 1.))

        imtest1 = tifffile.imread('example_im.tif')
        imtest1 = imtest1.astype(float)

        #imtest2 = numpy.zeros((500, 500))
        #for i in range(500):
        #    imtest2[:, i] = i/2

        im_d.create_im(imtest1,  'PastelHeat')

        self.m_layout = FloatLayout(size=(Window.width, Window.height))

        with self.canvas:

            self.add_widget(self.m_layout)
            self.m_layout.add_widget(im_d)

            im_d.update_im(imtest1)

    def show_im_mapped(self):

        im_d = IndexedDisplay(size_hint=(1., 1.))
        imtest2 = numpy.zeros((500, 500))

        for i in range(500):
            imtest2[:, i] =i

        mapping = numpy.hstack((numpy.arange(250), numpy.arange(250)))
        mapping = mapping.astype(int)

        im_d.create_im(imtest2, 'PastelHeat', mapping)
        self.m_layout = FloatLayout(size=(Window.width, Window.height))

        with self.canvas:
            self.add_widget(self.m_layout)
            self.m_layout.add_widget(im_d)

    def update_size(self, window, width, height):

        self.m_layout.width = width
        self.m_layout.height = height

class TestImage(App):

    def build(self):
        test_widget = TestWidget()
        test_widget.show_im()
        Window.bind(on_resize=test_widget.update_size)
        return test_widget

if __name__ == '__main__':
    TestImage().run()
