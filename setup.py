import setuptools

setuptools.setup(
    name='MakinaLink',
    version='1.2.3',
    package_dir={
        'mrx_link.mrx_link_pipeline': 'MakinaLinkPipeline/mrx_link/mrx_link_pipeline',
        'mrx_link.mrx_link_git': 'MakinaLinkGit/mrx_link/mrx_link_git',
    },
    packages=['mrx_link.mrx_link_pipeline', 'mrx_link.mrx_link_git'],
)
