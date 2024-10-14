from setuptools import setup, find_packages

setup(
    name='mkdocs_chessboard_plugin',
    description='A MkDocs plugin to render FEN diagrams with chessboard.js',
    url='https://github.com/oschlueter/chess-training',
    author='Oliver Schlüter',
    packages=find_packages(),
    install_requires=[
        'mkdocs',
    ],
    entry_points={
        'mkdocs.plugins': [
            'chessboard = mkdocs_chessboard_plugin.plugin:ChessboardPlugin',
        ]
    },
)