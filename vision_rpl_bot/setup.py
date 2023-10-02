from setuptools import setup

package_name = 'vision_rpl_bot'

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
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_rpi_node = vision_rpl_bot.publisher:main',
            'subscriber_rpi_node = vision_rpl_bot.subscriber:main',
            'cmd_vel_to_pwm_node = vision_rpl_bot.cmd_to_pwm_driver:main',
        ],
    },
)
