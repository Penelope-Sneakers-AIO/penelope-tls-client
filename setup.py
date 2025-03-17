from setuptools import setup, find_packages

setup(
    name='penelope_tls_client',
    version='0.0.1',
    packages=find_packages(),  # This ensures that all subpackages are included
    package_data={
        'penelope_tls_client.dependencies': ['*']
        # List any dependencies
    },
    include_package_data=True,  # Ensure package_data files are included

)
