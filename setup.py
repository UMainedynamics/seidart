from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class CustomBuildExt(build_ext):
    def build_extensions(self):
        # Add the Fortran compiler
        for ext in self.extensions:
            if ext.name == 'seidart.fortran.cpmlfdtd':
                ext.extra_f90_compile_args = ['-std=f95']
        super().build_extensions()

setup(
    name='seidart',
    version='2.2.3',
    packages=[
        'seidart',
        'seidart.fortran',
        'seidart.routines',
        'seidart.simulations',
        'seidart.visualization'
    ],
    ext_modules=[
        Extension(
            name='seidart.fortran.cpmlfdtd',
            sources=['src/seidart/fortran/cpmlfdtd.f95'],
            extra_f90_compile_args=['-std=f95'],  # Specify Fortran 95 standard
        ),
        # Add more extensions here as needed
    ],
    cmdclass={'build_ext': CustomBuildExt},
    entry_points={
        'console_scripts': [
            'prjbuild=seidart.routines.prjbuild:main',
            # other entry points...
        ]
    },
    install_requires=[
        'numpy',
        'setuptools',
        'wheel',
        'matplotlib',
        'seaborn'
    ]
)
