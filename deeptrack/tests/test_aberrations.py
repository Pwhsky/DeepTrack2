import sys

# sys.path.append(".")  # Adds the module to path

import unittest
import numpy as np

from .. import aberrations

from ..scatterers import PointParticle
from ..optics import Fluorescence
from ..image import Image



class TestAberrations(unittest.TestCase):

    particle = PointParticle(position=(32, 32), position_unit="pixel", intensity=1)

    def testGaussianApodization(self):
        aberrated_optics = Fluorescence(
            NA=0.3,
            resolution=1e-6,
            magnification=10,
            wavelength=530e-9,
            output_region=(0, 0, 64, 48),
            padding=(64, 64, 64, 64),
            pupil=aberrations.GaussianApodization(sigma=0.5),
        )
        aberrated_particle = aberrated_optics(self.particle)

        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, np.ndarray)
            self.assertEqual(im.shape, (64, 48, 1))
        
        aberrated_particle.store_properties(True)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, Image)
            self.assertEqual(im.shape, (64, 48, 1))

    def testZernike(self):
        aberrated_optics = Fluorescence(
            NA=0.3,
            resolution=1e-6,
            magnification=10,
            wavelength=530e-9,
            output_region=(0, 0, 64, 48),
            padding=(64, 64, 64, 64),
            pupil=aberrations.Zernike(
                n=[2, 3], m=[0, 1], coefficient=[0.5, 0.3],
                ),
        )
        aberrated_particle = aberrated_optics(self.particle)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, np.ndarray)
            self.assertEqual(im.shape, (64, 48, 1))

        aberrated_particle.store_properties(True)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, Image)
            self.assertEqual(im.shape, (64, 48, 1))

    def testPiston(self):
        aberrated_optics = Fluorescence(
            NA=0.3,
            resolution=1e-6,
            magnification=10,
            wavelength=530e-9,
            output_region=(0, 0, 64, 48),
            padding=(64, 64, 64, 64),
            pupil=aberrations.Piston(coefficient=1),
        )
        aberrated_particle = aberrated_optics(self.particle)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, np.ndarray)
            self.assertEqual(im.shape, (64, 48, 1))

        aberrated_particle.store_properties(True)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, Image)
            self.assertEqual(im.shape, (64, 48, 1))

    def testVerticalTilt(self):
        aberrated_optics = Fluorescence(
            NA=0.3,
            resolution=1e-6,
            magnification=10,
            wavelength=530e-9,
            output_region=(0, 0, 64, 48),
            padding=(64, 64, 64, 64),
            pupil=aberrations.VerticalTilt(coefficient=1),
        )
        aberrated_particle = aberrated_optics(self.particle)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, np.ndarray)
            self.assertEqual(im.shape, (64, 48, 1))

        aberrated_particle.store_properties(True)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, Image)
            self.assertEqual(im.shape, (64, 48, 1))

    def testHorizontalTilt(self):
        aberrated_optics = Fluorescence(
            NA=0.3,
            resolution=1e-6,
            magnification=10,
            wavelength=530e-9,
            output_region=(0, 0, 64, 48),
            padding=(64, 64, 64, 64),
            pupil=aberrations.HorizontalTilt(coefficient=1),
        )
        aberrated_particle = aberrated_optics(self.particle)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, np.ndarray)
            self.assertEqual(im.shape, (64, 48, 1))

        aberrated_particle.store_properties(True)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, Image)
            self.assertEqual(im.shape, (64, 48, 1))

    def testObliqueAstigmatism(self):
        aberrated_optics = Fluorescence(
            NA=0.3,
            resolution=1e-6,
            magnification=10,
            wavelength=530e-9,
            output_region=(0, 0, 64, 48),
            padding=(64, 64, 64, 64),
            pupil=aberrations.ObliqueAstigmatism(coefficient=1),
        )
        aberrated_particle = aberrated_optics(self.particle)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, np.ndarray)
            self.assertEqual(im.shape, (64, 48, 1))

        aberrated_particle.store_properties(True)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, Image)
            self.assertEqual(im.shape, (64, 48, 1))

    def testDefocus(self):
        aberrated_optics = Fluorescence(
            NA=0.3,
            resolution=1e-6,
            magnification=10,
            wavelength=530e-9,
            output_region=(0, 0, 64, 48),
            padding=(64, 64, 64, 64),
            pupil=aberrations.Defocus(coefficient=1),
        )
        aberrated_particle = aberrated_optics(self.particle)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, np.ndarray)
            self.assertEqual(im.shape, (64, 48, 1))

        aberrated_particle.store_properties(True)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, Image)
            self.assertEqual(im.shape, (64, 48, 1))

    def testAstigmatism(self):
        aberrated_optics = Fluorescence(
            NA=0.3,
            resolution=1e-6,
            magnification=10,
            wavelength=530e-9,
            output_region=(0, 0, 64, 48),
            padding=(64, 64, 64, 64),
            pupil=aberrations.Astigmatism(coefficient=1),
        )
        aberrated_particle = aberrated_optics(self.particle)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, np.ndarray)
            self.assertEqual(im.shape, (64, 48, 1))

        aberrated_particle.store_properties(True)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, Image)
            self.assertEqual(im.shape, (64, 48, 1))

    def testObliqueTrefoil(self):
        aberrated_optics = Fluorescence(
            NA=0.3,
            resolution=1e-6,
            magnification=10,
            wavelength=530e-9,
            output_region=(0, 0, 64, 48),
            padding=(64, 64, 64, 64),
            pupil=aberrations.ObliqueTrefoil(coefficient=1),
        )
        aberrated_particle = aberrated_optics(self.particle)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, np.ndarray)
            self.assertEqual(im.shape, (64, 48, 1))

        aberrated_particle.store_properties(True)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, Image)
            self.assertEqual(im.shape, (64, 48, 1))

    def testVerticalComa(self):
        aberrated_optics = Fluorescence(
            NA=0.3,
            resolution=1e-6,
            magnification=10,
            wavelength=530e-9,
            output_region=(0, 0, 64, 48),
            padding=(64, 64, 64, 64),
            pupil=aberrations.VerticalComa(coefficient=1),
        )
        aberrated_particle = aberrated_optics(self.particle)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, np.ndarray)
            self.assertEqual(im.shape, (64, 48, 1))

        aberrated_particle.store_properties(True)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, Image)
            self.assertEqual(im.shape, (64, 48, 1))

    def testHorizontalComa(self):
        aberrated_optics = Fluorescence(
            NA=0.3,
            resolution=1e-6,
            magnification=10,
            wavelength=530e-9,
            output_region=(0, 0, 64, 48),
            padding=(64, 64, 64, 64),
            pupil=aberrations.HorizontalComa(coefficient=1),
        )
        aberrated_particle = aberrated_optics(self.particle)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, np.ndarray)
            self.assertEqual(im.shape, (64, 48, 1))

        aberrated_particle.store_properties(True)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, Image)
            self.assertEqual(im.shape, (64, 48, 1))

    def testTrefoil(self):
        aberrated_optics = Fluorescence(
            NA=0.3,
            resolution=1e-6,
            magnification=10,
            wavelength=530e-9,
            output_region=(0, 0, 64, 48),
            padding=(64, 64, 64, 64),
            pupil=aberrations.Trefoil(coefficient=1),
        )
        aberrated_particle = aberrated_optics(self.particle)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, np.ndarray)
            self.assertEqual(im.shape, (64, 48, 1))

        aberrated_particle.store_properties(True)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, Image)
            self.assertEqual(im.shape, (64, 48, 1))

    def testSphericalAberration(self):
        aberrated_optics = Fluorescence(
            NA=0.3,
            resolution=1e-6,
            magnification=10,
            wavelength=530e-9,
            output_region=(0, 0, 64, 48),
            padding=(64, 64, 64, 64),
            pupil=aberrations.SphericalAberration(coefficient=1),
        )
        aberrated_particle = aberrated_optics(self.particle)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, np.ndarray)
            self.assertEqual(im.shape, (64, 48, 1))

        aberrated_particle.store_properties(True)
        for z in (-100, 0, 100):
            im = aberrated_particle.resolve(z=z)
            self.assertIsInstance(im, Image)
            self.assertEqual(im.shape, (64, 48, 1))


if __name__ == "__main__":
    unittest.main()