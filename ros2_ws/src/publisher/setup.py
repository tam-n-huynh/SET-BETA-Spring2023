from setuptools import setup

package_name = 'publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Max Huang',
    maintainer_email='menghuamh@gmail.com',
    description='This is a temporary publisher node to test the functionality of the shoulder_servos node',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = publisher.publisher_function:main',
                'listener = publisher.subscriber:main',
                'wheels = publisher.wheel_drive:main',
                'servos = publisher.shoulder_servos:main'
        ],
    },
)
