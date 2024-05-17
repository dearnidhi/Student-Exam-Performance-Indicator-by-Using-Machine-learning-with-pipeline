from setuptools import find_packages, setup

def get_requirements(file_path: str) -> list:
    '''
    This function returns the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if not req.startswith("-e ")]
    return requirements

setup(
    name='Exam-Performance',
    version='0.0.1',
    author='Nidhi',
    author_email='nidhiyachouhan12@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    zip_safe=False  # This ensures that .egg-info folder is generated
)
